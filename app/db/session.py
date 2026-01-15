from typing import Generator

import psycopg
from app.core.config import get_settings


def get_db() -> Generator[psycopg.Connection, None, None]:
    settings = get_settings()
    conn = psycopg.connect(settings.DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()