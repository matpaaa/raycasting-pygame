import pygame
from constants.color import *
from constants.fonts import *

class Button:
    def __init__(self, text, x, y, w, h, variant='default'):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.variant = variant
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surface):
        pygame.draw.rect(surface, BUTTON_BACKGROUND, self.rect, border_radius=4)

        color = BUTTON_WHITE
        if self.variant == 'danger':
            color = BUTTON_DANGER

        pygame.draw.rect(surface, color, self.rect, 2, border_radius=4)
        label = Fonts.font_btn.render(self.text, True, color)
        lx = self.rect.centerx - label.get_width()  // 2
        ly = self.rect.centery - label.get_height() // 2
        surface.blit(label, (lx, ly))

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos))