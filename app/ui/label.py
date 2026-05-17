import pygame
from app.constants.fonts import *
from app.constants.color import *
from app.constants.ui import *
from app.constants.settings import *

class Label:

    def __init__(self, label, x, y, h):
        self.label = label
        self.x = x
        self.y = y
        self.h = h

        self.label_surf = Fonts.font_btn.render(self.label, True, BUTTON_WHITE)
        self.label_w = 400 + GAP_BETWEEN_ELEMENT_LABEL
        self.label_rect = pygame.Rect(x, y, self.label_w, h)

    def draw(self, surface):
        lx = ELEMENT_WIDTH_LARGE - self.label_surf.get_width()
        ly = self.label_rect.centery - self.label_surf.get_height() // 2
        surface.blit(self.label_surf, (lx, ly))
