from pygame_actions import PygameActions
from ray_casting import RayCasting
from minimap import Minimap
from settings import DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, FPS, SCREEN_BACKGROUND, SCREEN_HEIGHT, SCREEN_WIDTH
from user import User
from health import *
from inventory import *
from sprite.human_sprite import *
from interaction import *
from effect import *
from pygame.event import Event
from map_config import *
from mock.map_mocked import *
from pygame import Surface
from ui.button import *
import global_var

class Game:
    
    def __init__(self, screen: Surface):
        self.screen = screen

        self.map_config = MapConfig(MAP_MOCKED, MAP_SPRITES_MOCKED, MAP_TEXTURES_MOCKED)
        self.map_config.load_textures()

        # Load sprite image
        for sprite in self.map_config.sprites:
            sprite.load()

        self.user = User(DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, self.map_config)
        self.health = Health(self.user, self.screen)
        self.inventory = Inventory(self.user, self.screen)
        self.ray_casting = RayCasting(screen, self.user, self.map_config)
        self.minimap = Minimap(screen, self.user, self.map_config)
        self.pygame_actions = PygameActions(self.user, self.screen)
        self.interaction = Interaction(self.screen, self.user)
        self.effect = Effect(self.screen, self.user)

        self.sprite_interact = None
        self.event = None

        self.btn_back_menu = Button('RETOUR AU MENU', SCREEN_WIDTH//2 - ELEMENT_WIDTH_LARGE//2, SCREEN_HEIGHT - 150, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT)
        self.dead_sound = None

    def handle_event(self, event: Event):
        self.event = event

        if self.btn_back_menu.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'home'

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)
        self.ray_casting.launch_fucking_rays(self.user)
        self.ray_casting.draw_sprites(self.user)

        self.user.handle_effect()
        self.user.draw_item_select(self.screen)
        self.minimap.draw()
        self.health.draw()
        self.inventory.draw()
        self.sprite_interact = self.interaction.handle_interaction()
        self.effect.draw()

        if not self.user.is_dead and not self.user.has_win:
            self.pygame_actions.actions(self.sprite_interact, self.event)

        if self.user.is_dead:
            if self.dead_sound is None:
                self.dead_sound = Sounds.dead()
            overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            overlay.fill((255, 56, 60, 255*0.3))
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(Assets.dead_screen, (SCREEN_WIDTH//2 - Assets.dead_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.dead_screen.get_height()//2))
            self.btn_back_menu.draw(self.screen)
        elif self.user.has_win:
            overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            overlay.fill((52, 199, 89, 255*0.3))
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(Assets.win_screen, (SCREEN_WIDTH//2 - Assets.win_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.win_screen.get_height()//2))
            self.btn_back_menu.draw(self.screen)