from typing import List
from app.sprites.sprite import *
from pygame import Surface
from app.ui.dialog import *
from app._utils.sounds import *
import time

class HumanSprite(Sprite):

    def __init__(self, x, y, image, dialogs: List[str], secret: str = None):
        super().__init__(x, y, image)
        self.is_interact = False
        self.dialogs = dialogs
        self.diablog = Dialog(image)
        self._dialog_index = 0
        self._last_change_dialog = None
        self.secret = secret

    @property
    def can_change_dialog(self):
        return not (self._last_change_dialog and time.time() - self._last_change_dialog <= 0.25)

    def next_dialog(self):
        if not self.can_change_dialog: return
        if self._dialog_index >= len(self.dialogs)-1: return
        Sounds.click()
        self._dialog_index += 1
        self._last_change_dialog = time.time()

    def previous_dialog(self):
        if not self.can_change_dialog: return
        if self._dialog_index == 0: return
        Sounds.click()
        self._dialog_index -= 1
        self._last_change_dialog = time.time()

    def interaction_released(self):
        self._dialog_index = 0
        self.is_interact = False

    def handle_interaction(self, screen: Surface):
        if not self.is_interact:
            self._dialog_index = 0
            self.is_interact = True

        current_dialog = self.dialogs[self._dialog_index]
        if current_dialog is None: return

        self.diablog.set_content(current_dialog)
        self.diablog.draw(screen)
        
    def handle_interaction_secret(self, screen: Surface):
        if self.secret:
            self.diablog.set_content(self.secret)
            self.diablog.draw(screen)