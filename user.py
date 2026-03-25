import math
from typing import List


class User:

    _rotate_rad = math.pi / 48
    _velocity: float = 0.03
    _fov: int = math.pi / 3

    def __init__(self, pos_x: int, pos_y: int, rot: float, map: List[List[int]]):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rot = rot
        self.map = map

    def _is_collision(self, pos_x: float, pos_y: float):
        return self.map[int(pos_y)][int(pos_x)] != 0

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
