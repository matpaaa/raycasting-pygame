from typing import List, Dict
from sprite.sprite import *
from pygame import Surface
import pygame

class MapConfig:

    def __init__(self, map: List[List[int]], sprites: List[Sprite], textures_path: Dict[int, str]):
        self._map = map
        self._sprites = sprites
        self._textures_path = textures_path
        self._textures = {}

    def load_textures(self):
        for path_key in self._textures_path:
            path = self._textures_path[path_key]
            self._textures[path_key] = pygame.image.load(path).convert()

    @property
    def map(self) -> List[List[int]]:
        return self._map
    
    @property
    def sprites(self) -> List[Sprite]:
        return self._sprites
    
    @property
    def textures(self) -> Dict[int, Surface]:
        return self._textures