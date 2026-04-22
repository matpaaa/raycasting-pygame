from user import *
from constants.assets import *
from settings import *
from constants.ui import *
from constants.fonts import *
from constants.color import *

class Inventory:
    
    _gap_item = 10
    _secret_size = 56
    _ammo_size = 40

    def __init__(self, user: User, screen):
        self.user = user
        self.screen = screen

        self.label_surf = Fonts.font_btn.render('Appuier sur E pour consommer', True, BUTTON_WHITE)
        self.label_w = 400 + GAP_BETWEEN_ELEMENT_LABEL
        self.label_rect = pygame.Rect(SCREEN_WIDTH//2 - 400//2, SCREEN_HEIGHT - 150, self.label_w, 50)

    def draw(self):
        for i in range(MAX_ITEM_SLOTS):
            is_select = self.user.slot_select == i

            item = self.user.get_item(i)

            pos_x = (SCREEN_WIDTH/2 - Assets.item_size * (MAX_ITEM_SLOTS/2)) + (Assets.item_size + self._gap_item) * i
            pos_y = SCREEN_HEIGHT - (Assets.slot_selected_size if is_select else Assets.item_size) - SCREEN_PADDING

            slot_texture = Assets.slot_selected if is_select else Assets.slot

            self.screen.blit(slot_texture, (pos_x, pos_y))

            if item is not None and item.id_item_type != 'SECRET':
                self.screen.blit(item.texture, (pos_x + slot_texture.get_width()//2 - item.texture.get_width()//2, pos_y + slot_texture.get_height()//2 - item.texture.get_height()//2))

                if is_select and item.id_item_type == 'CONSUMABLE' and not self.user.has_sprite_interaction:
                    lx = self.label_rect.centerx - self.label_surf.get_width() // 2
                    ly = self.label_rect.centery - self.label_surf.get_height() // 2
                    self.screen.blit(self.label_surf, (lx, ly))

        for i in range(len(self.user.code_items)):
            item = self.user.code_items[i]
            lx = SCREEN_WIDTH - 100
            ly = SCREEN_HEIGHT - (100 + 64 * i+1)
            self.screen.blit(item.texture_size(self._secret_size), (lx, ly))
            code_label = Fonts.font_btn.render(str(item.value), True, BUTTON_BACKGROUND)
            self.screen.blit(code_label, (lx + self._secret_size//3, ly + self._secret_size//3))

        for i in range(len(self.user.key_items)):
            item = self.user.key_items[i]
            lx = SCREEN_WIDTH - 200
            ly = SCREEN_HEIGHT - (100 + 64 * i+1)
            self.screen.blit(item.texture_size(self._secret_size), (lx, ly))

        if len(self.user.ammo_items) > 0:
            item = self.user.ammo_items[0]
            lx = SCREEN_WIDTH//2 + 200
            ly = SCREEN_HEIGHT - 75
            self.screen.blit(item.texture_size(self._ammo_size), (lx, ly))
            code_label = Fonts.font_ammo.render(str(len(self.user.ammo_items)), True, WHITE)
            self.screen.blit(code_label, (lx + self._ammo_size, ly + self._ammo_size//2))