import math
import time
from typing import List
from settings import *
from sounds import *
from sprite.sprite import *
from sprite.human_sprite import *
from item import *
from sprite.object_sprite import *
from sprite.door_sprite import *
from sprite.enemie_sprite import *
from constants.assets import *
from map_config import *

class User:

    _rotate_rad = math.pi / 48
    _default_velocity: float = 0.02
    _velocity: float = 0.02
    _fov: int = math.pi / 3
    _max_health = 160
    _health = _max_health
    _slot_select = 0
    _items: List[Item] = []
    _speed_boost_end = None
    _min_time_user_item = 1
    _has_sprite_interaction = False
    _munition_sound = None
    _shoot_interval = 1
    _shoot_at = None
    _step_gun_ray = 0.02

    def __init__(self, pos_x: int, pos_y: int, rot: float, map_config: MapConfig):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rot = rot
        self.map_config = map_config

    def _is_collision(self, pos_x: float, pos_y: float):
        door_sprites: List[DoorSprite] = list(filter(lambda sprite: isinstance(sprite, DoorSprite), self.map_config.sprites))
        is_collision = False

        for sprite in door_sprites:
            if self.is_sprite_collision(0.5, sprite, pos_x, pos_y) and not sprite.is_open:
                is_collision = True
                break
        
        if not is_collision:
            is_collision = self.map_config.map[int(pos_y)][int(pos_x)] != 0

        if is_collision:
            Sounds.hurt()
        return is_collision

    def move_up(self):
        new_pos_x = self.pos_x + self._velocity * math.cos(self.rot)
        new_pos_y = self.pos_y + self._velocity * math.sin(self.rot)

        if self._is_collision(new_pos_x, new_pos_y):
            return

        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

    def move_down(self):
        new_pos_x = self.pos_x - self._velocity * math.cos(self.rot)
        new_pos_y = self.pos_y - self._velocity * math.sin(self.rot)

        if self._is_collision(new_pos_x, new_pos_y):
            return

        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

    def move_left(self):
        self.rot -= self._rotate_rad

    def move_right(self):
        self.rot += self._rotate_rad

    def damage(self, dmg):
        Sounds.damage()
        if self._health - dmg <= 0:
            self._health = 10
        else:
            self._health -= dmg

    def heal(self, heal):
        Sounds.eat()
        if self._health + heal > self._max_health:
            self._health = self._max_health
        else:
            self._health += heal

    def handle_select_slot(self, slot_num):
        if slot_num < 0 or slot_num > MAX_ITEM_SLOTS or slot_num == self._slot_select: return
        self._slot_select = slot_num

    def add_item(self, item: Item):
        if len(self.inventory_items) >= MAX_ITEM_SLOTS: return
        self._items.append(item)

    def drop_item(self):
        item_deleted = self.inventory_items.pop(self.slot_select)
        return item_deleted
    
    def get_item(self, index: int) -> Item | None:
        if len(self.inventory_items)-1 < index: return None
        return self.inventory_items[index]

    def sprite_interaction(self) -> Sprite | None:
        for sprite in self.map_config.sprites:
            interaction_area = 0.75 if isinstance(sprite, DoorSprite) else USER_INTERACTION_AREA
            if self.is_sprite_collision(interaction_area, sprite, self.pos_x, self.pos_y):
                if isinstance(sprite, ObjectSprite):
                    if sprite.is_added:
                        self._has_sprite_interaction = True
                    else:
                        self._has_sprite_interaction = True

                return sprite
                
            if isinstance(sprite, HumanSprite):
                self._has_sprite_interaction = False
                sprite.is_interact = False

    def use_item(self):
        if len(self.inventory_items)-1 < self.slot_select or self._has_sprite_interaction: return
        inventory_items = self.inventory_items

        if inventory_items[self.slot_select].id_item_type != 'CONSUMABLE' or inventory_items[self.slot_select].added_at and time.time() - inventory_items[self.slot_select].added_at < self._min_time_user_item: return

        item_used = inventory_items.pop(self.slot_select)

        self._items = inventory_items + self.secret_items + self.ammo_items

        if item_used.id_item == 'VODKA':
            Sounds.bliat()
            self._velocity = item_used.value
            self._speed_boost_end = time.time() + EFFECT_VODKA_TIME

        if item_used.id_item == 'CANNED':
            self.heal(item_used.value)

    def handle_effect(self):
        if self.has_speed_boost and time.time() >= self._speed_boost_end:
            self._velocity = self._default_velocity
            self._speed_boost_end = None

        if self._munition_sound  and self._munition_sound <= time.time():
            Sounds.ammo()
            self._munition_sound = None

    def handle_shoot(self):
        if self._shoot_at and time.time() - self._shoot_at < self._shoot_interval: return
        if self.item_selected is None: return
        if self.item_selected.id_item_type != 'WEAPON': return
    
        self._shoot_at = time.time()

        if len(self.ammo_items) == 0:
            Sounds.no_shot()
        else:
            Sounds.shot()
            self._items = self.inventory_items + self.secret_items + self.ammo_items[0:len(self.ammo_items)-1]
            self._munition_sound = time.time() + 1
            sprite_shooted = self.get_enemie_shot()

            if not sprite_shooted is None:
                sprite_shooted.receive_damage(self.item_selected.value)

    def get_enemie_shot(self):
        dx = math.cos(self.get_rot)
        dy = math.sin(self.get_rot)

        x, y = self.get_pos_x, self.get_pos_y

        enemy_sprites = [s for s in self.map_config.sprites if isinstance(s, EnemieSprite)]

        while True:
            x += dx * self._step_gun_ray
            y += dy * self._step_gun_ray

            map_x, map_y = int(x), int(y)

            if not (0 <= map_x < len(self.map_config.map[0]) and 0 <= map_y < len(self.map_config.map)):
                return None
            
            if self.map_config.map[map_y][map_x] != 0:
                return None

            for sprite in enemy_sprites:
                dist = math.hypot(sprite.pos_x - x, sprite.pos_y - y)
                if dist < 0.25:
                    return sprite

    def use_key(self) -> bool:
        if len(self.key_items) == 0:
            # TODO Mettre le son quand on a pas la clé
            return False
        else:
            self._items = self.inventory_items + self.code_items + self.key_items[0:len(self.key_items)-1] + self.ammo_items
            return True
        
    def is_sprite_collision(self, area: float, sprite: Sprite, pos_x: float, pos_y: float):
        if sprite.pos_x <= pos_x + area and sprite.pos_x >= pos_x - area:
            if sprite.pos_y <= pos_y + area and sprite.pos_y >= pos_y - area:
                return True
        return False
    
    def draw_item_select(self, screen: Surface):
        if self.item_selected and self.item_selected.id_item == 'GUN':
            screen.blit(Assets.gun_selected, (0, 0))

    @property
    def get_fov(self) -> int:
        return self._fov
    
    @property
    def get_rot(self):
        return self.rot

    @property
    def get_velociy(self) -> float:
        return self._velocity
    
    @property
    def get_pos_x(self) -> float:
        return self.pos_x
    
    @property
    def get_pos_y(self) -> float:
        return self.pos_y
    
    @property
    def health(self) -> int:
        return self._health
    
    @property
    def slot_select(self) -> int:
        return self._slot_select

    @property
    def has_speed_boost(self) -> bool:
        return self._velocity != self._default_velocity
    
    @property
    def effect_time_remaining(self):
        if self._speed_boost_end is None: return None
        time_left = self._speed_boost_end - time.time()
        return time_left if time_left >= 0 else None
    
    @property
    def items(self) -> List[Item]:
        return self._items
    
    @property
    def inventory_items(self) -> List[Item]:
        return list(filter(lambda item: item.id_item_type != 'SECRET' and item.id_item_type != 'AMMO', self._items))
    
    @property
    def secret_items(self) -> List[Item]:
        return list(filter(lambda item: item.id_item_type == 'SECRET', self._items))
    
    @property
    def key_items(self) -> List[Item]:
        return list(filter(lambda item: item.id_item == 'KEY', self._items))
    
    @property
    def code_items(self) -> List[Item]:
        return list(filter(lambda item: item.id_item == 'CODE', self._items))
    
    @property
    def ammo_items(self) -> List[Item]:
        return list(filter(lambda item: item.id_item_type == 'AMMO', self._items))
    
    @property
    def has_sprite_interaction(self) -> bool:
        return self._has_sprite_interaction
    
    @property
    def item_selected(self) -> Item | None:
        if len(self.inventory_items)-1 < self.slot_select: return
        return self.inventory_items[self.slot_select]