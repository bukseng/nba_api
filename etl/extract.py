from typing import List
import time
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


from etl_config import (
    DATA_PATH,
    POSITIONS, 
    YEAR_RANGE, 
    FILE_IDS,
    ROOT_SITE,
    REQUEST_HEADER
)


def get_id(player_url: str) -> str:
    id_search = re.search(r'\/(\d+)$', player_url)
    return id_search.group(1)


def extract_values(table: Tag, stat_type: str) -> List[List[str]]:
    print(type(table))
    return [
        [get_id(cells[1].find('a')['href'])] + 
        [cell.text for cell in cells]
        if stat_type == 'Totals'
        else [cell.text for cell in cells]
        for row in table.find_all('tr')
        if (cells := [cell for cell in row.find_all('td')])
    ]


def extract_page(year: str, position: str, stat_type: str, page_no: int):
    url = f'{ROOT_SITE}/{year}/{stat_type}/All/player/{position}/asc/{page_no}/Regular_Season'
    page = requests.get(url, headers=REQUEST_HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('tbody')
    if not table:
        return None

    return extract_values(table, stat_type)


def extract_stats(year: str, position: str):
    for stat_type in FILE_IDS:
        page_no = 1
        output = f'{DATA_PATH}{year}_{position}_{stat_type}.csv'
        print(f'Exctracting {year}_{position}_{stat_type}...')
        all_data = []
        while True:
            data = extract_page(year, position, stat_type, page_no)
            if not data:
                time.sleep(2)
                break

            all_data += data

            time.sleep(5)
            page_no += 1

        pd.DataFrame(all_data).to_csv(output, header=False, index=False)


def extract():
    for year in YEAR_RANGE:
        for position in POSITIONS:
            extract_stats(year, position)
