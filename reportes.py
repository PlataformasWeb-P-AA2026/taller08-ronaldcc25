import pandas as pd
from sqlalchemy import func, select
from sqlalchemy.orm import aliased

from modelos import Continente, Jugador, Pais

pais_juega_alias = aliased(Pais)


def players_dataframe(session):
    rows = (
        session.execute(
            select(
                Jugador.nombre_jugador.label("nombre_jugador"),
                Pais.nombre.label("pais_nacimiento"),
                pais_juega_alias.nombre.label("pais_donde_juega"),
                Jugador.posicion.label("posicion"),
                Jugador.edad.label("edad"),
                Jugador.numero_partidos_seleccion.label("numero_partidos_seleccion"),
                Jugador.goles_seleccion.label("goles_seleccion"),
                Continente.nombre.label("continente"),
            )
            .join(Pais, Jugador.pais_nacimiento_id == Pais.id)
            .join(Continente, Pais.continente_id == Continente.id)
            .join(pais_juega_alias, Jugador.pais_donde_juega_id == pais_juega_alias.id)
            .order_by(Jugador.nombre_jugador)
        )
        .mappings()
        .all()
    )
    return pd.DataFrame(rows)


def continent_summary_dataframe(session):
    rows = (
        session.execute(
            select(
                Continente.nombre.label("continente"),
                func.count(Jugador.id).label("numero_jugadores"),
                func.sum(Jugador.goles_seleccion).label("numero_goles"),
            )
            .join(Pais, Pais.continente_id == Continente.id)
            .join(Jugador, Jugador.pais_nacimiento_id == Pais.id)
            .group_by(Continente.nombre)
            .order_by(Continente.nombre)
        )
        .mappings()
        .all()
    )
    return pd.DataFrame(rows)


def country_summary_dataframe(session):
    rows = (
        session.execute(
            select(
                Pais.nombre.label("pais"),
                func.count(Jugador.id).label("numero_jugadores"),
                func.sum(Jugador.goles_seleccion).label("numero_goles"),
            )
            .join(Jugador, Jugador.pais_nacimiento_id == Pais.id)
            .group_by(Pais.nombre)
            .order_by(Pais.nombre)
        )
        .mappings()
        .all()
    )
    return pd.DataFrame(rows)
