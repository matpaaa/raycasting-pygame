from map.map import MAP
from pygame_actions import PygameActions
from ray_casting import RayCasting
from minimap import Minimap
from settings import DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, FPS, SCREEN_BACKGROUND, SCREEN_HEIGHT, SCREEN_WIDTH
from user import User
from health import *
from inventory import *
from map.map_sprites import *
from sprite.human_sprite import *
from interaction import *

class Game:
    
    def __init__(self, screen):
        self.screen = screen

        # Load sprite image
        for i in range(0, len(MAP_SPRITES)):
            MAP_SPRITES[i].load()

        self.user = User(DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, MAP, MAP_SPRITES)
        self.health = Health(self.user, self.screen)
        self.inventory = Inventory(self.user, self.screen)
        self.ray_casting = RayCasting(screen, MAP, self.user, MAP_SPRITES)
        self.minimap = Minimap(screen, MAP, self.user)
        self.pygame_actions = PygameActions(self.user, self.screen)
        self.interaction = Interaction(self.screen, self.user)

        self.sprite_interact = None

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)
        self.ray_casting.launch_fucking_rays(self.user)
        self.ray_casting.draw_sprites(self.user)
        self.pygame_actions.actions(self.sprite_interact)
        self.minimap.draw()
        self.health.draw()
        self.inventory.draw()
        self.sprite_interact = self.interaction.handle_interaction()