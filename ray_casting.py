import math
from typing import List
from pygame import Surface
import pygame
import numpy as np
from user import User
from sprite.sprite import *
from sprite.object_sprite import *
from sprite.door_sprite import *
from sprite.collision_sprite import *
from map_config import *

class RayCasting:
 
    def __init__(self, screen: Surface, user, map_config: MapConfig):
        self.screen = screen
        self.user = user
        self.map_config = map_config
        self.z_buffer = [float('inf')] * screen.get_width()
 
    def _cast_ray_dda(self, ox: float, oy: float, dx: float, dy: float):
        map_x, map_y = int(ox), int(oy)

        delta_x = abs(1 / dx) if dx != 0 else float('inf')
        delta_y = abs(1 / dy) if dy != 0 else float('inf')

        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1

        side_x = (map_x + 1 - ox) * delta_x if dx > 0 else (ox - map_x) * delta_x
        side_y = (map_y + 1 - oy) * delta_y if dy > 0 else (oy - map_y) * delta_y

        hit = False
        side = 0

        map_height = len(self.map_config.map)
        map_width = len(self.map_config.map[0])

        while not hit:
            if side_x < side_y:
                side_x += delta_x
                map_x += step_x
                side = 0
            else:
                side_y += delta_y
                map_y += step_y
                side = 1

            if not (0 <= map_x < map_width and 0 <= map_y < map_height):
                return float('inf'), 0.0, side, 0

            if self.map_config.map[map_y][map_x] != 0:
                hit = True

        tex_u = 0
        distance = 0
        if side == 0 and dx != 0:
            distance = (map_x - ox + (1 - step_x) / 2) / dx
            tex_u = oy + distance * dy
        elif (dy != 0):
            distance = (map_y - oy + (1 - step_y) / 2) / dy
            tex_u = ox + distance * dx

        tex_u -= math.floor(tex_u)
        wall_type = self.map_config.map[map_y][map_x]

        return distance, tex_u, side, wall_type
 
    def _build_darkness_overlay(self, screen_width: int, screen_height: int) -> Surface:
        light_w = 700
        light_h = 500
        center_x = screen_width // 2
        center_y = screen_height // 2

        z = np.array(self.z_buffer, dtype=np.float32)
        z = np.clip(z, 0, RENDER_DISTANCE)

        base_shadow = np.clip((z / RENDER_DISTANCE) * 255, 0, 255)
        shadow_2d = np.tile(base_shadow, (screen_height, 1)).astype(np.float32)

        if self.user.light_enabled:
            xs = np.arange(screen_width)
            ys = np.arange(screen_height)

            dx = np.clip(np.abs(xs - center_x) / (light_w / 2), 0, 1)
            dy = np.clip(np.abs(ys - center_y) / (light_h / 2), 0, 1)
            dist_norm = np.sqrt(np.outer(dy ** 2, np.ones(screen_width)) +
                                np.outer(np.ones(screen_height), dx ** 2))
            dist_norm = np.clip(dist_norm, 0, 1)

            boosted_render = RENDER_DISTANCE + 3
            boosted_shadow = np.tile(
                np.clip((z / boosted_render) * 255, 0, 255),
                (screen_height, 1)
            ).astype(np.float32)

            fade = dist_norm ** 2
            inside_mask = dist_norm < 1.0
            shadow_2d = np.where(
                inside_mask,
                boosted_shadow * (1 - fade) + shadow_2d * fade,
                shadow_2d
            )

        shadow_2d = np.clip(shadow_2d, 0, 255).astype(np.uint8)

        darkness = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        alpha_array = pygame.surfarray.pixels_alpha(darkness)
        alpha_array[:] = shadow_2d.T
        del alpha_array

        return darkness

    def launch_fucking_rays(self, user):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
 
        for i in range(screen_width):
            rot_i = user.get_rot - (user.get_fov / 2) + user.get_fov * i / screen_width
 
            dx = math.cos(rot_i)
            dy = math.sin(rot_i)
 
            distance, tex_u, side, pos = self._cast_ray_dda(
                user.get_pos_x, user.get_pos_y, dx, dy
            )

            if distance == float('inf'):
                self.z_buffer[i] = float('inf')
                continue

            if distance < 0.01:
                self.z_buffer[i] = float('inf')
                continue
 
            distance *= math.cos(user.get_rot - rot_i)
            wall_height = screen_height / distance
 
            texture = self.map_config.textures.get(pos)
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
                
    def draw_sprites(self, user: User):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        sorted_sprites = sorted(
            self.map_config.sprites,
            key=lambda s: math.hypot(s.pos_x - user.get_pos_x, s.pos_y - user.get_pos_y),
            reverse=True
        )

        for sprite in sorted_sprites:

            if isinstance(sprite, ObjectSprite) and sprite.is_added:
                continue

            if isinstance(sprite, CollisionSprite) and sprite.is_open:
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
            
            if isinstance(sprite, ObjectSprite):
                y_start = screen_height // 2 + sprite_height
            else:
                y_start = screen_height // 2 - sprite_height // 4

            scaled_texture = pygame.transform.scale(texture, (max(1, sprite_width), max(1, sprite_height)))

            for col in range(x_start, x_end):
                if col < 0 or col >= screen_width:
                    continue

                if distance >= self.z_buffer[col]:
                    continue

                tex_x = col - x_start
                tex_x = max(0, min(tex_x, sprite_width - 1))

                col_surface = scaled_texture.subsurface(pygame.Rect(tex_x, 0, 1, max(1, sprite_height)))
                self.screen.blit(col_surface, (col, y_start))

    def draw_darkness(self):
        """À appeler en dernier, après launch_fucking_rays et draw_sprites."""
        darkness = self._build_darkness_overlay(
            self.screen.get_width(), self.screen.get_height()
        )
        self.screen.blit(darkness, (0, 0))