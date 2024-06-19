DATA_PATH = "data/"
TRANS_PATH = "transformed/transformed.csv"
YEAR_RANGE = range(1947, 2025)
POSITIONS = ("C", "PF", "SF", "SG", "PG")
FILE_IDS = ("Totals", "Averages", "Advanced_Stats")
DROP_COLS = ([1], [0, 1, 2, 3], [0, 1, 2])
DROP_COL_IDX = 0
TRANS_PROCS = ((DROP_COL_IDX,), (DROP_COL_IDX,), (DROP_COL_IDX,))
HEADER = [
    "id","Player","Team","Games Played","Total Minutes","Total Points","Total FG Made","Total FG Attempt", "Total FG Perc",
    "Total 3P Made","Total 3P Attempt","Total 3P Perc", "Total FT Made","Total FT Attempt", "Total FT Perc","Total Off Reb",
    "Total Def Reb", "Total Reb","Total Ast","Total Stl","Total Blk","Total TOV","Total PF",
    "Mins PG","Points PG","FG Made PG","FG Attempt PG","FG Perc PG","3P Made PG","3P Attempt PG","3P Perc PG","FT Made PG",
    "FT Attempt PG","FT Perc PG","Off Reb PG","Def Reb PG","Reb PG","Ast PG","Stl PG","Blk PG","TOV PG","PF PG",
    "True Shooting Perc","Effective FG Perc","Total Shooting Perc","Off Reb Perc","Def Reb Perc","Total Reb Perc",
    "Ast Perc","TOV Perc","Stl Perc","Blk Perc","Usage Rate Perc","Pure Point Rtg","Points Per Shot","Off Rtg","Def Rtg",
    "Efficiency Diff","Floor Impact Counter","Player Efficiency Rating", "Position", "Year"
]
HEADER_ALIAS = [
    "player_id", "player_name", "team", "games_played", "total_minutes", "total_points", "total_fg_made", 
    "total_fg_attempt", "total_fg_perc", "total_3p_made", "total_3p_attempt", "total_3p_perc", 
    "total_ft_made", "total_ft_attempt", "total_ft_perc", "total_off_reb", "total_def_reb", "total_reb",
    "total_ast", "total_stl", "total_blk", "total_tov", "total_pf", "mins_pg", "points_pg", "fg_made_pg",
    "fg_attempt_pg", "fg_perc_pg", "three_p_made_pg", "three_p_attempt_pg", "three_p_perc_pg", 
    "ft_made_pg", "ft_attempt_pg", "ft_perc_pg", "off_reb_pg", "def_reb_pg", "reb_pg", "ast_pg", "stl_pg", 
    "blk_pg", "tov_pg", "pf_pg", "true_shooting_perc", "effective_fg_perc", "total_shooting_perc", 
    "off_reb_perc", "def_reb_perc", "total_reb_perc", "ast_perc", "tov_perc", "stl_perc", "blk_perc", 
    "usage_rate_perc", "pure_point_rtg", "points_per_shot", "off_rtg", "def_rtg", "efficiency_diff",
    "floor_impact_counter", "player_efficiency_rating", "position", "year"
]
PG_STATS_COLS = [
    "id", "player_id", "team", "games_played", "total_minutes", "total_points", "total_fg_made", 
    "total_fg_attempt", "total_fg_perc", "total_3p_made", "total_3p_attempt", "total_3p_perc", 
    "total_ft_made", "total_ft_attempt", "total_ft_perc", "total_off_reb", "total_def_reb", "total_reb",
    "total_ast", "total_stl", "total_blk", "total_tov", "total_pf", "mins_pg", "points_pg", "fg_made_pg",
    "fg_attempt_pg", "fg_perc_pg", "three_p_made_pg", "three_p_attempt_pg", "three_p_perc_pg", 
    "ft_made_pg", "ft_attempt_pg", "ft_perc_pg", "off_reb_pg", "def_reb_pg", "reb_pg", "ast_pg", "stl_pg", 
    "blk_pg", "tov_pg", "pf_pg", "true_shooting_perc", "effective_fg_perc", "total_shooting_perc", 
    "off_reb_perc", "def_reb_perc", "total_reb_perc", "ast_perc", "tov_perc", "stl_perc", "blk_perc", 
    "usage_rate_perc", "pure_point_rtg", "points_per_shot", "off_rtg", "def_rtg", "efficiency_diff",
    "floor_impact_counter", "player_efficiency_rating", "position", "year"
]
PG_STATS_VALS = f"VALUES ({','.join(['%s' for _ in PG_STATS_COLS])})"
INSERT_PG_STATS = f"INSERT INTO stats ({','.join(PG_STATS_COLS)}) {PG_STATS_VALS}"
INSERT_PG_PLAYERS = "INSERT INTO players (id, name) VALUES (%s, %s)"
ROOT_SITE = "https://basketball.realgm.com/nba/stats"
REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}
HEADER_NAMES = dict(zip(HEADER, HEADER_ALIAS))
