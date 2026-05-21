from app.constants.assets import *
from app.constants.settings import *

class LoadingScreen:
    
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.loading, (SCREEN_WIDTH//2-Assets.loading.get_width()//2, SCREEN_HEIGHT//2-Assets.loading.get_height()//2))