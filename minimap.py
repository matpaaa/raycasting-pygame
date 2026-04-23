import pygame
import math
from typing import List, Tuple, Dict
from pygame import Surface
from user import User
from map_config import *
from settings import *

class Minimap:

    _MINIMAP_SIZE = 100
    _USER_SIZE = 0.2

    def __init__(self, screen: Surface, user: User, map_config: MapConfig):
        self.screen = screen
        self.map_config = map_config
        self.user = user

    @property
    def get_map_pos(self) -> Dict:
        padding = 20
        
        map_start_x = self.screen.get_width() - self._MINIMAP_SIZE - padding
        map_start_y = padding

        return {
            "map_start_x": map_start_x,
            "map_start_y": map_start_y,
        } 

    def draw(self):
        map_pos = self.get_map_pos

        pos_x = self.user.get_pos_x
        pos_y = self.user.get_pos_y

        cell_size = self._MINIMAP_SIZE // (MINIMAP_USER_AREA_DISTANCE * 2 + 1)

        pygame.draw.rect(self.screen, 'black', (map_pos['map_start_x'], map_pos['map_start_y'], self._MINIMAP_SIZE, self._MINIMAP_SIZE))

        for dy in range(-MINIMAP_USER_AREA_DISTANCE, MINIMAP_USER_AREA_DISTANCE + 1):
            for dx in range(-MINIMAP_USER_AREA_DISTANCE, MINIMAP_USER_AREA_DISTANCE + 1):
                map_index_x = int(pos_x) + dx
                map_index_y = int(pos_y) + dy

                if not (0 <= map_index_x < len(self.map_config.map[0]) and 0 <= map_index_y < len(self.map_config.map)):
                    continue

                screen_x = map_pos['map_start_x'] + (dx + MINIMAP_USER_AREA_DISTANCE) * cell_size
                screen_y = map_pos['map_start_y'] + (dy + MINIMAP_USER_AREA_DISTANCE) * cell_size

                if self.map_config.map[map_index_y][map_index_x] != 0:
                    pygame.draw.rect(self.screen, 'purple', (screen_x, screen_y, cell_size, cell_size))

        center_x = map_pos['map_start_x'] + MINIMAP_USER_AREA_DISTANCE * cell_size
        center_y = map_pos['map_start_y'] + MINIMAP_USER_AREA_DISTANCE * cell_size
        pygame.draw.rect(self.screen, 'white', (center_x, center_y, cell_size, cell_size))