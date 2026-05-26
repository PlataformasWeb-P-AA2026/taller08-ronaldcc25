import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEFAULT_SQLITE_URL = "sqlite:///paises.db"


def resolve_database_url(database_url=None):
    return database_url or os.getenv("DATABASE_URL") or DEFAULT_SQLITE_URL


def get_engine(database_url=None):
    url = resolve_database_url(database_url)
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, future=True, connect_args=connect_args)


def get_session_factory(database_url=None):
    engine = get_engine(database_url)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
