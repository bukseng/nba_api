import os
from contextlib import contextmanager

from dotenv import load_dotenv
from cryptography.fernet import Fernet
import psycopg2
import psycopg2.extras as psyext
from psycopg2.extensions import connection
import pymongo
import pandas as pd

from etl_config import (
    TRANS_PATH,
    INSERT_PG_STATS,
    INSERT_PG_PLAYERS,
    HEADER_NAMES
)


def decrypt_pswd() -> str:
    fern =  Fernet(os.getenv("POSTGRESQL_PSWD_KEY"))
    return fern.decrypt(
        os.getenv("POSTGRESQL_ENCR_PSWD").encode("utf-8")
    ).decode("utf-8")


@contextmanager
def connect_to_db():
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
def use_cursor(conn: connection):
    cur = conn.cursor()
    try: 
        yield cur
    finally:
        cur.close()


def load_batch(conn: connection, df: pd.DataFrame, query: str):
    with use_cursor(conn) as cur:
        psyext.execute_batch(cur, query, df.values)

    conn.commit()


def insert_id(df: pd.DataFrame) -> pd.DataFrame:
    df.insert(
        0, 
        column='_id', 
        value=df[['year', 'player_id']].astype(str).agg('_'.join, axis=1)
    )
    return df


def load_stats(conn: connection, df: pd.DataFrame):
    stats_df = df.drop(df.columns[1], axis=1)
    stats_df = insert_id(stats_df)
    load_batch(conn, stats_df, INSERT_PG_STATS)
 

def load_players(conn: connection, df: pd.DataFrame):
    players_df = df[['player_id', 'player_name']].drop_duplicates()
    load_batch(conn, players_df, INSERT_PG_PLAYERS)


def get_mongo_stats_coll() -> pymongo.collection.Collection:
    return pymongo.MongoClient(
        os.getenv("MONGODB_URI")
    )[os.getenv("DB_NAME")]["stats"]


def mongo_load(df: pd.DataFrame):
    stats_coll = get_mongo_stats_coll()
    mongo_df =  insert_id(df)
    stats_coll.insert_many(mongo_df.to_dict(orient="records"))


def load():
    load_dotenv()
    df = pd.read_csv(TRANS_PATH, index_col=False)
    df.rename(columns=lambda x: HEADER_NAMES[x], inplace=True)
    with connect_to_db() as conn:
        load_stats(conn, df)
        load_players(conn, df)

    mongo_load(df)
