import math
from typing import List
from pygame import Surface
import pygame
from user import User


class RayCasting:

    _step: float = 0.01

    def __init__(self, screen: Surface, map: List[List[int]]):
        self.screen = screen
        self.map = map

    def launch_fucking_rays(self, user: User):
        for i in range (self.screen.get_width()):
            rot_i = user.get_rot - (user.get_fov / 2) + user.get_fov  * i / self.screen.get_width()

            dx = self._step * math.cos(rot_i)
            dy = self._step * math.sin(rot_i)

            x, y = user.get_pos_x, user.get_pos_y
            n = 0
            color = 'red'

            while True:
                x = x + dx
                y = y + dy
                n += 1

                pos = self.map[int(y)][int(x)]
                if pos != 0:
                    distance = self._step * n
                    distance *= math.cos(user.get_rot - rot_i)
                    height = self.screen.get_width() / distance

                    color = 'red'

                    if pos == 2:
                        color = 'white'

                    break

            y1 = self.screen.get_width()/2 - height/2
            y2 = self.screen.get_width()/2 + height/2

            pygame.draw.line(self.screen, color, (i, y1), (i, y2))