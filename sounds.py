import pygame


class Sounds:

    @staticmethod
    def init():
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)

    @staticmethod
    def click():
        sound = pygame.mixer.Sound('./assets/sounds/click.mp3')
        sound.play()
        sound.set_volume(0.1)

    @staticmethod
    def walk():
        sound = pygame.mixer.Sound('./assets/sounds/walk.mp3')
        sound.play()
        sound.set_volume(0.1)
        return sound
    
    @staticmethod
    def home():
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load('./assets/sounds/home-music.mp3')
        pygame.mixer.music.play(loops=-1, fade_ms=5000)

    @staticmethod
    def game():
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load('./assets/sounds/game-music.mp3')
        pygame.mixer.music.play(loops=-1, fade_ms=2000)