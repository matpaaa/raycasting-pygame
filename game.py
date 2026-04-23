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

class Game:
    
    def __init__(self, screen):
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

    def handle_event(self, event: Event):
        self.event = event

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)
        self.ray_casting.launch_fucking_rays(self.user)
        self.ray_casting.draw_sprites(self.user)
        self.pygame_actions.actions(self.sprite_interact, self.event)
        self.user.handle_effect()
        self.user.draw_item_select(self.screen)
        self.minimap.draw()
        self.health.draw()
        self.inventory.draw()
        self.sprite_interact = self.interaction.handle_interaction()
        self.effect.draw()