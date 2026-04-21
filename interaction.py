from pygame import Surface
from user import *
from sprite.human_sprite import *
from constants.fonts import *
from constants.color import *
from constants.ui import *
from settings import *
from sprite.object_sprite import *

class Interaction:

    def __init__(self, screen: Surface, user: User):
        self.screen = screen
        self.user = user

        self.label_surf = Fonts.font_btn.render('Appuyier sur E pour intéragir', True, BUTTON_WHITE)
        self.label_w = 400 + GAP_BETWEEN_ELEMENT_LABEL
        self.label_rect = pygame.Rect(SCREEN_WIDTH//2 - 400//2, SCREEN_HEIGHT - 150, self.label_w, 50)

    def handle_interaction(self):
        sprite = self.user.sprite_interaction()
        if sprite is not None:
            if isinstance(sprite, HumanSprite) or isinstance(sprite, ObjectSprite):
                lx = self.label_rect.centerx - self.label_surf.get_width() // 2
                ly = self.label_rect.centery - self.label_surf.get_height() // 2
                self.screen.blit(self.label_surf, (lx, ly))
                return sprite
