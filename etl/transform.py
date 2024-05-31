from typing import List

import pandas as pd

from etl.etl_config import (
    DATA_PATH,
    TRANS_PATH,
    POSITIONS, 
    YEAR_RANGE, 
    FILE_IDS,
    DROP_COLS,
    DROP_COL_IDX,
    TRANS_PROCS,
    HEADER
)


def get_file_names(year: int, position: str) -> List[str]:
    return [
        f"{DATA_PATH}{year}_{position}_{file_id}.csv"
        for file_id in FILE_IDS
    ]


def drop_df_cols(df: pd.DataFrame, cols: List[int]) -> pd.DataFrame:
    return df.drop(
        df.columns[cols], axis=1
    )


def transform_file(df: pd.DataFrame, idx: int) -> pd.DataFrame:
    for trans_proc in TRANS_PROCS[idx]:
        if trans_proc == DROP_COL_IDX:
            df = drop_df_cols(df, DROP_COLS[idx]) 

    return df


def add_cols(df: pd.DataFrame, new_cols: List[pd.DataFrame]) -> pd.DataFrame:
    for col in new_cols:
        df = pd.concat([df, col], axis=1)
    return df


def transform_files(year: int, position: str) -> pd.DataFrame:
    file_names = get_file_names(year, position)
    trans_files = [
        transform_file(pd.read_csv(file_name, header=None), idx)
        for idx, file_name in enumerate(file_names)
    ]
    df = pd.concat(trans_files, axis=1)
    df = add_cols(
        df,
        [
            pd.DataFrame([position for _ in range(df.shape[0])], index=None),
            pd.DataFrame([year for _ in range(df.shape[0])], index=None)
        ]
    )
    return df


def merge_by_position(year: int) -> pd.DataFrame:
    dfs = [
        transform_files(year, position)
        for position in POSITIONS
    ]
    return pd.concat(dfs, axis=0)


def merge_all():
    dfs = [
        merge_by_position(year)
        for year in YEAR_RANGE
    ]
    df = pd.concat(dfs, axis=0)
    df.to_csv(
        f"{TRANS_PATH}transformed.csv",
        header=HEADER,
        sep=',',
        index=False
    )


def transform():
    try:
        merge_all()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    transform()
