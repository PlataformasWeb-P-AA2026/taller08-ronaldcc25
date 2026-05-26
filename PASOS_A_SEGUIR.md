# Pasos a seguir

## 1. Crear el entorno virtual

```sh
python3 -m venv .venv
```

## 2. Activar el entorno virtual

```sh
. .venv/bin/activate
```

## 3. Instalar las dependencias

```sh
pip install -r requirements.txt
```

## 4. Verificar que el archivo de datos exista

```sh
ls data
```

Debe aparecer:

```text
jugadores_futbol.csv
```

## 5. Crear la base de datos SQLite desde la terminal

```sh
sqlite3 paises.db ".databases"
```

## 6. Importar los datos a SQLite

```sh
python importacion_sqlite.py
```

## 7. Generar evidencias de SQLite

```sh
python generar_evidencias.py
```

## 8. Levantar el frontend con SQLite

```sh
DATABASE_URL=sqlite:///paises.db streamlit run fronted/app.py
```

## 9. Abrir la aplicación en el navegador

```text
http://localhost:8501
```

## Ejecución completa en orden para SQLite

```sh
cd /home/asus/Yo/taller08-ronaldcc25
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
ls data
sqlite3 paises.db ".databases"
python importacion_sqlite.py
python generar_evidencias.py
DATABASE_URL=sqlite:///paises.db streamlit run fronted/app.py
```

## Cambio de motor de base de datos en el mismo script

Si luego quieres probar con otra base de datos, abre `importacion_sqlite.py` y cambia la línea activa `DATABASE_URL` por una de las líneas comentadas.

Ejemplos incluidos dentro del script:

```python
DATABASE_URL = "sqlite:///paises.db"
# DATABASE_URL = "mysql+pymysql://root:TU_CLAVE@localhost/paises"
# DATABASE_URL = "mysql+pymysql://usuario:TU_CLAVE@localhost/paises"
```
