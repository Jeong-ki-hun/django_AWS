from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
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


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
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


class MusinsaTable(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    riview = models.CharField(max_length=255, blank=True, null=True)
    wishlist = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'musinsa_table'


class ObList(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ob_list'


class Question(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ob_question'


class ShopList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    status = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_list'

class SeoulTable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    x = models.CharField(max_length=255, blank=True, null=True)
    y = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_table'

class RestTable(models.Model):
    label =  models.CharField(max_length=255, blank=True, null=True)
    food_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    count = models.CharField(max_length=255, blank=True, null=True)


class CctvTable(models.Model):
    label =  models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    count = models.CharField(max_length=255, blank=True, null=True)


class streetTable(models.Model):
    address = models.CharField(max_length=255,blank=True, null=True)
    count = models.CharField(max_length=255, blank=True, null=True)
    time =  models.CharField(max_length=255, blank=True, null=True)

class ObResttable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField()
    food_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.TextField()
    status = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ob_resttable'