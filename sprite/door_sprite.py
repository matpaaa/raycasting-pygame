from sprite.sprite import *
from ui.dialog import *
from sprite.collision_sprite import *

class DoorSprite(CollisionSprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, 'Une clé est nécessaire pour ouvrir la porte')

    def show_dialog(self, screen, user):
        super().show_dialog(screen, user.can_open_door)

    def handle_open(self, user):
        if user.can_open_door:
            user.use_key()
            super().handle_open()
