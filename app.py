import streamlit as st
import requests
import json
from predilsocial import preparar_datos

# Configuración API DataRobot
DATAROBOT_API_KEY = ""
DATAROBOT_DEPLOYMENT_ID = ""
DATAROBOT_HOST = "https://app.datarobot.com"

headers = {
    "Authorization": f"Bearer {DATAROBOT_API_KEY}",
    "Content-Type": "application/json",
}

# Interfaz institucional
st.set_page_config(page_title="Prosperidad Social", layout="centered")

st.title("📊 Plataforma de Prosperidad Social")
st.write("Aplicación oficial para análisis de beneficiarios. Interfaz sencilla y accesible.")

# Formulario dinámico para variables
st.header("Ingrese la información del beneficiario")

bancarizada = st.selectbox("¿Está bancarizada?", ["Sí", "No"])
genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
edad = st.slider("Edad", 18, 100, 30)
nivel_escolaridad = st.selectbox("Nivel de escolaridad", ["Primaria", "Secundaria", "Universitaria", "Ninguno"])
discapacidad = st.selectbox("¿Tiene discapacidad?", ["Sí", "No"])
etnia = st.selectbox("Etnia", ["Indígena", "Afrodescendiente", "Mestizo", "Otro"])
estado_beneficiario = st.selectbox("Estado del beneficiario", ["Activo", "Inactivo", "Suspendido"])

# Botón de predicción
if st.button("Generar Predicción"):
    datos = preparar_datos(
        bancarizada, genero, edad, nivel_escolaridad, discapacidad, etnia, estado_beneficiario
    )
