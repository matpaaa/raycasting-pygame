import pygame
from settings import *

class Assets:
    home_background = None
    logo = None
    home_title = None

    @staticmethod
    def load():
        image = pygame.image.load('./assets/home-background.png').convert_alpha()
        Assets.home_background = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        Assets.logo = pygame.image.load('./assets/logo.png').convert_alpha()
        Assets.home_title = pygame.image.load('./assets/home-title.png').convert_alpha()