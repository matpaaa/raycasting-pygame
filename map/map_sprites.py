from sprite.human_sprite import *
from sprite.object_sprite import *
from constants.assets import *
from item_factory import *

default_pnj_path = './assets/game/pnj/default-pnj.png'
epstein_pnj_path = './assets/game/pnj/epstein-pnj.png'
arnaud_pnj_path = './assets/game/pnj/arnaud-pnj.png'

MAP_SPRITES = [
    HumanSprite(1.5, 2, default_pnj_path, [
        'Hello'
    ]),
    HumanSprite(2.5, 2, epstein_pnj_path, [
        'Hello'
    ]),
    HumanSprite(3.5, 2, arnaud_pnj_path, [
        'Hello'
    ]),
    ObjectSprite(1.5, 3, ItemFactory.vodka()),
    ObjectSprite(2.5, 3, ItemFactory.code(1)),
    ObjectSprite(3.5, 3, ItemFactory.code(2))
]