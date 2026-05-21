from app.sprites.sprite import *
from app.ui.dialog import *

class CollisionSprite(Sprite):
    def __init__(self, x, y, image, invalid_message, id=None, is_open=False):
        super().__init__(x, y, image, id)

        self._is_open = is_open
        self._diablog = Dialog(None)
        self._invalid_message = invalid_message

    def show_dialog(self, screen: Surface, can_open: bool):
        if not self._is_open:
            if can_open:
                self._diablog.set_content('Appuier sur E pour ouvrir la porte')
            else:
                self._diablog.set_content(self._invalid_message)
            self._diablog.draw(screen)

    def handle_open(self):
        if self._is_open: return
        self._is_open = True

    @property
    def is_open(self) -> bool:
        return self._is_open