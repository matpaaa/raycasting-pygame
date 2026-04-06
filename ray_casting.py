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
            1: pygame.image.load('assets/cell.png').convert(),
            2: pygame.image.load('assets/sky.png').convert(),
        }

    def launch_fucking_rays(self, user: User):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        for i in range(screen_width):
            rot_i = user.get_rot - (user.get_fov / 2) + user.get_fov * i / screen_width

            dx = self._step * math.cos(rot_i)
            dy = self._step * math.sin(rot_i)

            x, y = user.get_pos_x, user.get_pos_y
            n = 0

            while True:
                x += dx
                y += dy
                n += 1

                map_x, map_y = int(x), int(y)
                pos = self.map[map_y][map_x]

                if pos != 0:
                    distance = self._step * n
                    distance *= math.cos(user.get_rot - rot_i)
                    wall_height = screen_height / distance

                    frac_x = x - map_x
                    frac_y = y - map_y

                    if min(frac_x, 1 - frac_x) < min(frac_y, 1 - frac_y):
                        tex_u = frac_y
                    else:
                        tex_u = frac_x

                    # Render col with texture
                    texture = self.textures.get(pos)
                    if texture:
                        tex_width = texture.get_width()
                        tex_height = texture.get_height()

                        tex_x = int(tex_u * tex_width) % tex_width
                        tex_column = texture.subsurface(pygame.Rect(tex_x, 0, 1, tex_height))

                        wall_h = int(wall_height)
                        scaled_column = pygame.transform.scale(tex_column, (1, max(1, wall_h)))

                        y1 = int(screen_height / 2 - wall_h / 2)
                        self.screen.blit(scaled_column, (i, y1))
                    else:
                        color = 'red'
                        y1 = screen_height / 2 - wall_height / 2
                        y2 = screen_height / 2 + wall_height / 2
                        pygame.draw.line(self.screen, color, (i, y1), (i, y2))

                    break