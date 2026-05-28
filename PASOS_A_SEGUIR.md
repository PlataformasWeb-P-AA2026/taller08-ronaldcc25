# Pasos a seguir

Driver Para PostgreSQL, el driver más común es psycopg2-binary.
Driver Para MySQL / MariaDB, el driver más usado es pymysql

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

python3 creacion-tablas.py

python3 importacion_datos.py

streamlit run app.py
```


PARA MARIADB

```sh
sudo apt update && sudo apt install mariadb-server -y

sudo mysql

CREATE DATABASE paises;
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
EXIT;

# driver de python3
pip install pymysql

# nueva cadena de conexión
cadena_base_datos = "mysql+pymysql://root:1234@localhost:3306/paises"
```

PARA POSTGRESQL
```sh
sudo apt install postgresql postgresql-contrib -y

sudo -u postgres psql

CREATE DATABASE paises;
ALTER USER postgres WITH PASSWORD '1234';
\q

# driver de python3
pip install psycopg2-binary

# nueva cadena de conexión
cadena_base_datos = "postgresql+psycopg2://postgres:1234@localhost:5432/paises"
