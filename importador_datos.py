import csv
from pathlib import Path

from sqlalchemy.orm import Session

from base_datos import get_engine
from modelos import Base, Continente, Jugador, Pais

PAIS_A_CONTINENTE = {
    "Alemania": "Europa",
    "Argentina": "América del Sur",
    "Australia": "Oceanía",
    "Brasil": "América del Sur",
    "Ecuador": "América del Sur",
    "España": "Europa",
    "Estados Unidos": "América del Norte",
    "Francia": "Europa",
    "Inglaterra": "Europa",
    "Japón": "Asia",
    "Marruecos": "África",
    "México": "América del Norte",
    "Nigeria": "África",
    "Portugal": "Europa",
    "Senegal": "África",
}


class ImportadorDatos:
    def __init__(self, database_url, csv_path="data/jugadores_futbol.csv"):
        self.database_url = database_url
        self.csv_path = csv_path

    def get_or_create_continente(self, session, nombre, cache):
        if nombre in cache:
            return cache[nombre]
        continente = session.query(Continente).filter_by(nombre=nombre).one_or_none()
        if continente is None:
            continente = Continente(nombre=nombre)
            session.add(continente)
            session.flush()
        cache[nombre] = continente
        return continente

    def get_or_create_pais(self, session, nombre, cache_continentes, cache_paises):
        if nombre in cache_paises:
            return cache_paises[nombre]
        continente_nombre = PAIS_A_CONTINENTE.get(nombre)
        if continente_nombre is None:
            raise ValueError(f"No existe continente configurado para el país: {nombre}")
        continente = self.get_or_create_continente(
            session, continente_nombre, cache_continentes
        )
        pais = session.query(Pais).filter_by(nombre=nombre).one_or_none()
        if pais is None:
            pais = Pais(nombre=nombre, continente_id=continente.id)
            session.add(pais)
            session.flush()
        cache_paises[nombre] = pais
        return pais

    def preparar_tablas(self, engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def importar(self):
        engine = get_engine(self.database_url)
        self.preparar_tablas(engine)

        with Session(engine) as session:
            cache_continentes = {}
            cache_paises = {}

            with Path(self.csv_path).open(encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pais_nacimiento = self.get_or_create_pais(
                        session, row["pais_nacimiento"], cache_continentes, cache_paises
                    )
                    pais_donde_juega = self.get_or_create_pais(
                        session,
                        row["pais_donde_juega"],
                        cache_continentes,
                        cache_paises,
                    )

                    jugador = Jugador(
                        nombre_jugador=row["nombre_jugador"],
                        pais_nacimiento_id=pais_nacimiento.id,
                        pais_donde_juega_id=pais_donde_juega.id,
                        posicion=row["posicion"],
                        edad=int(row["edad"]),
                        numero_partidos_seleccion=int(row["numero_partidos_seleccion"]),
                        goles_seleccion=int(row["goles_seleccion"]),
                    )
                    session.add(jugador)

            session.commit()

            total_continentes = session.query(Continente).count()
            total_paises = session.query(Pais).count()
            total_jugadores = session.query(Jugador).count()

        return total_continentes, total_paises, total_jugadores
