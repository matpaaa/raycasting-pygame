from app.features.item import *
from app.api.game_api import *
import app._utils.global_var as global_var

def recover_item(id_save: int, id_item: int, id_sprite: int):
    res = GameApi.recover_item({
        'id_save': id_save,
        'id_item': id_item,
        'id_sprite': id_sprite
    })
    return res

def drop_item(id_save: int, id_item: int, pos_x: float, pos_y: float):
    GameApi.drop_item({
        'id_save': id_save,
        'id_item': id_item,
        'pos_x': pos_x,
        'pos_y': pos_y
    })
    
def open_door(id_save: int, id_sprite: int):
    GameApi.open_door({
        'id_save': id_save,
        'id_sprite': id_sprite
    })
    
def game_win(id_save: int):
    GameApi.win({
        'id_save': id_save
    })
    global_var.save_store.invalid_saves({'refetch': True})
    
def game_failed(id_save: int):
    GameApi.failed({
        'id_save': id_save
    })
    global_var.save_store.invalid_saves({'refetch': True})