import argparse
from pathlib import Path

from sqlalchemy.orm import Session

from base_datos import get_engine, resolve_database_url
from reportes import (
    continent_summary_dataframe,
    country_summary_dataframe,
    players_dataframe,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="sqlite:///paises.db")
    parser.add_argument("--output-dir", default="evidencias/sqlite")
    args = parser.parse_args()

    database_url = resolve_database_url(args.db)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    engine = get_engine(database_url)

    with Session(engine) as session:
        detalle = players_dataframe(session)
        resumen_continente = continent_summary_dataframe(session)
        resumen_pais = country_summary_dataframe(session)

    detalle.to_csv(output_dir / "tabla_jugadores.csv", index=False)
    resumen_continente.to_csv(output_dir / "tabla_continentes.csv", index=False)
    resumen_pais.to_csv(output_dir / "tabla_paises.csv", index=False)

    resumen = [
        f"base_de_datos={database_url}",
        f"total_jugadores={len(detalle)}",
        f"total_continentes={len(resumen_continente)}",
        f"total_paises={len(resumen_pais)}",
    ]
    (output_dir / "resumen.txt").write_text("\n".join(resumen), encoding="utf-8")


if __name__ == "__main__":
    main()
