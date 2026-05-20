import app._utils.global_var as global_var
from app.ui.button import *
from app.ui.text import *
from app.constants.settings import *
from app.constants.color import *
from app.constants.fonts import *
from app.constants.assets import *

class ErrorScreen:
    
    def __init__(self, screen):
        self.screen = screen
        
        self.back_btn = Button(
            'Retour au menu',
            SCREEN_WIDTH//2-ELEMENT_WIDTH_LARGE//2,
            SCREEN_HEIGHT-SCREEN_PADDING-ELEMENT_HEIGHT,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT
        )
        
        self.title = Text("Une erreur c'est produite", 'center', 100, WHITE, 'title')
    
    def handle_event(self, event):
        if self.back_btn.is_clicked(event):
            global_var.navigate_page('saves')
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.back_btn.draw(self.screen)
        self.title.draw(self.screen)