from app.sprites.collision_sprite import *

class FinalDoorSprite(CollisionSprite):
    def __init__(self, x, y, image, id=None, is_open=False):
        super().__init__(x, y, image, 'Trouver les 5 codes pour ouvrir la porte', id, is_open)

    def show_dialog(self, screen, user):
        super().show_dialog(screen, user.can_open_final_door)

    def handle_open(self, user):
        if user.can_open_final_door:
            super().handle_open()