import pygame
from pygame import Surface
from app.constants.settings import *

class Assets:
    background: Surface | None = None
    logo: Surface | None = None
    home_title: Surface | None = None
    screen_title: Surface | None = None
    window: Surface | None = None
    window_small: Surface | None = None
    danger: Surface | None = None

    vodka: Surface | None = None
    ammo: Surface | None = None
    code: Surface | None = None
    key: Surface | None = None
    battery: Surface | None = None
    slot: Surface | None = None
    slot_selected: Surface | None = None

    gun_selected: Surface | None = None

    light_off: Surface | None = None
    light_on: Surface | None = None

    dead_screen: Surface | None = None
    win_screen: Surface | None = None

    health = {}

    item_size = 75
    slot_selected_size = 85

    @staticmethod
    def load():
        background = pygame.image.load('./app/assets/screens/background.png').convert_alpha()
        Assets.background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        Assets.logo = pygame.image.load('./app/assets/screens/logo.png').convert_alpha()
        Assets.screen_title = pygame.image.load('./app/assets/screens/screen-title.png').convert_alpha()
        Assets.home_title = pygame.image.load('./app/assets/screens/home-title.png').convert_alpha()
        Assets.window = pygame.image.load('./app/assets/screens/window.png').convert_alpha()
        Assets.window_small = pygame.image.load('./app/assets/screens/window-small.png').convert_alpha()
        Assets.danger = pygame.transform.scale(
            pygame.image.load('./app/assets/screens/danger.png').convert_alpha(),
            (32, 32)
        )

        Assets.vodka = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/vodka.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.ammo = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/ammo.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.code = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/code.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.battery = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/battery.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.key = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/key.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.slot = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/slot.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )

        Assets.slot_selected = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/slot.png').convert_alpha(),
            (Assets.slot_selected_size, Assets.slot_selected_size)
        )

        Assets.health = {
            '1': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-1.png').convert_alpha(), (300, 50)),
            '2': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-2.png').convert_alpha(), (300, 50)),
            '3': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-3.png').convert_alpha(), (300, 50)),
            '4': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-4.png').convert_alpha(), (300, 50)),
            '5': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-5.png').convert_alpha(), (300, 50)),
            '6': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-6.png').convert_alpha(), (300, 50)),
            '7': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-7.png').convert_alpha(), (300, 50)),
            '8': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-8.png').convert_alpha(), (300, 50)),
            '9': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-9.png').convert_alpha(), (300, 50)),
            '10': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-10.png').convert_alpha(), (300, 50)),
            '11': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-11.png').convert_alpha(), (300, 50)),
            '12': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-12.png').convert_alpha(), (300, 50)),
            '13': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-13.png').convert_alpha(), (300, 50)),
            '14': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-14.png').convert_alpha(), (300, 50)),
            '15': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-15.png').convert_alpha(), (300, 50)),
            '16': pygame.transform.scale(pygame.image.load('./app/assets/game/health/h-16.png').convert_alpha(), (300, 50)),
        }

        gun_selected = pygame.image.load('./app/assets/game/items/gun-selected.png').convert_alpha()
        Assets.gun_selected = pygame.transform.scale(gun_selected, (SCREEN_WIDTH, SCREEN_HEIGHT))

        Assets.dead_screen = pygame.image.load('./app/assets/screens/dead-screen.png').convert_alpha()
        Assets.win_screen = pygame.image.load('./app/assets/screens/win-screen.png').convert_alpha()

        Assets.light_off = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/light-off.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )
        Assets.light_on = pygame.transform.scale(
            pygame.image.load('./app/assets/game/items/light-on.png').convert_alpha(),
            (Assets.item_size, Assets.item_size)
        )