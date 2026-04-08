from user import *
from constants.assets import *
from settings import *
from constants.ui import *

class Inventory:
    
    _gap_item = 10

    def __init__(self, user: User, screen):
        self.user = user
        self.screen = screen

    def draw(self):
        for i in range(MAX_ITEM_SLOTS):
            is_select = self.user.slot_select == i

            self.screen.blit(Assets.slot_selected if is_select else Assets.slot, (
                (SCREEN_WIDTH/2 - Assets.item_size * (MAX_ITEM_SLOTS/2)) + (Assets.item_size + self._gap_item) * i,
                SCREEN_HEIGHT - (Assets.slot_selected_size if is_select else Assets.item_size) - SCREEN_PADDING
            ))