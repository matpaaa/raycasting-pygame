import time
from app.model.player_model import *
from app.model.item_model import *
from app.model.finish_model import *
from app.model.puzzle_model import *
from app.model.open_model import *
from app.sprites.enemie_sprite import *
from app.sprites.object_sprite import *
from app.sprites.door_sprite import *
from app.sprites.final_door_sprite import *

class SaveModel:
    id_save: int
    created_at: time
    updated_at: time
    duration: int
    id_map: int
    is_win: bool
    is_failed: bool
    
class SaveHomeModel(SaveModel):
    players: list[PlayerModel]
    
class SaveLoadedModel(SaveModel):
    players: list[PlayerModel]
    items_secret: list[ItemSecretModel]
    finish: list[FinishModel]
    puzzles: list[PuzzleModel]
    open: list[OpenModel]
    sprite_doors: list[DoorSprite | FinalDoorSprite]
    sprite_items: list[ObjectSprite]
    sprite_enemies: list[EnemieSprite]