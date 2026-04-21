from typing import List
from sprite.sprite import *
from pygame import Surface
from ui.dialog import *

class HumanSprite(Sprite):

    def __init__(self, x, y, image, dialogs: List[str]):
        super().__init__(x, y, image)
        self.is_interact = False
        self.dialogs = dialogs
        self.diablog = Dialog(image)

    def handle_interaction(self, screen: Surface):
        if not self.is_interact:
            self.is_interact = True

        if self.is_interact:
            self.diablog.set_content(self.dialogs[0])
        
        if self.dialogs[0] is not None:
            self.diablog.draw(screen)