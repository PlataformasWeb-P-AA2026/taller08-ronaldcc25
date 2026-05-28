# Pasos a seguir

## 1. Crear el entorno virtual

```sh
python3 -m venv .venv
```

## 2. Activar el entorno virtual

```sh
. .venv/bin/activate
```

# Pasos para instalar todo en la terminal (Ubuntu/Linux)

# 1. Actualizar repositorios e instalar herramientas del sistema (Python, Pip, Virtualenv y SQLite3)
sudo apt update && sudo apt install -y python3 python3-pip python3-venv sqlite3

# 2. Crear y activar el entorno virtual (opcional pero recomendado, veo que ya usas .venv)
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar todas las librerías de Python desde el archivo requirements.txt
pip install -r requirements.txt


## 3. Instalar las dependencias

```sh
pip install -r requirements.txt
```

## 4. Crear la base de datos SQLite

```sh
sqlite3 paises.db ".databases"
```

streamlit run app.py
