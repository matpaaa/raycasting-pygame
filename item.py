import pygame

class Item:
    def __init__(self, id_item: str, name: str, value: int  | float| None, id_item_type: str, image: str):
        self.id_item = id_item
        self.name = name
        self.value = value
        self.id_item_type = id_item_type
        self.image = image

    @property
    def texture(self):
        return pygame.transform.scale(
            pygame.image.load(self.image).convert_alpha(),
            (32, 32)
        )
    
    def texture_size(self, size=32):
        return pygame.transform.scale(
            pygame.image.load(self.image).convert_alpha(),
            (size, size)
        )