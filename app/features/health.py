from app.features.user import *
from app.constants.assets import *
from app.constants.ui import *

class Health:

    def __init__(self, user: User, screen):
        self.user = user
        self.screen = screen

    def draw(self):
        self.screen.blit(Assets.health[f'{self.user.health//10}'], (SCREEN_PADDING, SCREEN_PADDING))