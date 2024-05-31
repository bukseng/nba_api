DATA_PATH = 'data/'
TRANS_PATH = 'transformed/'
YEAR_RANGE = range(1947, 2024)
POSITIONS = ('C', 'PF', 'SF', 'SG', 'PG')
FILE_IDS = ('Totals', 'Averages', 'Advanced_Stats')
DROP_COLS = ([1], [0, 1, 2, 3], [0, 1, 2])
DROP_COL_IDX = 0
TRANS_PROCS = ((DROP_COL_IDX,), (DROP_COL_IDX,), (DROP_COL_IDX,))
HEADER = [
    "id","Player","Team","Games Played","Total Minutes","Total Points","Total FG Made","Total FG Attempt", "Total FG Perc",
    "Total 3P Made","Total 3P Attempt","Total 3P Perc", "Total FT Made","Total FT Attempt", "Total FT Perc","Total Off Reb",
    "Total Def Reb", "Total Reb","Total Ast","Total Stl","Total Blk","Total TOV","Total PF",
    "Mins PG","Points PG","FG Made PG","FG Atttempt PG","FG Perc PG","3P Made PG","3P Attempt PG","3P Perc PG","FT Made PG",
    "FT Attempt PG","FT Perc PG","Off Reb PG","Def Reb PG","Reb PG","Ast PG","Stl PG","Blk PG","TOV PG","PF PG",
    "True Shooting Perc","Effective FG Perc","Total Shooting Perc","Off Reb Perc","Def Reb Perc","Total Reb Perc",
    "Ast Perc","TOV Perc","Stl Perc","Blk Perc","Usage Rate Perc","Pure Point Rtg","Points Per Shot","Off Rtg","Def Rtg",
    "Efficiency Diff","Floor Impact Counter","Player Efficiency Rating", "Position", "Year"
]
