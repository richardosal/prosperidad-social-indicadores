import pandas as pd
import streamlit as st

URL = "https://www.datos.gov.co/resource/xfif-myr2.csv?$limit=50000"

@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv(URL)
        return df
    except Exception:
        return pd.DataFrame()
