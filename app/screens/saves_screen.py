import pygame
from app.constants.assets import *
from app.ui.button import *
from app.constants.settings import *
import app._utils.global_var as global_var
from app.api.auth_api import *

class SavesScreen:
    
    def __init__(self, screen):
        self.screen = screen
        self.disconnect_btn = Button('DECONNEXION', SCREEN_WIDTH-ELEMENT_WIDTH_SMALL-SCREEN_PADDING, 64, ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT, 'danger')
        
        self.start_game_x = SCREEN_WIDTH//2-Assets.start_game.get_width()//2
        self.start_game_y = SCREEN_HEIGHT//2-Assets.start_game.get_height()//2
        self.start_game_w = Assets.start_game.get_width()
        self.start_game_h = Assets.start_game.get_height()
        self.start_game_rect = pygame.Rect(self.start_game_x, self.start_game_y, self.start_game_w, self.start_game_h)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.start_game_rect.collidepoint(event.pos):
            global_var.navigatePage('game')
            
        if self.disconnect_btn.is_clicked(event):
            res = AuthApi.logout()
            if res.status_code == 200:
                global_var.navigatePage('login')
        
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        
        self.disconnect_btn.draw(self.screen)
        self.screen.blit(Assets.arrow_left, (23, SCREEN_HEIGHT//2-Assets.arrow_left.get_height()//2))
        self.screen.blit(Assets.arrow_right, (SCREEN_WIDTH-23-Assets.arrow_right.get_width(), SCREEN_HEIGHT//2-Assets.arrow_right.get_height()//2))
        self.screen.blit(Assets.start_game, (self.start_game_x, self.start_game_y))