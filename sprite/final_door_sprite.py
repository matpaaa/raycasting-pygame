from sprite.collision_sprite import *

class FinalDoorSprite(CollisionSprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, 'Trouver les 5 codes pour ouvrir la porte')

    def show_dialog(self, screen, user):
        super().show_dialog(screen, user.can_open_final_door)

    def handle_open(self, user):
        if user.can_open_final_door:
            super().handle_open()