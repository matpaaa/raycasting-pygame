import pygame
import math
from typing import List, Tuple, Dict
from pygame import Surface
from user import User

class Minimap:

    _MINIMAP_SIZE = 100
    _USER_SIZE = 0.2

    def __init__(self, screen: Surface, map: List[List[int]], user: User):
        self.screen = screen
        self.map = map
        self.user = user

    @property
    def get_map_pos(self) -> Dict:
        padding = 20
        if not self.screen:
            raise Exception("Erreur lors de l'affichage de la minimap l'écran n'existe pas")
        
        map_start_x = self.screen.get_width() - self._MINIMAP_SIZE - padding
        map_start_y = padding

        return {
            "map_start_x": map_start_x,
            "map_start_y": map_start_y,
        } 

    def draw(self):
        map_pos = self.get_map_pos
        ratio = self._MINIMAP_SIZE / len(self.map[0])

        pygame.draw.rect(self.screen, 'black', (map_pos['map_start_x'], map_pos['map_start_y'], self._MINIMAP_SIZE, self._MINIMAP_SIZE))
        for x in range(0, self._MINIMAP_SIZE):
            map_index_x = math.floor(x / ratio)
            map_x = x / ratio
            for y in range(0, self._MINIMAP_SIZE):
                map_index_y = math.floor(y / ratio)
                map_y = y / ratio

                if self.map[map_index_y][map_index_x] != 0:
                    pygame.draw.rect(self.screen, 'purple', (map_pos['map_start_x'] + x, map_pos['map_start_y'] + y, 1, 1))

                pos_x = self.user.get_pos_x
                pos_y = self.user.get_pos_y

                if pos_x - self._USER_SIZE < map_x and map_x < pos_x + self._USER_SIZE and pos_y - self._USER_SIZE < map_y and map_y < pos_y + self._USER_SIZE:
                    pygame.draw.rect(self.screen, 'white', (map_pos['map_start_x'] + x, map_pos['map_start_y'] + y, 1, 1))