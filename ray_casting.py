import math
from typing import List
from pygame import Surface
import pygame
from user import User


class RayCasting:

    _step: float = 0.03

    def __init__(self, screen: Surface, map: List[List[int]], user: User):
        self.screen = screen
        self.map = map
        self.user = user
        self.textures = {
            0: pygame.image.load('assets/cell.png').convert(),
            1: pygame.image.load('assets/sky.png').convert(),
        }

    def width_map_ratio(self, width: int) -> int:
        return width * len(self.map[0]) / self.screen.get_width()
    
    def height_map_ratio(self, height: int) -> int:
        return height * len(self.map[0]) / self.screen.get_height()

    def launch_fucking_rays(self, user: User):
        for i in range (self.screen.get_width()):
            rot_i = user.get_rot - (user.get_fov / 2) + user.get_fov  * i / self.screen.get_width()

            dx = self._step * math.cos(rot_i)
            dy = self._step * math.sin(rot_i)

            x, y = user.get_pos_x, user.get_pos_y
            n = 0
            color = 'gray'

            while True:
                x = x + dx
                y = y + dy
                n += 1

                pos = self.map[int(y)][int(x)]
                if pos != 0:
                    distance = self._step * n
                    distance *= math.cos(user.get_rot - rot_i)
                    height = self.screen.get_width() / distance

                    color = 'gray'

                    if pos == 2:
                        color = 'red'

                    break

            y1 = self.screen.get_height()/2 - height/2
            y2 = self.screen.get_height()/2 + height/2

            floor = self.screen.get_width()/2 + height/2
            cell = self.screen.get_width()/2 - height/2

            pygame.draw.line(self.screen, color, (i, y1), (i, y2))

            # texture = pygame.transform.scale(self.textures[0], (1, 100))
            # self.screen.blit(texture, (i, self.screen.get_height() - floor))

            # sky_offset = -10 * math.degrees(self.player.angle) % WIDTH
            # self.sc.blit(self.textures['S'], (sky_offset, 0))
            # self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
            # self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
            # pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

