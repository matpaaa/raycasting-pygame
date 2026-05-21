from app.model.save_model import *
from app.api.save_api import *
from app.store.store import InvalidStoreOptions
from app.sprites.enemie_sprite import *
from app.sprites.object_sprite import *
from app.sprites.door_sprite import *
from app.sprites.final_door_sprite import *
from app.features.item import *

class SaveStore:
    save_loaded: None | SaveLoadedModel
    saves: None | SaveHomeModel
    
    def __init__(self):
        self.save_loaded = None
        self.saves = None
    
    def invalid_saves(self, options=None):
        if options is None:
            options = {"refetch": None}
            
        self.saves = None
            
        if options.get("refetch"):
            self.hydrate_saves()
            
    def invalid_save_loaded(self, options=None):
        if options is None:
            options = {"refetch": None}

        self.save_loaded = None

        if options.get("refetch"):
            self.hydrate_save_loaded()
    
    def hydrate_saves(self):
        if self.saves is None:
            self.saves = SaveApi.get_saves()
            
    def hydrate_save_loaded(self, save_id: int):
        if self.save_loaded is None:
            self.save_loaded = SaveApi.get_save(save_id)

            original_doors   = self.save_loaded['sprite_doors']
            original_items   = self.save_loaded['sprite_items']
            original_enemies = self.save_loaded['sprite_enemies']

            self.save_loaded['sprite_items']   = []
            self.save_loaded['sprite_enemies'] = []
            self.save_loaded['sprite_doors']   = []

            for sprite in original_doors:
                is_open = [door for door in self.save_loaded['open'] if door['id_sprite'] == sprite['id_sprite']]
                if sprite['id_sprite_door_type'] == 'CODE':
                    self.save_loaded['sprite_doors'].append(FinalDoorSprite(float(sprite['pos_x']), float(sprite['pos_y']), sprite['image'], sprite['id_sprite'], is_open))
                else:
                    self.save_loaded['sprite_doors'].append(DoorSprite(float(sprite['pos_x']), float(sprite['pos_y']), sprite['image'], sprite['id_sprite'], is_open))

            for sprite in original_items:
                item = sprite['item']
                value = None
                if item['id_item'] == 'CODE':
                    value = sprite['value']
                else:
                    value = float(item['value']) if item['value'] is not None else None
                    
                itemClass = Item(item['id_item'], item['name'], value, item['id_item_type'], item['image'])
                self.save_loaded['sprite_items'].append(ObjectSprite(float(sprite['pos_x']), float(sprite['pos_y']), itemClass, sprite['id_sprite']))

            for sprite in original_enemies:
                self.save_loaded['sprite_enemies'].append(EnemieSprite(float(sprite['pos_x']), float(sprite['pos_y']), sprite['image'], sprite['health'], sprite['damage'], sprite['id_sprite']))