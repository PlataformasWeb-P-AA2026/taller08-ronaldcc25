from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Continente(Base):
    __tablename__ = "continentes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    paises: Mapped[list["Pais"]] = relationship(back_populates="continente")


class Pais(Base):
    __tablename__ = "paises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    continente_id: Mapped[int] = mapped_column(ForeignKey("continentes.id"), nullable=False)

    continente: Mapped["Continente"] = relationship(back_populates="paises")
    jugadores_nacimiento: Mapped[list["Jugador"]] = relationship(
        foreign_keys="Jugador.pais_nacimiento_id",
        back_populates="pais_nacimiento",
    )
    jugadores_donde_juega: Mapped[list["Jugador"]] = relationship(
        foreign_keys="Jugador.pais_donde_juega_id",
        back_populates="pais_donde_juega",
    )


class Jugador(Base):
    __tablename__ = "jugadores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_jugador: Mapped[str] = mapped_column(String(200), nullable=False)
    pais_nacimiento_id: Mapped[int] = mapped_column(ForeignKey("paises.id"), nullable=False)
    pais_donde_juega_id: Mapped[int] = mapped_column(ForeignKey("paises.id"), nullable=False)
    posicion: Mapped[str] = mapped_column(String(100), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    numero_partidos_seleccion: Mapped[int] = mapped_column(Integer, nullable=False)
    goles_seleccion: Mapped[int] = mapped_column(Integer, nullable=False)

    pais_nacimiento: Mapped["Pais"] = relationship(
        foreign_keys=[pais_nacimiento_id],
        back_populates="jugadores_nacimiento",
    )
    pais_donde_juega: Mapped["Pais"] = relationship(
        foreign_keys=[pais_donde_juega_id],
        back_populates="jugadores_donde_juega",
    )
