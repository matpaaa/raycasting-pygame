from constants.ui import *
from settings import *
from constants.assets import *
from ui.input import *
from ui.button import *
import global_var
from sounds import *

class NewPasswordScreen:

    def __init__(self, screen):
        self.screen = screen

        self.input_password = Input(
            'NOUVEAU MOT DE PASSE',
            100,
            300,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
            'NOUVEAU'
        )
        self.input_password_confirm = Input(
            'CONFIRMER LE MOT DE PASSE',
            100,
            300 + ELEMENT_HEIGHT + GAP_BETWEEN_ELEMENT,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
            'CONFIRMER'
        )
        self.btn_submit = Button(
            'CONFIRMER',
            ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL,
            300 + ELEMENT_HEIGHT*2 + GAP_BETWEEN_ELEMENT*2,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT
        )

    def handle_event(self, event):
        self.input_password.handle_event(event)
        self.input_password_confirm.handle_event(event)

        if self.btn_submit.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'login'

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(
            Assets.logo,
            (SCREEN_WIDTH / 2 - Assets.logo.get_width()  / 2,
             SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2)
        )

        self.input_password.draw(self.screen)
        self.input_password_confirm.draw(self.screen)
        self.btn_submit.draw(self.screen)