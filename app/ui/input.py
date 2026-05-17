import pygame
from app.constants.color import *
from app.constants.fonts import *
from app.ui.label import *

class Input:
    def __init__(self, placeholder, x, y, input_w, h, label=None):
        self.placeholder = placeholder
        self.x = x
        self.y = y
        self.input_w = input_w
        self.h = h
        self.value = ""
        self.focused = False

        self.label = label

        if label != None:
            self.label_rect = Label(label, x + 4, y, h)
            self.input_rect = pygame.Rect(x + self.label_rect.label_w + 4, y, input_w, h)
        else:
            self.input_rect = pygame.Rect(x + 4, y, input_w, h)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.focused = self.input_rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.focused:
            if event.key == pygame.K_BACKSPACE:
                self.value = self.value[:-1]
            elif event.key not in (pygame.K_RETURN, pygame.K_TAB, pygame.K_ESCAPE):
                self.value += event.unicode

    def draw(self, surface):
        if self.label != None:
            self.label_rect.draw(surface)

        border_color = BUTTON_WHITE if self.focused else INPUT_BORDER_INACTIVE
        pygame.draw.rect(surface, INPUT_BACKGROUND, self.input_rect, border_radius=4)
        pygame.draw.rect(surface, border_color, self.input_rect, 2, border_radius=4)

        if self.value:
            text_surf = Fonts.font_btn.render(self.value, True, BUTTON_WHITE)
        else:
            text_surf = Fonts.font_btn.render(self.placeholder, True, INPUT_PLACEHOLDER)

        padding = 12
        max_w = self.input_rect.width - padding * 2

        if text_surf.get_width() > max_w:
            clip_rect = pygame.Rect(
                text_surf.get_width() - max_w, 0,
                max_w, text_surf.get_height()
            )
            text_surf = text_surf.subsurface(clip_rect)

        tx = self.input_rect.x + padding
        ty = self.input_rect.centery - text_surf.get_height() // 2
        surface.blit(text_surf, (tx, ty))