from django.db import models
from django.utils.timezone import now

# Create your models here.
class account(models.Model):
    id_account = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    email = models.EmailField(unique=True)
    class Meta:
        managed = False
        db_table = 'account'

class item(models.Model):
    id_item = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=16)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    id_item_type = models.ForeignKey('item_type', models.DO_NOTHING, db_column='id_item_type')
    id_item_possessed = models.ForeignKey('item_possessed', models.DO_NOTHING, db_column='id_item_possessed')

    class Meta:
        managed = False
        db_table = 'item'


class item_possessed(models.Model):
    id_item_possessed = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    id_save = models.ForeignKey('save', models.DO_NOTHING, db_column='id_save')

    class Meta:
        managed = False
        db_table = 'item_possessed'


class item_type(models.Model):
    id_item_type = models.CharField(primary_key=True, max_length=16)
    is_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'item_type'


class map(models.Model):
    id_map = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'map'


class save(models.Model):
    id_save = models.AutoField(primary_key=True)
    pos_y = models.DecimalField(max_digits=10, decimal_places=2)
    pox_x = models.DecimalField(max_digits=10, decimal_places=2)
    health = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id_account = models.ForeignKey(account, models.DO_NOTHING, db_column='id_account')
    id_map = models.ForeignKey(map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'save'
