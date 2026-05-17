from pygame import Surface
import pygame
from app.constants.ui import *
from app.constants.settings import *
from app.constants.color import *
from app.constants.fonts import *

class Dialog:
    def __init__(self, image: str | None):
        self.content = None
        self.image = image

        self.rect = pygame.Rect(SCREEN_WIDTH/2 - ELEMENT_WIDTH_LARGE/2, SCREEN_HEIGHT - 150 - ELEMENT_HEIGHT, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT)

    def set_content(self, content: str | None):
        self.content = content

    @property
    def human_preview(self):
        if self.image is not None:
            return pygame.transform.scale(
                pygame.image.load(self.image).convert_alpha(),
                (32, 32)
            )

    def draw(self, screen: Surface):
        if self.content is None: return
        pygame.draw.rect(screen, BUTTON_BACKGROUND, self.rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=4)
        label = Fonts.font_error_bubble.render(self.content, True, WHITE)
        lx = self.rect.x + (0 if self.image is None else 40) + SCREEN_PADDING
        ly = self.rect.centery - label.get_height() // 2

        if self.image is not None:
            screen.blit(self.human_preview, ((SCREEN_WIDTH - ELEMENT_WIDTH_LARGE)/2 + SCREEN_PADDING, self.rect.centery - 16))

        screen.blit(label, (lx, ly))
