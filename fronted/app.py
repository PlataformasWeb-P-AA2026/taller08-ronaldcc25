import sys
from pathlib import Path

import streamlit as st
from sqlalchemy.orm import Session

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from base_datos import get_engine, resolve_database_url
from reportes import (
    continent_summary_dataframe,
    country_summary_dataframe,
    players_dataframe,
)

st.set_page_config(page_title="Taller 08 - Jugadores", layout="wide")

st.title("Taller 08 - Integración de datos y ORM")

url = resolve_database_url()
st.caption(f"Base de datos activa: {url}")

try:
    engine = get_engine(url)
    with Session(engine) as session:
        detalle = players_dataframe(session)
        resumen_continente = continent_summary_dataframe(session)
        resumen_pais = country_summary_dataframe(session)

    st.subheader("Tabla de jugadores")
    st.dataframe(detalle, use_container_width=True)

    st.subheader("Resumen por continente")
    st.dataframe(resumen_continente, use_container_width=True)

    st.subheader("Resumen por país")
    st.dataframe(resumen_pais, use_container_width=True)
except Exception as error:
    st.error(
        "No se pudo consultar la base de datos. Importa primero la información con importacion_sqlite.py o revisa DATABASE_URL."
    )
    st.exception(error)
