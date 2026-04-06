from constants.ui import *
from settings import *
from constants.assets import *

class HomeScreen:

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.home_background, (0, 0))
        self.screen.blit(Assets.home_title, (Assets.home_title.get_width() - SCREEN_PADDING, SCREEN_HEIGHT / 2 - Assets.home_title.get_height() / 2))
        self.screen.blit(Assets.logo, (SCREEN_PADDING, SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2))