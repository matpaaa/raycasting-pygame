import pygame
from settings import *

class Assets:
    background = None
    logo = None
    home_title = None
    screen_title = None

    @staticmethod
    def load():
        background = pygame.image.load('./assets/screens/background.png').convert_alpha()
        Assets.background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        Assets.logo = pygame.image.load('./assets/screens/logo.png').convert_alpha()
        Assets.screen_title = pygame.image.load('./assets/screens/screen-title.png').convert_alpha()
        Assets.home_title = pygame.image.load('./assets/screens/home-title.png').convert_alpha()