import math
from typing import List
from pygame import Surface
import pygame
from user import User
from sprite.sprite import *
from sprite.object_sprite import *

class RayCasting:

    _step: float = 0.03

    def __init__(self, screen: Surface, map: List[List[int]], user: User, sprites: List[Sprite]):
        self.screen = screen
        self.map = map
        self.user = user
        self.textures = {
            1: pygame.image.load('assets/textures/wall.png').convert(),
            2: pygame.image.load('assets/textures/sky.png').convert(),
        }
        
        self.z_buffer = [float('inf')] * screen.get_width()
        self.sprites = sprites

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

                    self.z_buffer[i] = distance
                    break
                
    def draw_sprites(self, user: User):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        sorted_sprites = sorted(
            self.sprites,
            key=lambda s: math.hypot(s.pos_x - user.get_pos_x, s.pos_y - user.get_pos_y),
            reverse=True
        )

        for sprite in sorted_sprites:

            if isinstance(sprite, ObjectSprite) and sprite.is_added:
                continue

            dx = sprite.pos_x  - user.get_pos_x
            dy = sprite.pos_y  - user.get_pos_y
            distance = math.hypot(dx, dy)

            if distance < 0.1:
                continue

            sprite_angle = math.atan2(dy, dx)
            angle_diff = sprite_angle - user.get_rot

            while angle_diff > math.pi:  angle_diff -= 2 * math.pi
            while angle_diff < -math.pi: angle_diff += 2 * math.pi

            half_fov = user.get_fov / 2

            if abs(angle_diff) > half_fov + 0.3:
                continue

            sprite_height = 0
            if isinstance(sprite, ObjectSprite):
                sprite_height = int((screen_height//6) / distance)
            else:
                sprite_height = int(screen_height//1.5 / distance)
            sprite_width = sprite_height

            center_x = int((0.5 + angle_diff / user.get_fov) * screen_width)

            x_start = center_x - sprite_width // 2
            x_end   = center_x + sprite_width // 2

            texture = sprite.texture
            tex_w = texture.get_width()
            tex_h = texture.get_height()
            
            y_start = 0
            if isinstance(sprite, ObjectSprite):
                y_start = screen_height // 2 + sprite_height
            else:
                y_start = screen_height // 2 - sprite_height // 4

            for col in range(x_start, x_end):
                if col < 0 or col >= screen_width:
                    continue

                if distance >= self.z_buffer[col]:
                    continue

                tex_x = int((col - x_start) / sprite_width * tex_w)
                tex_x = max(0, min(tex_x, tex_w - 1))

                tex_col = texture.subsurface(pygame.Rect(tex_x, 0, 1, tex_h))
                
                scaled_col = pygame.transform.scale(tex_col, (1, max(1, sprite_height)))

                self.screen.blit(scaled_col, (col, y_start))