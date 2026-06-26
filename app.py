import streamlit as st

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Prosperidad Social",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# ESTILOS CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background:#F4F7FA;
}

.titulo{
    font-size:42px;
    color:#0B5394;
    font-weight:bold;
    text-align:center;
}

.subtitulo{
    font-size:22px;
    color:#3d3d3d;
    text-align:center;
}

.bloque{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.10);
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    height:65px;
    font-size:22px;
    font-weight:bold;
    border-radius:12px;
    background:#0072CE;
    color:white;
}

.stButton>button:hover{
    background:#009E60;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# ENCABEZADO
# -----------------------------

st.markdown("<div class='titulo'>🏛️ Prosperidad Social</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitulo'>Sistema Inteligente de Predicción de Beneficiarios</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# INFORMACIÓN
# -----------------------------

col1,col2,col3=st.columns(3)

with col1:
    st.info("👤 Información del ciudadano")

with col2:
    st.info("📍 Ubicación")

with col3:
    st.info("💰 Beneficios")

st.divider()

st.success("✅ La aplicación se está construyendo correctamente.")
