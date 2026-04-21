import math
from pygame import Surface
from user import User
from constants.assets import Assets
from constants.ui import *
from constants.fonts import *
from constants.color import *

class Effect:

    def __init__(self, screen: Surface, user: User):
        self.screen = screen
        self.user = user

    def draw(self):
        if self.user.has_speed_boost and self.user.effect_time_remaining is not None:
            self.screen.blit(Assets.vodka, (SCREEN_WIDTH//2 - 350, SCREEN_HEIGHT - 100))
            label = Fonts.font_effect.render(str(math.floor(self.user.effect_time_remaining)), True, WHITE)
            self.screen.blit(label, (SCREEN_WIDTH//2 - 350 + Assets.vodka.get_width() + 16, SCREEN_HEIGHT - 100 + Assets.vodka.get_height()//2))