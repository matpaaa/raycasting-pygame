from app.sprites.sprite import *
from app.ui.dialog import *
from app.sprites.collision_sprite import *

class DoorSprite(CollisionSprite):
    def __init__(self, x, y, image, id=None, is_open=False):
        super().__init__(x, y, image, 'Une clé est nécessaire pour ouvrir la porte', id, is_open)

    def show_dialog(self, screen, user):
        super().show_dialog(screen, user.can_open_door)
        
    def handle_force_open(self):
        super().handle_open()

    def handle_open(self, user):
        if user.can_open_door and not self.is_open:
            user.use_key()
            super().handle_open()
