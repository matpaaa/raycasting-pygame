import pygame

class Fonts:
    font_title = None
    font_subtitle = None
    font_btn = None

    @staticmethod
    def load():
        Fonts.font_title           = pygame.font.SysFont("couriernew", 32, bold=True)
        Fonts.font_subtitle        = pygame.font.SysFont("couriernew", 18, bold=True)
        Fonts.font_btn        = pygame.font.SysFont("couriernew", 28, bold=True)