from importador_datos import ImportadorDatos

DATABASE_URL = "sqlite:///paises.db"
# DATABASE_URL = "mysql+pymysql://root:TU_CLAVE@localhost/paises"
# DATABASE_URL = "mysql+pymysql://usuario:TU_CLAVE@localhost/paises"

CSV_PATH = "data/jugadores_futbol.csv"


def main():
    importador = ImportadorDatos(database_url=DATABASE_URL, csv_path=CSV_PATH)
    importador.importar()


if __name__ == "__main__":
    main()
