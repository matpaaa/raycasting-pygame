from typing import List, Dict
from app.sprites.sprite import *
from pygame import Surface
import pygame
from app.sprites.object_sprite import *
from app.features.item import *

class MapConfig:

    def __init__(self, map: List[List[int]], sprites: List[Sprite], textures_path: Dict[int, str], id_save: int):
        self._map = map
        self._sprites = sprites
        self._textures_path = textures_path
        self._textures = {}
        self._id_save = id_save

    def load_textures(self):
        for path_key in self._textures_path:
            path = self._textures_path[path_key]
            self._textures[path_key] = pygame.image.load(path).convert()

    def add_item_to_sprite(self, x: int, y: int, item: Item):
        new_sprite = ObjectSprite(x, y, item)
        new_sprite.load()
        self._sprites.append(new_sprite)
        
    def get_sprite(self, id_sprite: int) -> Sprite | None:
        return next(sprite for sprite in self.sprites if sprite.id == id_sprite)
    
    def add_sprite(self, sprite: Sprite):
        self._sprites.append(sprite)

    @property
    def map(self) -> List[List[int]]:
        return self._map
    
    @property
    def sprites(self) -> List[Sprite]:
        return self._sprites
    
    @property
    def textures(self) -> Dict[int, Surface]:
        return self._textures
    
    @property
    def id_save(self) -> int:
        return self._id_save