

import math


class User:

    _rotate_rad = math.pi / 8
    _velocity: float = 0.1
    _fov: int = math.pi / 3

    def __init__(self, pos_x: int, pos_y: int, rot: float):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rot = rot

    def move_up(self):
        self.pos_x = self.pos_x + self._velocity * math.cos(self.rot)
        self.pos_y = self.pos_y + self._velocity * math.sin(self.rot)

    def move_down(self):
        self.pos_x = self.pos_x - self._velocity * math.cos(self.rot)
        self.pos_y = self.pos_y - self._velocity * math.sin(self.rot)

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