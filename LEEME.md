# Prosperidad Social IA — Guía súper sencilla 🧭

## ¿Qué hace este proyecto?
Muestra un formulario bonito donde alguien llena los datos de un beneficiario,
y una inteligencia artificial (entrenada en DataRobot) devuelve una predicción.

## 🔑 Paso 1: Configura tu llave secreta (API Key)
1. Copia el archivo `.env.example` y renómbralo a `.env`.
2. Abre `.env` y reemplaza `tu_api_key_aqui` por tu API Key real de DataRobot.
3. **Nunca subas el archivo `.env` a GitHub** (ya viene protegido si usas `.gitignore`).

## 📦 Paso 2: Instala lo necesario
Abre una terminal en la carpeta del proyecto y escribe:

```
pip install -r requirements.txt
```

## ▶️ Paso 3: Ejecuta la aplicación
```
streamlit run app.py
```

Se abrirá una ventana en tu navegador con el formulario.

## 🧠 ¿Cómo funciona por dentro?
- `app.py` → es la parte visual (el formulario y los colores).
- `predictsocial.py` → es el "mensajero" que habla con DataRobot.
- Cuando llenas el formulario y das clic en **Realizar predicción**:
  1. Tus datos se convierten en un mini-CSV de una sola fila.
  2. Se envía a DataRobot (Batch Prediction API).
  3. Se espera unos segundos a que DataRobot procese.
  4. Se descarga el resultado y se muestra en pantalla.

## ⚠️ Importante: ajusta los nombres de columnas
Los nombres de las variables del formulario (`bancarizado`, `codigo_departamento`,
etc.) deben coincidir **exactamente** con los nombres de columnas que tu modelo
espera en DataRobot. Si el modelo no reconoce una columna, revisa:
1. El nombre exacto de la columna en tu archivo original de Prosperidad Social.
2. Que ese mismo nombre esté escrito igual en `app.py` (diccionario `datos_beneficiario`).

## 🎨 ¿Quieres cambiar los colores o el logo?
Busca la sección de estilos (`st.markdown` con `<style>`) al inicio de `app.py`.
Ahí puedes cambiar `--azul-institucional` y `--naranja-institucional` por los
colores oficiales de tu entidad.
