import time

class PlayerModel:
    id_player: int
    health: int
    energy: int
    pos_x: float
    pos_y: float
    rotation: float
    created_at: time
    name: str
    is_owner: bool