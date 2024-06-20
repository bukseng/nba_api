from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoApiStats(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    player_id = models.IntegerField()
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
        db_table = 'django_api_stats'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'players'


class Stats(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    player_id = models.IntegerField()
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
