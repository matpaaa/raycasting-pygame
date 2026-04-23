import pygame


class Sounds:

    @staticmethod
    def init():
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)

    @staticmethod
    def click():
        sound = pygame.mixer.Sound('./assets/sounds/click.mp3')
        sound.play()
        sound.set_volume(0.1)

    @staticmethod
    def hurt():
        sound = pygame.mixer.Sound('./assets/sounds/hurt.mp3')
        sound.play()
        sound.set_volume(0.5)

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
        pygame.mixer.music.play(loops=-1, fade_ms=5000)

    @staticmethod
    def damage():
        sound = pygame.mixer.Sound('./assets/sounds/damage.mp3')
        sound.play()
        sound.set_volume(0.5)

    @staticmethod
    def eat():
        sound = pygame.mixer.Sound('./assets/sounds/eat.mp3')
        sound.play()
        sound.set_volume(0.5)

    @staticmethod
    def shot():
        sound = pygame.mixer.Sound('./assets/sounds/shot.mp3')
        sound.play()
        sound.set_volume(0.25)

    @staticmethod
    def no_shot():
        sound = pygame.mixer.Sound('./assets/sounds/no-shot.mp3')
        sound.play()
        sound.set_volume(0.25)

    @staticmethod
    def take_gun():
        sound = pygame.mixer.Sound('./assets/sounds/take-gun.mp3')
        sound.play()
        sound.set_volume(0.3)

    @staticmethod
    def take_key():
        sound = pygame.mixer.Sound('./assets/sounds/take-key.mp3')
        sound.play()
        sound.set_volume(0.3)

    @staticmethod
    def take_item():
        sound = pygame.mixer.Sound('./assets/sounds/take-item.mp3')
        sound.play()
        sound.set_volume(0.3)

    @staticmethod
    def ammo():
        sound = pygame.mixer.Sound('./assets/sounds/ammo.mp3')
        sound.play()
        sound.set_volume(0.5)

    @staticmethod
    def bliat():
        sound = pygame.mixer.Sound('./assets/sounds/bliat.mp3')
        sound.play()
        sound.set_volume(0.25)