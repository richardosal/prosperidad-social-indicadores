"""
predictsocial.py
------------------
Este archivo es el "mensajero" entre tu aplicación de Streamlit y DataRobot.

¿Qué hace?
1. Recibe los datos de UN beneficiario (los que el usuario llenó en el formulario).
2. Los convierte en un CSV de una sola fila (porque tu deployment de DataRobot
   solo acepta predicciones por lotes -> Batch Prediction API).
3. Envía ese CSV a DataRobot y espera a que termine de procesarlo.
4. Descarga el resultado y lo devuelve como un diccionario fácil de usar.

No necesitas tocar este archivo para usar la app. Solo asegúrate de tener
tu archivo .env configurado (ver .env.example).
"""

import os
import io
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Carga las variables secretas desde el archivo .env
load_dotenv()

DATAROBOT_API_TOKEN = os.getenv("DATAROBOT_API_TOKEN")
DATAROBOT_ENDPOINT = os.getenv(
    "DATAROBOT_ENDPOINT", "https://app.datarobot.com/api/v2"
)
DEPLOYMENT_ID = os.getenv("DEPLOYMENT_ID", "6a3df30bd8e3d1c090d66f29")

HEADERS = {
    "Authorization": f"Bearer {DATAROBOT_API_TOKEN}",
}


class DataRobotError(Exception):
    """Error personalizado para que los mensajes sean claros en la interfaz."""
    pass


def _validar_configuracion():
    if not DATAROBOT_API_TOKEN:
        raise DataRobotError(
            "No se encontró la API Key de DataRobot. "
            "Revisa que tu archivo .env tenga la variable DATAROBOT_API_TOKEN."
        )


def predecir_beneficiario(datos: dict, tiempo_espera_maximo: int = 60) -> dict:
    """
    Envía los datos de UN beneficiario a DataRobot y devuelve la predicción.

    Parámetros
    ----------
    datos : dict
        Diccionario con las variables del beneficiario, por ejemplo:
        {
            "bancarizado": "Si",
            "codigo_departamento": "05",
            "nombre_departamento": "Antioquia",
            ...
        }
    tiempo_espera_maximo : int
        Segundos máximos a esperar a que DataRobot termine el trabajo.

    Devuelve
    -------
    dict con la fila de resultado que envió DataRobot (incluye la predicción).
    """
    _validar_configuracion()

    # 1. Convertimos el diccionario en un CSV de una sola fila en memoria
    df_entrada = pd.DataFrame([datos])
    csv_bytes = df_entrada.to_csv(index=False).encode("utf-8")

    # 2. Creamos el trabajo de predicción por lotes (Batch Prediction Job)
    url_batch = f"{DATAROBOT_ENDPOINT}/batchPredictions/"
    payload = {
        "deploymentId": DEPLOYMENT_ID,
        "passthroughColumnsSet": "all",
        "csvSettings": {"delimiter": ","},
    }

    files = {"file": ("beneficiario.csv", io.BytesIO(csv_bytes), "text/csv")}

    respuesta = requests.post(
        url_batch, headers=HEADERS, data={"json": str(payload)}, files=files
    )

    if respuesta.status_code not in (200, 201, 202):
        raise DataRobotError(
            f"DataRobot respondió con un error al crear el trabajo: "
            f"{respuesta.status_code} - {respuesta.text}"
        )

    job = respuesta.json()
    job_id = job.get("id")
    if not job_id:
        raise DataRobotError("DataRobot no devolvió un ID de trabajo válido.")

    # 3. Esperamos a que el trabajo termine (consultamos su estado cada 2 seg)
    url_estado = f"{DATAROBOT_ENDPOINT}/batchPredictions/{job_id}/"
    segundos_esperados = 0
    estado = None

    while segundos_esperados < tiempo_espera_maximo:
        resp_estado = requests.get(url_estado, headers=HEADERS)
        resp_estado.raise_for_status()
        estado_json = resp_estado.json()
        estado = estado_json.get("status")

        if estado in ("COMPLETED", "FAILED", "ABORTED"):
            break

        time.sleep(2)
        segundos_esperados += 2

    if estado != "COMPLETED":
        raise DataRobotError(
            f"El trabajo de predicción no terminó a tiempo o falló. Estado final: {estado}"
        )

    # 4. Descargamos el resultado (el CSV con la predicción incluida)
    url_resultado = f"{DATAROBOT_ENDPOINT}/batchPredictions/{job_id}/download/"
    resp_resultado = requests.get(url_resultado, headers=HEADERS)
    resp_resultado.raise_for_status()

    df_resultado = pd.read_csv(io.StringIO(resp_resultado.text))

    if df_resultado.empty:
        raise DataRobotError("DataRobot devolvió un resultado vacío.")

    # Devolvemos la primera (y única) fila como diccionario
    return df_resultado.iloc[0].to_dict()
