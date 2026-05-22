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
        "t'es venu pour me sortir d'ici ?",
        " impossibles de mettre la main sur ce maudit code."
    ]),
     HumanSprite(11.5, 1.5, default_pnj_path, [
        "tu veux un bout de code?"
        "tu en as là bas dans la salle de ces zombies .",
        "c'est fini pour moi meme si je sors...",
        ]),

    HumanSprite(33.5, 2.5, default_pnj_path, [
    "Hein ? ... T’es nouveau toi ?",
    "J’te jure qu’avant ces murs étaient plus propres.",
    "J’ai perdu quelque chose ici... ou peut-être que non.",
    "Les codes... toujours ces maudits codes...",
    "J’entends les zombies la nuit. Ils grattent les murs.",
    "Faut pas aller dans le noir...",
    "Un jour la porte s’est ouverte toute seule. Enfin... je crois.",
    "T’as vu mon frère ? Il devait revenir il y a 20 ans.",
    "La sortie ? Hahaha... personne sort vraiment d’ici.",
    "J’avais une lampe avant... ou c’était une arme ?",
    "Le bloc nord sent la mort.",
    "Tu me rappelles quelqu’un... je ne sais pas qui.",
    "Les gardes ont disparu du jour au lendemain.",
    "Parfois les zombies parlent entre eux ?",
    "Le code... ah non oublie, j’ai encore mélangé.",
    ]),
    HumanSprite(35.5, 3.5, default_pnj_path, [
    "Les gardes étaient 5 avant.",
    "Ils auraient dû nous les donner...",
    "Au lieu de nous condamner.",
      ]),

    #Zombies
    EnemieSprite(38.5, 22.5, zombie_path, 50,20),
    EnemieSprite(37.5, 22.5, zombie_path, 50, 20),
    EnemieSprite(10.5, 8.5, zombie_path, 50, 20),
    EnemieSprite(28.5, 1.5, zombie_path, 50, 20),
   
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