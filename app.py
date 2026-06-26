import streamlit as st

# ------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------------------------
st.set_page_config(
    page_title="Prosperidad Social",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# CSS
# ------------------------------------------------
st.markdown("""
<style>

.main{
    background:#F4F7FA;
}

h1{
    color:#0056A3;
    text-align:center;
}

h3{
    color:#4A4A4A;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:60px;
    border-radius:12px;
    background:#0066CC;
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#00994D;
    color:white;
}

div[data-testid="stMetric"]{
    background:white;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 0px 8px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# ENCABEZADO
# ------------------------------------------------

st.title("🏛️ Prosperidad Social")

st.subheader("Sistema Inteligente de Predicción de Beneficiarios")

st.write("---")

# ------------------------------------------------
# MÉTRICAS
# ------------------------------------------------

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Modelo IA","Activo")

with c2:
    st.metric("Variables","20")

with c3:
    st.metric("Estado","Listo")

st.write("---")

st.success("La aplicación se está construyendo correctamente.")

st.info("En el siguiente paso agregaremos el formulario del modelo.")
