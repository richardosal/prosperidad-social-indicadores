import streamlit as st
import requests
import json
from predictsocial import preparar_datos

# Configuración API DataRobot
DATAROBOT_API_KEY = ""
DATAROBOT_DEPLOYMENT_ID = ""
DATAROBOT_HOST = "https://app.datarobot.com"

headers = {
    "Authorization": f"Bearer {DATAROBOT_API_KEY}",
    "Content-Type": "application/json",
}

# Configuración de la página
st.set_page_config(page_title="Prosperidad Social", layout="centered")

# Encabezado institucional
st.title("📊 Plataforma de Prosperidad Social")
st.markdown("Interfaz oficial para análisis de beneficiarios. *Accesible, clara y fácil de usar.*")

# Formulario dinámico con variables del dataset
st.header("Formulario de Beneficiario")

bancarizada = st.selectbox("¿Está bancarizada?", ["Sí", "No"])
codigo_departamento = st.text_input("Código del Departamento de Atención")
codigo_municipio = st.text_input("Código del Municipio de Atención")
discapacidad = st.selectbox("¿Tiene discapacidad?", ["Sí", "No"])
estado_beneficiario = st.selectbox("Estado del beneficiario", ["Activo", "Inactivo", "Suspendido"])
etnia = st.selectbox("Etnia", ["Indígena", "Afrodescendiente", "Mestizo", "Otro"])
fecha_inscripcion = st.date_input("Fecha de inscripción")
genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
nivel_escolaridad = st.selectbox("Nivel de escolaridad", ["Primaria", "Secundaria", "Universitaria", "Ninguno"])
tipo_beneficio = st.selectbox("Tipo de beneficio", ["Monetario", "En especie", "Otro"])
rango_edad = st.slider("Edad", 0, 100, 30)

# Botón grande para predicción
if st
