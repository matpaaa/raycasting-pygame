from django.db import models
from django.utils.timezone import now

# Create your models here.
class account(models.Model):
    id_account = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=16)
    password = models.CharField(max_length=180)
    created_at = models.DateTimeField(default=now)
    email = models.CharField(unique=True, max_length=320)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'account'


class item(models.Model):
    id_item = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=16)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_item_type = models.ForeignKey('item_type', models.DO_NOTHING, db_column='id_item_type')

    class Meta:
        managed = False
        db_table = 'item'


class ItemPossessed(models.Model):
    id_item_possessed = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    id_item = models.ForeignKey(item, models.DO_NOTHING, db_column='id_item')
    id_player = models.ForeignKey('player', models.DO_NOTHING, db_column='id_player')

    class Meta:
        managed = False
        db_table = 'item_possessed'


class item_secret_possessed(models.Model):
    id_item_secret_possessed = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    id_item = models.ForeignKey(item, models.DO_NOTHING, db_column='id_item')
    id_save = models.ForeignKey('save', models.DO_NOTHING, db_column='id_save', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_secret_possessed'


class item_type(models.Model):
    id_item_type = models.CharField(primary_key=True, max_length=16)

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


class player(models.Model):
    id_player = models.AutoField(primary_key=True)
    health = models.SmallIntegerField()
    energy = models.IntegerField()
    pos_x = models.DecimalField(max_digits=10, decimal_places=2)
    pos_y = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=16)
    is_owner = models.BooleanField()
    id_account = models.ForeignKey(account, models.DO_NOTHING, db_column='id_account')
    id_save = models.ForeignKey('save', models.DO_NOTHING, db_column='id_save')

    class Meta:
        managed = False
        db_table = 'player'


class puzzle(models.Model):
    id_puzzle = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    id_sprite_door_type = models.ForeignKey('sprite_door_type', models.DO_NOTHING, db_column='id_sprite_door_type')

    class Meta:
        managed = False
        db_table = 'puzzle'


class save(models.Model):
    id_save = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    duration = models.IntegerField()
    is_win = models.BooleanField()
    is_failed = models.BooleanField()
    online_code = models.CharField(max_length=6, blank=True, null=True)
    id_map = models.ForeignKey(map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'save'


class sprite(models.Model):
    id_sprite = models.IntegerField(primary_key=True)
    pos_x = models.DecimalField(max_digits=10, decimal_places=2)
    pos_y = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'sprite'


class sprite_door(models.Model):
    id_sprite = models.OneToOneField(sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    id_sprite_door_type = models.ForeignKey('sprite_door_type', models.DO_NOTHING, db_column='id_sprite_door_type')
    id_map = models.ForeignKey(map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'sprite_door'


class sprite_door_type(models.Model):
    id_sprite_door_type = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'sprite_door_type'


class sprite_enemy(models.Model):
    id_sprite = models.OneToOneField(sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    health = models.IntegerField()
    damage = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sprite_enemy'


class sprite_item(models.Model):
    id_sprite = models.OneToOneField(sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    created_at = models.DateTimeField()
    id_item = models.ForeignKey(item, models.DO_NOTHING, db_column='id_item')

    class Meta:
        managed = False
        db_table = 'sprite_item'


class to_finish(models.Model):
    pk = models.CompositePrimaryKey('id_save', 'id_puzzle')
    id_save = models.ForeignKey(save, models.DO_NOTHING, db_column='id_save')
    id_puzzle = models.ForeignKey(puzzle, models.DO_NOTHING, db_column='id_puzzle')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'to_finish'


class to_open(models.Model):
    pk = models.CompositePrimaryKey('id_save', 'id_sprite')
    id_sprite = models.ForeignKey(sprite_door, models.DO_NOTHING, db_column='id_sprite')
    id_save = models.ForeignKey(save, models.DO_NOTHING, db_column='id_save')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'to_open'