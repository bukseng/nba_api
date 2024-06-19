import os
from contextlib import contextmanager

from dotenv import load_dotenv
from cryptography.fernet import Fernet
import psycopg2
import psycopg2.extras as psyext
import pandas as pd

from etl_config import (
    TRANS_PATH,
    INSERT_PG_STATS,
    INSERT_PG_PLAYERS
)

def decrypt_pswd():
    fern =  Fernet(os.getenv("POSTGRESQL_PSWD_KEY"))
    return fern.decrypt(
        os.getenv("POSTGRESQL_ENCR_PSWD").encode("utf-8")
    ).decode("utf-8")


def connect_to_db():
    conn = psycopg2.connect(
        database=os.getenv("POSTGRESQL_DB_NAME"),
        user=os.getenv("POSTGRESQL_USER"),
        password=decrypt_pswd(),
        host=os.getenv("POSTGRESQL_HOST"),
        port=os.getenv("POSTGRESQL_PORT")
    )
    return conn


@contextmanager
def use_cursor(conn):
    cur = conn.cursor()
    try: 
        yield cur
    finally:
        cur.close()


def load_batch(conn, df, query):
    with use_cursor(conn) as cur:
        psyext.execute_batch(cur, query, df.values)

    conn.commit()


def load_stats(conn, df):
    stats_df = df.drop(df.columns[1], axis=1)
    stats_df.insert(
        0, 
        column='uid', 
        value=stats_df[['Year', 'id']].astype(str).agg('_'.join, axis=1)
    )
    load_batch(conn, stats_df, INSERT_PG_STATS)
 

def load_players(conn, df):
    players_df = df[['id', 'Player']].drop_duplicates()
    load_batch(conn, players_df, INSERT_PG_PLAYERS)

if __name__ == "__main__":
    try:
        load_dotenv()
        conn = connect_to_db()
        df = pd.read_csv(TRANS_PATH, index_col=False)
        load_stats(conn, df)
        load_players(conn, df) 
    except Exception as e:
        print(str(e))
    finally:
        conn.close()