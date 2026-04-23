from user import *
from pygame import Surface
from constants.ui import *
from constants.assets import *

class Battery:

    _max_width = 200

    def __init__(self, screen: Surface, user: User):
        self.user = user
        self.screen = screen

    def draw(self):
        battries = self.user.battery // BATTERY_CAPACITY
        for i in range(battries):
            self.screen.blit(Assets.battery, (SCREEN_PADDING + 50 * i, 75))