import pygame

class Fonts:
    font_title_big = None
    font_title_small = None
    font_btn = None

    @staticmethod
    def load():
        try:
            Fonts.font_title_big  = pygame.font.SysFont("couriernew", 90, bold=True)
            Fonts.font_title_small= pygame.font.SysFont("couriernew", 72, bold=True)
            Fonts.font_btn        = pygame.font.SysFont("couriernew", 28, bold=True)
        except:
            Fonts.font_title_big  = pygame.font.SysFont(None, 90, bold=True)
            Fonts.font_title_small= pygame.font.SysFont(None, 72, bold=True)
            Fonts.font_btn        = pygame.font.SysFont(None, 28, bold=True)