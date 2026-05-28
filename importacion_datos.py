from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from creacion_tablas import Continente, Jugador, Pais

# Diccionario de mapeo que armamos previamente
mapeo_continentes = {
    "Ecuador": "América",
    "Japón": "Asia",
    "Alemania": "Europa",
    "España": "Europa",
    "Portugal": "Europa",
    "Marruecos": "África",
    "Brasil": "América",
    "Francia": "Europa",
    "Estados Unidos": "América",
    "Senegal": "África",
    "Inglaterra": "Europa",
    "México": "América",
    "Argentina": "América",
    "Nigeria": "África",
    "Australia": "Oceanía",
}

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ojo aquí con la ruta de tu archivo, ajústala si es necesario
with open("data/jugadores_futbol.csv", "r", encoding="utf-8") as f:
    lineas = f.readlines()

dic_continentes = {}
dic_paises = {}

# Usamos lineas[1:] para saltarnos la primera fila (los encabezados)
for linea in lineas[1:]:
    linea = linea.strip()
    if not linea:
        continue

    # 1. Extraemos los datos separados por coma
    datos = linea.split(",")
    nombre_jugador = datos[0].strip()
    pais_nac = datos[1].strip()
    pais_juego = datos[2].strip()
    posicion = datos[3].strip()
    edad = int(datos[4].strip())
    partidos = int(datos[5].strip())
    goles = int(datos[6].strip())

    # 2. Gestionar el Continente y País de nacimiento
    continente_nac_nombre = mapeo_continentes.get(pais_nac)

    # Validamos y creamos el continente de nacimiento si no existe
    if continente_nac_nombre not in dic_continentes:
        cont_nac = Continente(nombre=continente_nac_nombre)
        session.add(cont_nac)
        dic_continentes[continente_nac_nombre] = cont_nac

    # Validamos y creamos el país de nacimiento si no existe
    if pais_nac not in dic_paises:
        p_nac = Pais(nombre=pais_nac, continente=dic_continentes[continente_nac_nombre])
        session.add(p_nac)
        dic_paises[pais_nac] = p_nac

    # 3. Gestionar el Continente y País donde juega
    continente_juego_nombre = mapeo_continentes.get(pais_juego)

    if continente_juego_nombre not in dic_continentes:
        cont_juego = Continente(nombre=continente_juego_nombre)
        session.add(cont_juego)
        dic_continentes[continente_juego_nombre] = cont_juego

    if pais_juego not in dic_paises:
        p_juego = Pais(
            nombre=pais_juego, continente=dic_continentes[continente_juego_nombre]
        )
        session.add(p_juego)
        dic_paises[pais_juego] = p_juego

    # 4. Crear al Jugador y relacionarlo con los objetos del diccionario
    jugador = Jugador(
        nombre=nombre_jugador,
        posicion=posicion,
        edad=edad,
        partidos_seleccion=partidos,
        goles_seleccion=goles,
        pais_nacimiento=dic_paises[pais_nac],
        pais_donde_juega=dic_paises[pais_juego],
    )
    session.add(jugador)

# 5. Finalmente, mandamos todo a la base de datos
session.commit()
print("Datos importados correctamente")
