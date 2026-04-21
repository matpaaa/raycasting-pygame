from sprite.human_sprite import *
from sprite.object_sprite import *
from constants.assets import *
from item_factory import *

MAP_SPRITES = [
    HumanSprite(1.5, 2, 'assets/textures/epstein.png', [
        'Hello'
    ]),
    ObjectSprite(1.5, 3, ItemFactory.vodka())
]