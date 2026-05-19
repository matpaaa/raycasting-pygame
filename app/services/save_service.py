from app.mock.map_mocked import *
from app.sprites.object_sprite import *
from app.sprites.enemie_sprite import *
from app.api.save_api import *
import app._utils.global_var as global_var
from app.features.user import *


def create_save():
    data = {
        'sprite_items': [],
        'sprite_enemies': []
    }
    
    for sprite in [s for s in MAP_SPRITES_MOCKED if isinstance(s, ObjectSprite)]:
        data['sprite_items'].append({
            'pos_x': sprite._x,
            'pos_y': sprite._y,
            'image': sprite.image,
            'id_item': sprite.item.id_item
        })
        
    for sprite in [s for s in MAP_SPRITES_MOCKED if isinstance(s, EnemieSprite)]:
        data['sprite_enemies'].append({
            'health': sprite.pv,
            'damage': sprite.damage,
            'pos_x': sprite._x,
            'pos_y': sprite._y,
            'image': sprite.image,
        })
    
    res = SaveApi.create_save(data)
    if res.status_code == 200:
        res_data = res.json()
        global_var.save_store.invalid_save_loaded()
        global_var.save_store.hydrate_save_loaded(res_data['id_save'])
        global_var.navigatePage('game')
    else:
        Exception('Impossible de créer une nouvelle partie')
        
def load_save(save_id: int):
    global_var.navigatePage('loading')
    global_var.save_store.invalid_save_loaded()
    global_var.save_store.hydrate_save_loaded(save_id)
    global_var.navigatePage('game')
        
def save_user(user: User):
    data = {
        'health': user.health,
        'energy': user.battery,
        'pos_x': user.pos_x,
        'pos_y': user.pos_y,
        'rotation': user.rot
    }
    
    res = SaveApi.save_player(data)
    if res.status_code == 200:
        global_var.navigatePage('saves')
    else:
        Exception('Erreur durant la sauvegarde la partie')
        
def delete_save(id_save: int):
    res = SaveApi.delete_save({ 'id_save': id_save })
    if res.status_code == 200:
        global_var.save_store.invalid_saves({'refetch': True})