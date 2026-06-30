import streamlit as st
import pandas as pd

from datos import cargar_datos
from modelo import preparar_datos


st.set_page_config(page_title="Prosperidad Social",
                   page_icon="🏛️",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
.main {background:#F4F7FA;}
.stButton>button{
width:100%;
height:55px;
font-size:22px;
background:#0056A3;
color:white;
border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_datos():
    url="https://www.datos.gov.co/resource/xfif-myr2.csv?$limit=50000"
    try:
        return pd.read_csv(url)
    except Exception:
        return pd.DataFrame()

df=cargar_datos()
st.write(df.columns.tolist())

with st.sidebar:
    st.title("🏛️ Prosperidad Social")
  # Cargar datos oficiales
df = cargar_datos()

if df.empty:
    st.error("No fue posible cargar los datos de Prosperidad Social.")
    st.stop()
    st.success("Sistema activo")
    st.metric("Variables", len(df.columns) if not df.empty else 0)
    st.metric("Registros", f"{len(df):,}" if not df.empty else "0")

st.title("Sistema Inteligente de Prosperidad Social")

if df.empty:
    st.error("No fue posible cargar el conjunto de datos.")
    st.stop()

st.subheader("Indicadores")
c1,c2,c3=st.columns(3)
c1.metric("Beneficiarios", f"{len(df):,}")
c2.metric("Columnas", len(df.columns))
c3.metric("Modelo", "Preparado")

st.divider()
st.header("Formulario")

def opciones(col):
    if col in df.columns:
        return sorted(df[col].dropna().astype(str).unique().tolist())
    return []

col1,col2=st.columns(2)

with col1:
    genero=st.selectbox("Género", opciones("genero"))
    etnia=st.selectbox("Etnia", opciones("etnia"))
    discapacidad=st.selectbox("Discapacidad", opciones("discapacidad"))
    estado=st.selectbox("Estado Beneficiario", opciones("estadobeneficiario"))
    rango=st.selectbox("Rango Edad", opciones("rangoedad"))

with col2:
    deptos=opciones("nombredepartamentoatencion")
    dep = st.selectbox("Departamento", deptos)
    muni_df=df[df["nombredepartamentoatencion"].astype(str)==dep] if "nombredepartamentoatencion" in df.columns else pd.DataFrame()
    munis=sorted(muni_df["nombremunicipioatencion"].dropna().astype(str).unique()) if not muni_df.empty else []
    mun = st.selectbox("Municipio", munis)
    banc = st.selectbox("Bancarizado", opciones("bancarizado"))
    cantidad = st.number_input(
    "Cantidad de beneficiarios",
    min_value=1,
    max_value=20,
    value=1
)
if st.button("🔍 Realizar predicción"):

    datos_prediccion = preparar_datos(
        genero,
        etnia,
        discapacidad,
        estado,
        rango,
        dep,
        mun,
        banc,
        cantidad
    )

    st.success("✅ Información preparada correctamente.")

    st.subheader("Datos que se enviarán al modelo")

    st.dataframe(datos_prediccion)

st.divider()
st.subheader("Vista previa del conjunto de datos")
st.dataframe(df.head(20), use_container_width=True)
