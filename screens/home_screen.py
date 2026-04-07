from constants.ui import *
from settings import *
from constants.assets import *
from ui.button import *
import global_var

btn_connect = Button('SE CONNECTER', 650, SCREEN_HEIGHT-150, 460, 50)
btn_quit = Button('QUITTER LE JEU', 650, SCREEN_HEIGHT-150 + 62 , 460, 50, 'danger')

class HomeScreen:

    def __init__(self, screen):
        self.screen = screen

    def handle_event(self, event):
        if btn_connect.is_clicked(event):
            global_var.current_page = 'login'

        if btn_quit.is_clicked(event):
            global_var.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.home_title, (Assets.home_title.get_width() - SCREEN_PADDING, SCREEN_HEIGHT / 2 - Assets.home_title.get_height() / 2))
        self.screen.blit(Assets.logo, (SCREEN_PADDING, SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2))

        btn_connect.draw(self.screen)
        btn_quit.draw(self.screen)