from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Attractions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    queue = models.IntegerField(blank=True, null=True)
    maintenance = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    wait_time = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'attractions'

    @classmethod
    def filter_attractions(cls, include_restaurants, open_only, sort_by):
        attractions = cls.objects.all()
        if include_restaurants:
            attractions = attractions.prefetch_related('restaurant_set')
        if open_only:
            attractions = attractions.filter(open=True)
        if sort_by:
            if sort_by == 'wait_time':
                attractions = attractions.order_by('wait_time')
            elif sort_by == 'queue':
                attractions = attractions.order_by('queue')
            elif sort_by == 'capacity':
                attractions = attractions.order_by('capacity')
        return attractions


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


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


class Park(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    date = models.DateField(null=True, blank=True)
    num_workers = models.IntegerField(blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    weather = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'park'


class Restaurants(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'restaurants'

class Place(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    capacity = models.IntegerField()
    open = models.BooleanField()

class Attraction(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

