import pygame
from constants.ui import *
from settings import *
from constants.color import *
from constants.fonts import *
from ui.button import *
from sounds import *
from constants.assets import *

class ErrorBubble:

    def __init__(self, screen, content=None):
        self.screen = screen
        self.content = content
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - ELEMENT_WIDTH_LARGE/2, SCREEN_PADDING, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT)
        self.btn_close = Button(
            'FERMER',
            SCREEN_WIDTH - (SCREEN_WIDTH - ELEMENT_WIDTH_LARGE)/2 - SCREEN_PADDING - ELEMENT_WIDTH_VERY_SMALL,
            SCREEN_PADDING + (ELEMENT_HEIGHT - ELEMENT_HEIGHT_SMALL)/2,
            ELEMENT_WIDTH_VERY_SMALL,
            ELEMENT_HEIGHT_SMALL
        )

    def handle_event(self, event):
        if self.btn_close.is_clicked(event) and self.content is not None:
            Sounds.click()
            self.content = None

    def set_content(self, content: str):
        self.content = content

    def reset(self):
        self.content = None

    def draw(self):
        if self.content is None: return
        pygame.draw.rect(self.screen, BUTTON_BACKGROUND, self.rect, border_radius=4)
        pygame.draw.rect(self.screen, DANGER, self.rect, 2, border_radius=4)
        label = Fonts.font_subtitle.render(self.content, True, WHITE)
        lx = self.rect.centerx - label.get_width()  // 2
        ly = self.rect.centery - label.get_height() // 2
        self.screen.blit(label, (lx, ly))
        self.screen.blit(Assets.danger, ((SCREEN_WIDTH - ELEMENT_WIDTH_LARGE)/2 + SCREEN_PADDING, self.rect.centery - 16))
        self.btn_close.draw(self.screen)