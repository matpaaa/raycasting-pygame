from sprite.sprite import *
from ui.dialog import *
from pygame import Surface

class DoorSprite(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.is_open = False
        self.diablog = Dialog(None)

    def show_dialog(self, screen: Surface, user):
        if not self.is_open:
            if len(user.key_items) == 0:
                self.diablog.set_content('Une clé est nécessaire pour ouvrir la porte')
            else:
                self.diablog.set_content('Appuier sur E pour ouvrir la porte')
            self.diablog.draw(screen)

    def handle_open(self, user):
        if self.is_open: return
        
        can_open = user.use_key()
        if can_open:
            self.is_open = True
