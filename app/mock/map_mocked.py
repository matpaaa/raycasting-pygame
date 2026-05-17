from app.sprites.human_sprite import *
from app.sprites.object_sprite import *
from app.constants.assets import *
from app._utils.item_factory import *
from app.sprites.door_sprite import *
from app.sprites.enemie_sprite import *


MAP_MOCKED = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
    [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
    [1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
    [1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,9,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

default_pnj_path = './app/assets/game/pnj/default-pnj.png'
epstein_pnj_path = './app/assets/game/pnj/epstein-pnj.png'
arnaud_pnj_path = './app/assets/game/pnj/arnaud-pnj.png'
zombie_path = './app/assets/game/pnj/zombie-pnj.png'
bars_path = './app/assets/textures/bars.png'

MAP_SPRITES_MOCKED = [
    HumanSprite(1.5, 2, arnaud_pnj_path, [
        'Salut à toi, tourne les flèches directionneles',
        'Je suis le formateur je vais te donner des conseils'
    ]),
    HumanSprite(19.5, 2, epstein_pnj_path, [
        "OHHHH merci, je te suis reconnaissant de l'avoir ouvert",
        "Un idiot m'a enfèrmé en prenant la clé de ma cellule"
    ]),
    HumanSprite(11.5, 1.5, default_pnj_path, [
        "Un mec fou passe son temps à taper dans sa cellule",
        "Il mérite d'etre enfèrmé selon moi",
        "j'ai caché sa clé il ne sortira pas pour l'instant"
    ]),
    DoorSprite(19.5, 4,bars_path ),
    DoorSprite(16.5, 16, bars_path ),
    DoorSprite(17.5, 6.5, bars_path),
    EnemieSprite(8, 17, zombie_path, 50, 20),
    ObjectSprite(2.5,7, ItemFactory.vodka()),
    ObjectSprite(19.5, 1.5, ItemFactory.code(1)),
    ObjectSprite(19,7.5 , ItemFactory.code(2)),  
    ObjectSprite(18.2, 12.3, ItemFactory.code(3)),
    ObjectSprite(3.5, 16.5, ItemFactory.code(4)),
    ObjectSprite(16.5, 18.5, ItemFactory.code(5)),
    ObjectSprite(2.5,3.5, ItemFactory.key()),
    ObjectSprite(19.5,3 , ItemFactory.key()),
    ObjectSprite(18.5,7.5,ItemFactory.key()),
    ObjectSprite(1.5, 2.5, ItemFactory.canned()), 
    ObjectSprite(13.3, 9.5, ItemFactory.gun()),
    ObjectSprite(10, 9.5, ItemFactory.ammo()),
    ObjectSprite(10.5, 9.5, ItemFactory.ammo())
]

MAP_TEXTURES_MOCKED = {
    1: './app/assets/textures/wall.png',
    2: './app/assets/textures/sky.png',
}