from django.db import models
from django.utils.timezone import now

# Create your models here.
class Account(models.Model):
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


class Item(models.Model):
    id_item = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=16)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_item_type = models.ForeignKey('ItemType', models.DO_NOTHING, db_column='id_item_type')
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'item'


class ItemPossessed(models.Model):
    id_item_possessed = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now())
    id_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='id_item')
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')

    class Meta:
        managed = False
        db_table = 'item_possessed'


class ItemSecretPossessed(models.Model):
    id_item_secret_possessed = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now())
    id_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='id_item')
    id_save = models.ForeignKey('Save', models.DO_NOTHING, db_column='id_save', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_secret_possessed'


class ItemType(models.Model):
    id_item_type = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'item_type'


class Map(models.Model):
    id_map = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    default_pos_x = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    default_pos_y = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    default_rotation = models.IntegerField(default=90)
    created_at = models.DateTimeField(default=now())

    class Meta:
        managed = False
        db_table = 'map'


class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    health = models.SmallIntegerField(default=160)
    energy = models.IntegerField(default=1200)
    pos_x = models.DecimalField(max_digits=10, decimal_places=2)
    pos_y = models.DecimalField(max_digits=10, decimal_places=2)
    rotation = models.IntegerField(default=90)
    created_at = models.DateTimeField(default=now())
    is_owner = models.BooleanField(default=False)
    id_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='id_account')
    id_save = models.ForeignKey('Save', models.DO_NOTHING, db_column='id_save')

    class Meta:
        managed = False
        db_table = 'player'


class Puzzle(models.Model):
    id_puzzle = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=now())
    id_map = models.ForeignKey(Map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'puzzle'


class Save(models.Model):
    id_save = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())
    duration = models.IntegerField()
    is_win = models.BooleanField()
    is_failed = models.BooleanField()
    online_code = models.CharField(max_length=6, blank=True, null=True)
    id_map = models.ForeignKey(Map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'save'


class Sprite(models.Model):
    id_sprite = models.AutoField(primary_key=True)
    pos_x = models.DecimalField(max_digits=10, decimal_places=2)
    pos_y = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sprite'


class SpriteDoor(models.Model):
    id_sprite = models.OneToOneField(Sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    id_sprite_door_type = models.ForeignKey('SpriteDoorType', models.DO_NOTHING, db_column='id_sprite_door_type')
    id_map = models.ForeignKey(Map, models.DO_NOTHING, db_column='id_map')

    class Meta:
        managed = False
        db_table = 'sprite_door'


class SpriteDoorType(models.Model):
    id_sprite_door_type = models.CharField(primary_key=True, max_length=16)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'sprite_door_type'


class SpriteEnemy(models.Model):
    id_sprite = models.OneToOneField(Sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    id_save = models.OneToOneField(Save, models.DO_NOTHING, db_column='id_save')
    health = models.IntegerField()
    damage = models.IntegerField()
    created_at = models.DateTimeField(default=now())
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'sprite_enemy'


class SpriteItem(models.Model):
    id_sprite = models.OneToOneField(Sprite, models.DO_NOTHING, db_column='id_sprite', primary_key=True)
    id_save = models.OneToOneField(Save, models.DO_NOTHING, db_column='id_save')
    created_at = models.DateTimeField(default=now())
    id_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='id_item')
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,default=None)

    class Meta:
        managed = False
        db_table = 'sprite_item'


class ToFinish(models.Model):
    pk = models.CompositePrimaryKey('id_save', 'id_puzzle')
    id_save = models.ForeignKey(Save, models.DO_NOTHING, db_column='id_save')
    id_puzzle = models.ForeignKey(Puzzle, models.DO_NOTHING, db_column='id_puzzle')
    created_at = models.DateTimeField(default=now())

    class Meta:
        managed = False
        db_table = 'to_finish'


class ToOpen(models.Model):
    pk = models.CompositePrimaryKey('id_save', 'id_sprite')
    id_sprite = models.ForeignKey(SpriteDoor, models.DO_NOTHING, db_column='id_sprite')
    id_save = models.ForeignKey(Save, models.DO_NOTHING, db_column='id_save')
    created_at = models.DateTimeField(default=now())

    class Meta:
        managed = False
        db_table = 'to_open'