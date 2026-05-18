import time

class SpriteModel:
    id_sprite: int
    pos_x: float
    pos_y: float
    image: str
    
class SpriteDoor(SpriteModel):
    id_sprite_door_type: str
    
class SpriteItem(SpriteModel):
    created_at: time
    id_item: str
    value: float
    name: str
    id_item_type: str
    
class SpriteEnemie(SpriteModel):
    created_at: time
    health: int
    damage: int