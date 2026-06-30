import streamlit as st
import pandas as pd

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

with st.sidebar:
    st.title("🏛️ Prosperidad Social")
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
    genero=st.selectbox("Género", opciones("Genero"))
    etnia=st.selectbox("Etnia", opciones("Etnia"))
    discapacidad=st.selectbox("Discapacidad", opciones("Discapacidad"))
    estado=st.selectbox("Estado Beneficiario", opciones("EstadoBeneficiario"))
    rango=st.selectbox("Rango Edad", opciones("RangoEdad"))

with col2:
    deptos=opciones("NombreDepartamentoAtencion")
    dep=st.selectbox("Departamento", deptos)
    muni_df=df[df["NombreDepartamentoAtencion"].astype(str)==dep] if "NombreDepartamentoAtencion" in df.columns else pd.DataFrame()
    munis=sorted(muni_df["NombreMunicipioAtencion"].dropna().astype(str).unique()) if not muni_df.empty else []
    mun=st.selectbox("Municipio", munis)
    banc=st.selectbox("Bancarizado", opciones("Bancarizado"))
    cantidad=st.number_input("Cantidad Beneficiarios",1,20,1)

if st.button("Realizar predicción"):
    st.success("La interfaz está lista. En este punto se conectará el modelo de DataRobot.")
    st.metric("Resultado estimado","Pendiente de integrar IA")

st.divider()
st.subheader("Vista previa del conjunto de datos")
st.dataframe(df.head(20), use_container_width=True)
