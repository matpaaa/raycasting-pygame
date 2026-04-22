import pygame

class Sprite:
    def __init__(self, x, y, image):
        self._x = x
        self._y = y
        self._image = image


    def load(self) :
        self._sprite = {
            'x': self._x,
            'y': self._y,
            'texture': pygame.image.load(self._image).convert_alpha()
        }

    def set_image(self, image: str):
        self._image = image
        self.load()

    @property
    def pos_x(self):
        return self._sprite['x']
    
    @property
    def pos_y(self):
        return self._sprite['y']
    
    @property
    def texture(self):
        return self._sprite['texture']
    