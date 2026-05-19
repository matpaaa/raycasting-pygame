from app.features.item import *
from app.api.game_api import *

def recover_item(id_save: int, id_item: int, id_sprite: int):
    res = GameApi.recover_item({
        'id_save': id_save,
        'id_item': id_item,
        'id_sprite': id_sprite
    })
    return res

def drop_item(id_save: int, id_item: int, pos_x: float, pos_y: float):
    print(id_save, id_item, pos_x, pos_y)
    GameApi.drop_item({
        'id_save': id_save,
        'id_item': id_item,
        'pos_x': pos_x,
        'pos_y': pos_y
    })