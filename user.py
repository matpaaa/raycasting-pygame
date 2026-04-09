import math
from typing import List
from settings import *
from sounds import *

class User:

    _rotate_rad = math.pi / 48
    _velocity: float = 0.03
    _fov: int = math.pi / 3
    _max_health = 160
    _health = _max_health
    _slot_select = 0

    def __init__(self, pos_x: int, pos_y: int, rot: float, map: List[List[int]]):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rot = rot
        self.map = map

    def _is_collision(self, pos_x: float, pos_y: float):
        is_collision = self.map[int(pos_y)][int(pos_x)] != 0
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
        if self._health + heal > self._max_health:
            self._health = self._max_health
        else:
            self._health += heal

    def handle_select_slot(self, slot_num):
        if slot_num < 0 or slot_num > MAX_ITEM_SLOTS or slot_num == self._slot_select: return
        self._slot_select = slot_num

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
