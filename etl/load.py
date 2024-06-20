from psycopg2.extensions import connection
import psycopg2.extras as psyext
import pandas as pd

from api.database.pg import (
    use_cursor,
    pg_connect
)
from api.database.mongo import get_mongo_coll

from etl_config import (
    TRANS_PATH,
    INSERT_PG_STATS,
    INSERT_PG_PLAYERS,
    HEADER_NAMES
)


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


def mongo_load(df: pd.DataFrame):
    stats_coll = get_mongo_coll("stats")
    mongo_df =  insert_id(df)
    stats_coll.insert_many(mongo_df.to_dict(orient="records"))


def load():
    df = pd.read_csv(TRANS_PATH, index_col=False)
    df.rename(columns=lambda x: HEADER_NAMES[x], inplace=True)
    with pg_connect() as conn:
        load_stats(conn, df)
        load_players(conn, df)

    mongo_load(df)
