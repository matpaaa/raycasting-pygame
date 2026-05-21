from app.sprites.human_sprite import *
from app.sprites.object_sprite import *
from app.constants.assets import *
from app._utils.item_factory import *
from app.sprites.door_sprite import *
from app.sprites.enemie_sprite import *


MAP_MOCKED = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
[1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
[1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1],
[1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

default_pnj_path = './app/assets/game/pnj/default-pnj.png'
epstein_pnj_path = './app/assets/game/pnj/epstein-pnj.png'
arnaud_pnj_path = './app/assets/game/pnj/arnaud-pnj.png'
zombie_path = './app/assets/game/pnj/zombie-pnj.png'
bars_path = './app/assets/textures/bars.png'

MAP_SPRITES_MOCKED = [
    HumanSprite(3.5, 6.5, arnaud_pnj_path, [
        'utilise Y pour plus d"infos de notre part',
        'Mon tunnel... ne va surtout pas là bas',
    ]),
    HumanSprite(42.5, 14.5, epstein_pnj_path, [
        "t'es venu me sortir de là ou juste me regarder crever ici ?",
        " impossibles de mettre la main sur ce maudit code."
    ]),
      HumanSprite(33.5, 2.5, default_pnj_path, [
        "à changer"#le vieux
    ]),
          HumanSprite(33.5, 2.5, default_pnj_path, [
        "à changer"
    ]),
      HumanSprite(32.5, 20.5, default_pnj_path, [
        "à changer"
    ]),
    HumanSprite(11.5, 1.5, default_pnj_path, [
        "tu veux un bout de code,tu en as là bas dans la salle de ces zombies .",
        "c'est fini pour moi meme si je sors...",
    ]),
    #Zombies
    EnemieSprite(38.5, 22.5, zombie_path, 0,0),
    EnemieSprite(37.5, 22.5, zombie_path, 0, 0),
    EnemieSprite(10.5, 8.5, zombie_path, 0, 0),
    EnemieSprite(28.5, 1.5, zombie_path, 0, 0),

   
# VODDDDDKAAAAAA
ObjectSprite(11.5, 16.5, ItemFactory.vodka()),
ObjectSprite(42.5, 1.5, ItemFactory.vodka()),
#conserves
ObjectSprite(1.5, 2.5, ItemFactory.canned()),
ObjectSprite(38.5, 14.5, ItemFactory.canned()),
ObjectSprite(31.5, 17.5, ItemFactory.canned()),
#Gun
ObjectSprite(31.5, 14.5, ItemFactory.gun()),
#Munitions
ObjectSprite(10.5, 9.5, ItemFactory.ammo()),
ObjectSprite(11.5, 9.5, ItemFactory.ammo()),
#Batteries 
ObjectSprite(26.5, 24.5, ItemFactory.battery()),
ObjectSprite(42.5, 24.5 ,ItemFactory.battery()),
# CODES
ObjectSprite(32.5, 14.5, ItemFactory.code(1)),
ObjectSprite(31.5, 5.5, ItemFactory.code(2)),
ObjectSprite(1.5, 14.5, ItemFactory.code(3)),
ObjectSprite(2.5, 5.5, ItemFactory.code(4)),
ObjectSprite(25.5, 23.5, ItemFactory.code(5)),

# CLÉS
ObjectSprite(12.5, 5.5, ItemFactory.key()),
ObjectSprite(9.5, 23.5, ItemFactory.key()),
ObjectSprite(18.5, 16.5, ItemFactory.key()),
ObjectSprite(27.5, 10.5, ItemFactory.key()),
ObjectSprite(40.5, 18.5, ItemFactory.key()),
]
MAP_TEXTURES_MOCKED = {
    1: './app/assets/textures/wall.png',
    2: './app/assets/textures/sky.png',
}