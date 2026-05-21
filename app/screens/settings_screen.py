from app.constants.assets import *
import app._utils.global_var as global_var
from app.api.auth_api import *
from app.ui.button import *
from app._utils.sounds import *

class SettingsScreen:
    
    def __init__(self, screen):
        self.screen = screen
        
        self.delete_account_btn = Button(
            "Suppimer le compte",
            SCREEN_WIDTH//2-ELEMENT_WIDTH_LARGE//2,
            SCREEN_HEIGHT-SCREEN_PADDING-ELEMENT_HEIGHT,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
            'danger'
        )
        
        self.back_btn = Button(
            "Retour",
            SCREEN_WIDTH//2-ELEMENT_WIDTH_LARGE//2,
            SCREEN_HEIGHT-SCREEN_PADDING-ELEMENT_HEIGHT-ELEMENT_HEIGHT-20,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
        )
    
    def handle_event(self, event):
        if self.delete_account_btn.is_clicked(event):
            Sounds.click()
            res = AuthApi.delete_account()
            if res.status_code == 200:
                global_var.save_store.invalid_save_loaded()
                global_var.save_store.invalid_saves()
                global_var.user_store.invalid_maps()
                global_var.user_store.invalid_me()
                global_var.navigate_page('login')
        elif self.back_btn.is_clicked(event):
            global_var.navigate_page('saves')
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.delete_account_btn.draw(self.screen)
        self.back_btn.draw(self.screen)