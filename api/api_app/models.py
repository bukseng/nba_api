from django.db import models


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'players'


class Stat(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.CharField(max_length=50)
    games_played = models.IntegerField()
    total_minutes = models.IntegerField()
    total_points = models.IntegerField()
    total_fg_made = models.IntegerField()
    total_fg_attempt = models.IntegerField()
    total_fg_perc = models.DecimalField(max_digits=5, decimal_places=2)
    total_3p_made = models.IntegerField()
    total_3p_attempt = models.IntegerField()
    total_3p_perc = models.DecimalField(max_digits=5, decimal_places=2)
    total_ft_made = models.IntegerField()
    total_ft_attempt = models.IntegerField()
    total_ft_perc = models.DecimalField(max_digits=5, decimal_places=2)
    total_off_reb = models.IntegerField()
    total_def_reb = models.IntegerField()
    total_reb = models.IntegerField()
    total_ast = models.IntegerField()
    total_stl = models.IntegerField()
    total_blk = models.IntegerField()
    total_tov = models.IntegerField()
    total_pf = models.IntegerField()
    mins_pg = models.DecimalField(max_digits=5, decimal_places=2)
    points_pg = models.DecimalField(max_digits=5, decimal_places=2)
    fg_made_pg = models.DecimalField(max_digits=5, decimal_places=2)
    fg_attempt_pg = models.DecimalField(max_digits=5, decimal_places=2)
    fg_perc_pg = models.DecimalField(max_digits=5, decimal_places=2)
    three_p_made_pg = models.DecimalField(max_digits=5, decimal_places=2)
    three_p_attempt_pg = models.DecimalField(max_digits=5, decimal_places=2)
    three_p_perc_pg = models.DecimalField(max_digits=5, decimal_places=2)
    ft_made_pg = models.DecimalField(max_digits=5, decimal_places=2)
    ft_attempt_pg = models.DecimalField(max_digits=5, decimal_places=2)
    ft_perc_pg = models.DecimalField(max_digits=5, decimal_places=2)
    off_reb_pg = models.DecimalField(max_digits=5, decimal_places=2)
    def_reb_pg = models.DecimalField(max_digits=5, decimal_places=2)
    reb_pg = models.DecimalField(max_digits=5, decimal_places=2)
    ast_pg = models.DecimalField(max_digits=5, decimal_places=2)
    stl_pg = models.DecimalField(max_digits=5, decimal_places=2)
    blk_pg = models.DecimalField(max_digits=5, decimal_places=2)
    tov_pg = models.DecimalField(max_digits=5, decimal_places=2)
    pf_pg = models.DecimalField(max_digits=5, decimal_places=2)
    true_shooting_perc = models.DecimalField(max_digits=5, decimal_places=2)
    effective_fg_perc = models.DecimalField(max_digits=5, decimal_places=2)
    total_shooting_perc = models.DecimalField(max_digits=5, decimal_places=2)
    off_reb_perc = models.DecimalField(max_digits=5, decimal_places=2)
    def_reb_perc = models.DecimalField(max_digits=5, decimal_places=2)
    total_reb_perc = models.DecimalField(max_digits=5, decimal_places=2)
    ast_perc = models.DecimalField(max_digits=5, decimal_places=2)
    tov_perc = models.DecimalField(max_digits=5, decimal_places=2)
    stl_perc = models.DecimalField(max_digits=5, decimal_places=2)
    blk_perc = models.DecimalField(max_digits=5, decimal_places=2)
    usage_rate_perc = models.DecimalField(max_digits=5, decimal_places=2)
    pure_point_rtg = models.DecimalField(max_digits=5, decimal_places=2)
    points_per_shot = models.DecimalField(max_digits=5, decimal_places=2)
    off_rtg = models.DecimalField(max_digits=5, decimal_places=2)
    def_rtg = models.DecimalField(max_digits=5, decimal_places=2)
    efficiency_diff = models.DecimalField(max_digits=5, decimal_places=2)
    floor_impact_counter = models.DecimalField(max_digits=7, decimal_places=2)
    player_efficiency_rating = models.DecimalField(max_digits=5, decimal_places=2)
    position = models.CharField(max_length=50)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stats'
