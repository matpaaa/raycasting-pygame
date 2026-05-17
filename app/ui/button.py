import pygame
from app.constants.color import *
from app.constants.fonts import *
from app.ui.label import *

class Button:
    def __init__(self, text, x, y, w, h, variant='default', label=None):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.variant = variant

        self.label = label

        if label != None:
            self.label_rect = Label(label, x + 4, y, h)
            self.input_rect = pygame.Rect(x + self.label_rect.label_w + 4, y, w, h)
            self.rect = pygame.Rect(self.input_rect.width + GAP_BETWEEN_ELEMENT_LABEL, y, w, h)
        else:
            self.input_rect = pygame.Rect(x + 4, y, w, h)
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

        if self.label != None:
            self.label_rect.draw(surface)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos))