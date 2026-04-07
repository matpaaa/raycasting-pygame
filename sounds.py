import pygame

class Sounds:

    @staticmethod
    def click():
        sound = pygame.mixer.Sound('./assets/sounds/click.mp3')
        sound.play()