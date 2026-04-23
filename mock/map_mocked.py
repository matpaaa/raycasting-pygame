from sprite.human_sprite import *
from sprite.object_sprite import *
from constants.assets import *
from item_factory import *
from sprite.door_sprite import *
from sprite.enemie_sprite import *


MAP_MOCKED = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
    [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

default_pnj_path = './assets/game/pnj/default-pnj.png'
epstein_pnj_path = './assets/game/pnj/epstein-pnj.png'
arnaud_pnj_path = './assets/game/pnj/arnaud-pnj.png'
zombie_path = './assets/game/pnj/zombie-pnj.png'

MAP_SPRITES_MOCKED = [
    HumanSprite(1.5, 2, default_pnj_path, [
        'Hello'
    ]),
    HumanSprite(2.5, 2, epstein_pnj_path, [
        'Hello'
    ]),
    HumanSprite(3.5, 2, arnaud_pnj_path, [
        'Hello'
    ]),
    DoorSprite(6, 1.5, arnaud_pnj_path),
    DoorSprite(8, 1.5, arnaud_pnj_path),
    EnemieSprite(5, 1.5, zombie_path, 50, 20),
    ObjectSprite(1.5, 3, ItemFactory.vodka()),
    ObjectSprite(2.5, 3, ItemFactory.code(1)),
    ObjectSprite(3.5, 3, ItemFactory.code(2)),
    ObjectSprite(4.0, 3, ItemFactory.key()),
    ObjectSprite(4.5, 3, ItemFactory.key()),
    ObjectSprite(1.5, 4, ItemFactory.canned()),
    ObjectSprite(2.5, 4, ItemFactory.gun()),
    ObjectSprite(3.5, 4, ItemFactory.ammo()),
    ObjectSprite(4.5, 4, ItemFactory.ammo())
]

MAP_TEXTURES_MOCKED = {
    1: './assets/textures/wall.png',
    2: './assets/textures/sky.png',
}