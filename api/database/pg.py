import os
from contextlib import contextmanager

from dotenv import load_dotenv
from cryptography.fernet import Fernet
import psycopg2

load_dotenv()

def decrypt_pswd() -> str:
    fern =  Fernet(os.getenv("POSTGRESQL_PSWD_KEY"))
    return fern.decrypt(
        os.getenv("POSTGRESQL_ENCR_PSWD").encode("utf-8")
    ).decode("utf-8")


@contextmanager
def pg_connect():
    conn = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("POSTGRESQL_USER"),
        password=decrypt_pswd(),
        host=os.getenv("POSTGRESQL_HOST"),
        port=os.getenv("POSTGRESQL_PORT")
    )
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def use_cursor(conn: psycopg2.extensions.connection):
    cur = conn.cursor()
    try: 
        yield cur
    finally:
        cur.close()