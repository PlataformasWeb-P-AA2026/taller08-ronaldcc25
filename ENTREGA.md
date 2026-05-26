# Entrega taller08

## Fuente de datos utilizada

- Archivo: `data/jugadores_futbol.csv`

## Tecnologías utilizadas

- Python 3
- SQLAlchemy
- SQLite
- Streamlit
- Pandas

## Entidades implementadas

- Continente
- Pais
- Jugador

## Archivos principales del proyecto

- `modelos.py`
- `base_datos.py`
- `importador_datos.py`
- `importacion_sqlite.py`
- `reportes.py`
- `generar_evidencias.py`
- `fronted/app.py`
- `PASOS_A_SEGUIR.md`

## Orden de ejecución

El orden completo de ejecución se encuentra en:

- `PASOS_A_SEGUIR.md`

## Resultado de la carga en SQLite

Base de datos:

- `paises.db`


## Cambio a otras bases de datos

El script `importacion_sqlite.py` deja la URL de SQLite activa y contiene líneas comentadas con ejemplos de URLs para otros motores. Para probar otro motor, solo se cambia la línea `DATABASE_URL` dentro del mismo archivo.

## Evidencias a adjuntar

### Evidencia SQLite

Inserta aquí las capturas o imágenes de:

- creación de la base SQLite desde terminal
- ejecución de `importacion_sqlite.py`
- ejecución de `generar_evidencias.py`
- archivos generados en `evidencias/sqlite`

### Evidencia del frontend funcionando

Inserta aquí las capturas o imágenes de:

- tabla de jugadores
- resumen por continente
- resumen por país
