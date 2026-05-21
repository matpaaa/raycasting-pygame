import pygame

class Sprite:
    def __init__(self, x, y, image, id=None):
        self._x = x
        self._y = y
        self._image = image
        self._id = id
        self._texture = None


    def load(self) :
        if self._texture is None:
            self._texture = pygame.image.load(self._image).convert_alpha()
            
        self._sprite = {
            'x': self._x,
            'y': self._y,
            'texture': self._texture
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
    def image(self):
        return self._image
    
    @property
    def id(self):
        return self._id
    
    @property
    def texture(self):
        return self._sprite['texture']
    