from map import MAP
from pygame_actions import PygameActions
from ray_casting import RayCasting
from minimap import Minimap
from settings import DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, FPS, SCREEN_BACKGROUND, SCREEN_HEIGHT, SCREEN_WIDTH
from user import User
from health import *
from inventory import *

class Game:
    
    def __init__(self, screen):
        self.screen = screen

        self.user = User(DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, MAP)
        self.health = Health(self.user, self.screen)
        self.inventory = Inventory(self.user, self.screen)
        self.ray_casting = RayCasting(screen, MAP, self.user)
        self.minimap = Minimap(screen, MAP, self.user)
        self.pygame_actions = PygameActions(self.user)

    def draw(self):
        self.pygame_actions.actions()
        self.screen.fill(SCREEN_BACKGROUND)
        self.ray_casting.launch_fucking_rays(self.user)
        self.ray_casting.draw_sprites(self.user)
        self.minimap.draw()
        self.health.draw()
        self.inventory.draw()