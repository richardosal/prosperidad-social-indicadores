"""
app.py
------
Interfaz de usuario (la "cara bonita") de Prosperidad Social IA.

Aquí el usuario llena un formulario con los datos de un beneficiario,
y al dar clic en "Realizar predicción", la app le pide a predictsocial.py
que consulte el modelo en DataRobot y muestra el resultado en pantalla.
"""

import streamlit as st
from datetime import date
from predictsocial import predecir_beneficiario, DataRobotError

# ---------------------------------------------------------------------------
# Configuración general de la página
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Prosperidad Social IA",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Estilos institucionales (colores tipo entidad de gobierno: azul + naranja)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        :root {
            --azul-institucional: #003366;
            --naranja-institucional: #F4A11A;
            --gris-fondo: #F5F7FA;
        }

        .stApp {
            background-color: var(--gris-fondo);
        }

        header[data-testid="stHeader"] {
            background: var(--azul-institucional);
        }

        section[data-testid="stSidebar"] {
            background-color: var(--azul-institucional);
        }
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        .encabezado {
            background: linear-gradient(90deg, var(--azul-institucional) 0%, #004a99 100%);
            padding: 28px 36px;
            border-radius: 14px;
            color: white;
            margin-bottom: 24px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.12);
        }
        .encabezado h1 {
            margin: 0;
            font-size: 30px;
        }
        .encabezado p {
            margin: 6px 0 0 0;
            opacity: 0.9;
            font-size: 15px;
        }

        .tarjeta {
            background: white;
            border-radius: 14px;
            padding: 22px 26px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
            border-left: 6px solid var(--naranja-institucional);
            margin-bottom: 18px;
        }

        .resultado-ok {
            background: #E9F7EF;
            border-left: 6px solid #27AE60;
            border-radius: 14px;
            padding: 22px 26px;
        }

        .resultado-alerta {
            background: #FDF2E3;
            border-left: 6px solid var(--naranja-institucional);
            border-radius: 14px;
            padding: 22px 26px;
        }

        div.stButton > button {
            background-color: var(--naranja-institucional);
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 10px 26px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #d88f0d;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Encabezado institucional
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="encabezado">
        <h1>🤝 Prosperidad Social IA</h1>
        <p>Sistema de apoyo a la gestión de beneficiarios · Predicción inteligente con DataRobot</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Barra lateral: información del sistema
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ℹ️ Acerca de este sistema")
    st.write(
        "Esta herramienta permite ingresar los datos de un beneficiario y "
        "obtener una predicción generada por un modelo de inteligencia "
        "artificial entrenado en DataRobot."
    )
    st.markdown("---")
    st.markdown("### 📋 Pasos para usarla")
    st.write("1. Diligencie el formulario\n2. Verifique los datos\n3. Pulse *Realizar predicción*\n4. Revise el resultado")
    st.markdown("---")
    st.caption("Versión demo · Ajuste las variables según su dataset final")

# ---------------------------------------------------------------------------
# Formulario principal
# ---------------------------------------------------------------------------
st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
st.subheader("📝 Datos del beneficiario")

with st.form("formulario_beneficiario"):
    col1, col2, col3 = st.columns(3)

    with col1:
        bancarizado = st.selectbox("Bancarizado", ["Sí", "No"])
        codigo_departamento = st.text_input("Código departamento", placeholder="Ej: 05")
        nombre_departamento = st.text_input("Nombre departamento", placeholder="Ej: Antioquia")
        codigo_municipio = st.text_input("Código municipio", placeholder="Ej: 05001")
        nombre_municipio = st.text_input("Nombre municipio", placeholder="Ej: Medellín")
        pais = st.text_input("País", value="Colombia")

    with col2:
        discapacidad = st.selectbox("Discapacidad", ["Sí", "No"])
        estado_beneficiario = st.selectbox(
            "Estado del beneficiario", ["Activo", "Inactivo", "Suspendido", "Retirado"]
        )
        etnia = st.selectbox(
            "Etnia", ["Ninguna", "Indígena", "Afrodescendiente", "Raizal", "Rrom/Gitano", "Otra"]
        )
        genero = st.selectbox("Género", ["Femenino", "Masculino", "Otro"])
        nivel_escolaridad = st.selectbox(
            "Nivel de escolaridad",
            ["Ninguno", "Primaria", "Secundaria", "Técnico", "Tecnólogo", "Universitario", "Posgrado"],
        )
        rango_edad = st.selectbox(
            "Rango de edad", ["0-17", "18-28", "29-40", "41-60", "61-75", "76+"]
        )

    with col3:
        titular = st.selectbox("Es titular", ["Sí", "No"])
        cantidad_beneficiarios = st.number_input("Cantidad de beneficiarios", min_value=1, value=1)
        tipo_asignacion_beneficio = st.text_input("Tipo de asignación del beneficio")
        tipo_beneficio = st.text_input("Tipo de beneficio")
        tipo_documento = st.selectbox("Tipo de documento", ["CC", "TI", "CE", "RC", "PPT"])
        tipo_poblacion = st.text_input("Tipo de población")

    col4, col5, col6 = st.columns(3)
    with col4:
        fecha_inscripcion = st.date_input("Fecha de inscripción del beneficiario", value=date.today())
    with col5:
        fecha_ultimo_beneficio = st.date_input("Fecha del último beneficio asignado", value=date.today())
    with col6:
        rango_beneficios_consolidado = st.text_input("Rango de beneficios consolidado asignado")

    rango_ultimo_beneficio = st.text_input("Rango del último beneficio asignado")

    enviado = st.form_submit_button("🔍 Realizar predicción")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Al enviar el formulario: llamamos al mensajero (predictsocial.py)
# ---------------------------------------------------------------------------
if enviado:
    datos_beneficiario = {
        "bancarizado": bancarizado,
        "codigo_departamento": codigo_departamento,
        "nombre_departamento": nombre_departamento,
        "codigo_municipio": codigo_municipio,
        "nombre_municipio": nombre_municipio,
        "pais": pais,
        "discapacidad": discapacidad,
        "estado_beneficiario": estado_beneficiario,
        "etnia": etnia,
        "genero": genero,
        "nivel_escolaridad": nivel_escolaridad,
        "rango_edad": rango_edad,
        "titular": titular,
        "cantidad_beneficiarios": cantidad_beneficiarios,
        "tipo_asignacion_beneficio": tipo_asignacion_beneficio,
        "tipo_beneficio": tipo_beneficio,
        "tipo_documento": tipo_documento,
        "tipo_poblacion": tipo_poblacion,
        "fecha_inscripcion_beneficiario": str(fecha_inscripcion),
        "fecha_ultimo_beneficiario_asignado": str(fecha_ultimo_beneficio),
        "rango_beneficios_consolidado_asignado": rango_beneficios_consolidado,
        "rango_ultimo_beneficiario_asignado": rango_ultimo_beneficio,
    }

    with st.spinner("Consultando el modelo en DataRobot, un momento..."):
        try:
            resultado = predecir_beneficiario(datos_beneficiario)

            st.markdown('<div class="resultado-ok">', unsafe_allow_html=True)
            st.subheader("✅ Resultado de la predicción")
            st.write(
                "El modelo procesó la información y devolvió el siguiente resultado:"
            )
            st.json(resultado)
            st.markdown("</div>", unsafe_allow_html=True)

        except DataRobotError as error:
            st.markdown('<div class="resultado-alerta">', unsafe_allow_html=True)
            st.subheader("⚠️ No se pudo completar la predicción")
            st.write(str(error))
            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as error:  # noqa: BLE001
            st.markdown('<div class="resultado-alerta">', unsafe_allow_html=True)
            st.subheader("⚠️ Ocurrió un error inesperado")
            st.write(f"Detalle técnico: {error}")
            st.markdown("</div>", unsafe_allow_html=True)
