import pygame
from pygame import Surface
from settings import *

class Assets:
    background: Surface | None = None
    logo: Surface | None = None
    home_title: Surface | None = None
    screen_title: Surface | None = None
    window: Surface | None = None
    danger: Surface | None = None

    vodka: Surface | None = None
    ammo: Surface | None = None
    code: Surface | None = None
    key: Surface | None = None
    slot: Surface | None = None
    slot_selected: Surface | None = None

    gun_selected: Surface | None = None

    health = {}

    item_size = 75
    slot_selected_size = 85

    @staticmethod
    def load():
        background = pygame.image.load('./assets/screens/background.png').convert_alpha()
        Assets.background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        Assets.logo = pygame.image.load('./assets/screens/logo.png').convert_alpha()
        Assets.screen_title = pygame.image.load('./assets/screens/screen-title.png').convert_alpha()
        Assets.home_title = pygame.image.load('./assets/screens/home-title.png').convert_alpha()
        Assets.window = pygame.image.load('./assets/screens/window.png').convert_alpha()
        Assets.danger = pygame.transform.scale(
            pygame.image.load('./assets/screens/danger.png').convert_alpha(),
            (32, 32)
        )

        Assets.vodka = pygame.transform.scale(
            pygame.image.load('./assets/game/items/vodka.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.ammo = pygame.transform.scale(
            pygame.image.load('./assets/game/items/ammo.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.code = pygame.transform.scale(
            pygame.image.load('./assets/game/items/code.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.key = pygame.transform.scale(
            pygame.image.load('./assets/game/items/key.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.slot = pygame.transform.scale(
            pygame.image.load('./assets/game/items/slot.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.slot_selected = pygame.transform.scale(
            pygame.image.load('./assets/game/items/slot.png').convert_alpha(),
            (Assets.slot_selected_size, Assets.slot_selected_size)
        )

        Assets.health = {
            '1': pygame.transform.scale(pygame.image.load('./assets/game/health/h-1.png').convert_alpha(), (300, 50)),
            '2': pygame.transform.scale(pygame.image.load('./assets/game/health/h-2.png').convert_alpha(), (300, 50)),
            '3': pygame.transform.scale(pygame.image.load('./assets/game/health/h-3.png').convert_alpha(), (300, 50)),
            '4': pygame.transform.scale(pygame.image.load('./assets/game/health/h-4.png').convert_alpha(), (300, 50)),
            '5': pygame.transform.scale(pygame.image.load('./assets/game/health/h-5.png').convert_alpha(), (300, 50)),
            '6': pygame.transform.scale(pygame.image.load('./assets/game/health/h-6.png').convert_alpha(), (300, 50)),
            '7': pygame.transform.scale(pygame.image.load('./assets/game/health/h-7.png').convert_alpha(), (300, 50)),
            '8': pygame.transform.scale(pygame.image.load('./assets/game/health/h-8.png').convert_alpha(), (300, 50)),
            '9': pygame.transform.scale(pygame.image.load('./assets/game/health/h-9.png').convert_alpha(), (300, 50)),
            '10': pygame.transform.scale(pygame.image.load('./assets/game/health/h-10.png').convert_alpha(), (300, 50)),
            '11': pygame.transform.scale(pygame.image.load('./assets/game/health/h-11.png').convert_alpha(), (300, 50)),
            '12': pygame.transform.scale(pygame.image.load('./assets/game/health/h-12.png').convert_alpha(), (300, 50)),
            '13': pygame.transform.scale(pygame.image.load('./assets/game/health/h-13.png').convert_alpha(), (300, 50)),
            '14': pygame.transform.scale(pygame.image.load('./assets/game/health/h-14.png').convert_alpha(), (300, 50)),
            '15': pygame.transform.scale(pygame.image.load('./assets/game/health/h-15.png').convert_alpha(), (300, 50)),
            '16': pygame.transform.scale(pygame.image.load('./assets/game/health/h-16.png').convert_alpha(), (300, 50)),
        }

        gun_selected = pygame.image.load('./assets/game/items/gun-selected.png').convert_alpha()
        Assets.gun_selected = pygame.transform.scale(gun_selected, (SCREEN_WIDTH, SCREEN_HEIGHT))
