from user import *
from pygame import Surface
import pygame
from constants.ui import *

class Battery:

    _max_width = 200

    def __init__(self, screen: Surface, user: User):
        self.user = user
        self.screen = screen

    def draw(self):
        width = self.user.battery * self._max_width / MAX_USER_BATTERY
        rect = pygame.Rect(32, 75, width, 20)
        pygame.draw.rect(self.screen, '#aebb00', rect)