import streamlit as st
from predictsocial import cargar_modelo, preparar_datos, predecir

st.set_page_config(
    page_title="Prosperidad Social IA",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>
.stButton>button{
    width:100%;
    height:60px;
    font-size:22px;
    border-radius:12px;
    background:#0056A6;
    color:white;
}

div[data-baseweb="select"]{
    font-size:20px;
}

input{
    font-size:20px !important;
}

h1{
    color:#0056A6;
}

.block-container{
    padding-top:2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🏛️ Sistema Inteligente de Prosperidad Social")

st.write(
"""
Esta aplicación utiliza Inteligencia Artificial para estimar el
**Rango del Último Beneficio Asignado** de un beneficiario
según sus características.
"""
)

col1,col2=st.columns(2)

with col1:

    genero=st.selectbox(
        "Género",
        ["FEMENINO","MASCULINO"]
    )

    edad=st.selectbox(
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
        "Nivel Escolaridad",
        [
            "NINGUNO",
            "PRIMARIA",
            "SECUNDARIA",
            "TÉCNICO",
            "TECNÓLOGO",
            "UNIVERSITARIO"
        ]
    )

    discapacidad=st.selectbox(
        "Discapacidad",
        ["SI","NO"]
    )

    etnia=st.selectbox(
        "Etnia",
        [
            "NINGUNA",
            "INDÍGENA",
            "AFRO",
            "ROM",
            "RAIZAL"
        ]
    )

with col2:

    departamento=st.text_input("Departamento")

    municipio=st.text_input("Municipio")

    poblacion=st.text_input("Tipo de población")

    estado=st.selectbox(
        "Estado Beneficiario",
        [
            "ACTIVO",
            "SUSPENDIDO",
            "RETIRADO"
        ]
    )

    bancarizado=st.selectbox(
        "Bancarizado",
        ["SI","NO"]
    )

    cantidad=st.number_input(
        "Cantidad Beneficiarios",
        1,
        20,
        1
    )

st.divider()

if st.button("REALIZAR PREDICCIÓN"):

    modelo=cargar_modelo()

    datos=preparar_datos(
        genero,
        edad,
        escolaridad,
        discapacidad,
        etnia,
        departamento,
        municipio,
        poblacion,
        estado,
        bancarizado,
        cantidad
    )

    resultado=predecir(modelo,datos)

    st.success(f"Resultado estimado: {resultado}")
