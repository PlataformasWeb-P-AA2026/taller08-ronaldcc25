from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Continente(Base):
    __tablename__ = "continente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    paises = relationship("Pais", back_populates="continente")

    def __repr__(self):
        return "Continente: Nombre: %s" % (self.nombre)


class Pais(Base):
    __tablename__ = "pais"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    continente_id = Column(Integer, ForeignKey("continente.id"))

    continente = relationship("Continente", back_populates="paises")
    jugadores_nacidos = relationship(
        "Jugador",
        foreign_keys="[Jugador.pais_nacimiento_id]",
        back_populates="pais_nacimiento",
    )
    jugadores_donde_juegan = relationship(
        "Jugador",
        foreign_keys="[Jugador.pais_donde_juega_id]",
        back_populates="pais_donde_juega",
    )

    def __repr__(self):
        return "Pais: Nombre: %s, Continente: %s" % (
            self.nombre,
            self.continente.nombre,
        )


class Jugador(Base):
    __tablename__ = "jugador"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    posicion = Column(String(100))
    edad = Column(Integer)
    partidos_seleccion = Column(Integer)
    goles_seleccion = Column(Integer)
    pais_nacimiento_id = Column(Integer, ForeignKey("pais.id"))
    pais_donde_juega_id = Column(Integer, ForeignKey("pais.id"))

    pais_nacimiento = relationship(
        "Pais", foreign_keys=[pais_nacimiento_id], back_populates="jugadores_nacidos"
    )
    pais_donde_juega = relationship(
        "Pais",
        foreign_keys=[pais_donde_juega_id],
        back_populates="jugadores_donde_juegan",
    )

    def __repr__(self):
        return (
            "Jugador: Nombre: %s, Posicion: %s, Edad: %d, Partidos en Seleccion: %d, Goles en Seleccion: %d, Pais de nacimiento: %s, Pais donde juega: %s"
            % (
                self.nombre,
                self.posicion,
                self.edad,
                self.partidos_seleccion,
                self.goles_seleccion,
                self.pais_nacimiento.nombre,
                self.pais_donde_juega.nombre,
            )
        )


Base.metadata.create_all(engine)
