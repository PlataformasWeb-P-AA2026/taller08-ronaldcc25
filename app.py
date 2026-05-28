import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from configuracion import cadena_base_datos

# 1. Conexión a la base de datos
engine = create_engine(cadena_base_datos)

# 2. La consulta SQL "mágica" con JOINs para traer todo de golpe
# Tomamos el continente del país de nacimiento del jugador
query = """
    SELECT
        j.nombre AS nombre_jugador,
        p_nac.nombre AS pais_nacimiento,
        p_juego.nombre AS pais_donde_juega,
        j.posicion,
        j.edad,
        j.partidos_seleccion AS numero_partidos_seleccion,
        j.goles_seleccion,
        c.nombre AS continente
    FROM jugador j
    JOIN pais p_nac ON j.pais_nacimiento_id = p_nac.id
    JOIN pais p_juego ON j.pais_donde_juega_id = p_juego.id
    JOIN continente c ON p_nac.continente_id = c.id
"""

# Metemos el resultado directo a un DataFrame
df = pd.read_sql(query, engine)

# 3. Interfaz de Streamlit
st.title("⚽ Estadísticas de Jugadores")

# --- TABLA 1: Información completa ---
st.subheader("1. Listado General")
st.dataframe(df)

# --- TABLA 2: Agrupación por Continente ---
st.subheader("2. Resumen por Continente")
# groupby agrupa por continente, 'count' cuenta los nombres, 'sum' suma los goles
df_continentes = (
    df.groupby("continente")
    .agg(
        numero_jugadores=("nombre_jugador", "count"),
        numero_goles=("goles_seleccion", "sum"),
    )
    .reset_index()
)

st.dataframe(df_continentes)

# --- TABLA 3: Agrupación por País ---
st.subheader("3. Resumen por País (Nacimiento)")
df_paises = (
    df.groupby("pais_nacimiento")
    .agg(
        numero_jugadores=("nombre_jugador", "count"),
        numero_goles=("goles_seleccion", "sum"),
    )
    .reset_index()
)

# Renombramos la columna para que quede justo como pide el taller
df_paises = df_paises.rename(columns={"pais_nacimiento": "pais"})

st.dataframe(df_paises)
