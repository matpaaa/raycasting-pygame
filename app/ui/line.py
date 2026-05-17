import pygame
from app.constants.color import *

class Line:

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

        self.line_rect = pygame.Rect(x, y, w, 2)

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_WHITE, self.line_rect)