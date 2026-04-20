import pygame

class Fonts:
    font_title = None
    font_subtitle = None
    font_btn = None
    font_error_bubble = None

    @staticmethod
    def load():
        Fonts.font_title    = pygame.font.Font("./assets/fonts/pixel.otf", 32)
        Fonts.font_subtitle = pygame.font.Font("./assets/fonts/pixel.otf", 18)
        Fonts.font_error_bubble = pygame.font.Font("./assets/fonts/pixel.otf", 14)
        Fonts.font_btn      = pygame.font.Font("./assets/fonts/pixel.otf", 20)