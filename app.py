import streamlit as st

# ======================================================
# CONFIGURACIÓN
# ======================================================

st.set_page_config(
    page_title="Prosperidad Social",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# ESTILOS
# ======================================================

st.markdown("""
<style>

.main{
    background:#F4F7FA;
}

h1,h2,h3{
    color:#0056A3;
}

.stButton>button{
    width:100%;
    height:60px;
    border-radius:12px;
    background:#0056A3;
    color:white;
    font-size:22px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#00843D;
    color:white;
}

div[data-testid="stMetric"]{
    background:white;
    border-radius:12px;
    padding:18px;
    box-shadow:0px 0px 8px rgba(0,0,0,.15);
}

label{
    font-size:18px !important;
    font-weight:bold !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("🏛️ Prosperidad Social")

    st.success("🟢 Sistema Activo")

    st.markdown("---")

    st.metric("Variables",20)

    st.metric("Modelo","IA")

    st.metric("Estado","Disponible")

    st.markdown("---")

    st.write("### Información")

    st.write("✔ Inteligencia Artificial")

    st.write("✔ Streamlit")

    st.write("✔ DataRobot")

    st.write("✔ Proyecto Académico")

    st.markdown("---")

    st.caption("Versión 1.0")

# ======================================================
# ENCABEZADO
# ======================================================

st.title("🏛️ Prosperidad Social")

st.subheader("Sistema Inteligente de Predicción de Beneficiarios")

st.write(
"""
Esta aplicación permite ingresar la información de un beneficiario
para posteriormente realizar una predicción utilizando Inteligencia Artificial.
"""
)

st.divider()

# ======================================================
# INDICADORES
# ======================================================

c1,c2,c3,c4=st.columns(4)

c1.metric("Modelo","Activo")

c2.metric("Variables","20")

c3.metric("Estado","Listo")

c4.metric("Versión","1.0")

st.divider()

# ======================================================
# FORMULARIO
# ======================================================

st.header("Datos del Beneficiario")

col1,col2=st.columns(2)

with col1:

    genero=st.selectbox(
        "Género",
        ["Femenino","Masculino"]
    )

    rangoEdad=st.selectbox(
        "Rango de Edad",
        [
            "0-5",
            "6-12",
            "13-17",
            "18-28",
            "29-59",
            "60+"
        ]
    )

    escolaridad=st.selectbox(
        "Nivel de Escolaridad",
        [
            "Ninguno",
            "Primaria",
            "Secundaria",
            "Técnico",
            "Tecnólogo",
            "Universitario"
        ]
    )

    discapacidad=st.selectbox(
        "Discapacidad",
        ["Sí","No"]
    )

    etnia=st.selectbox(
        "Etnia",
        [
            "Ninguna",
            "Indígena",
            "Afro",
            "ROM",
            "Raizal"
        ]
    )

    bancarizado=st.selectbox(
        "Bancarizado",
        ["Sí","No"]
    )

with col2:

    departamento=st.text_input("Departamento")

    municipio=st.text_input("Municipio")

    tipoPoblacion=st.text_input("Tipo de Población")

    estado=st.selectbox(
        "Estado Beneficiario",
        [
            "Activo",
            "Suspendido",
            "Retirado"
        ]
    )

    tipoBeneficio=st.text_input("Tipo de Beneficio")

    cantidad=st.number_input(
        "Cantidad de Beneficiarios",
        min_value=1,
        max_value=20,
        value=1
    )

st.divider()

# ======================================================
# BOTÓN
# ======================================================

if st.button("🔍 REALIZAR PREDICCIÓN"):

    st.success("Predicción ejecutada correctamente.")

    st.divider()

    st.header("Resultado")

    a,b,c=st.columns(3)

    a.metric(
        "Predicción",
        "Rango Medio"
    )

    b.metric(
        "Confianza",
        "93%"
    )

    c.metric(
        "Estado IA",
        "Correcto")

    st.info(
        """
        **Nota**

        Esta versión muestra un resultado de prueba.

        En el siguiente paso conectaremos el modelo de DataRobot para obtener
        predicciones reales.
        """
    )
