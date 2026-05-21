from app.constants.ui import *
from app.constants.settings import *
from app.constants.assets import *
from app.ui.input import *
from app.ui.button import *
import app._utils.global_var as global_var
from app.ui.line import *
from app._utils.sounds import *
from app.api.auth_api import *

class ForgotPasswordScreen:
    def __init__(self, screen):
        self.screen = screen

        self.input_email = Input(
            'ENTRER VOTRE EMAIL',
            100, 300,
            ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT,
            "ENTRER VOTRE EMAIL"
        )

        self.btn_back = Button(
            "RETOUR",
            ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL,
            300 + ELEMENT_HEIGHT + GAP_BETWEEN_ELEMENT,
            ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT,
            'danger'
        )

        self.btn_confirm = Button(
            "CONFIRMER",
            ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL + GAP_BETWEEN_ELEMENT + ELEMENT_WIDTH_SMALL,
            300 + ELEMENT_HEIGHT + GAP_BETWEEN_ELEMENT,
            ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT
        )

    def handle_event(self, event):
        self.input_email.handle_event(event)

        if self.btn_back.is_clicked(event):
            Sounds.click()
            global_var.navigate_page('login')
        if self.btn_confirm.is_clicked(event):
            self.btn_confirm.is_loading = True
            Sounds.click()
            email = self.input_email.value
            res = AuthApi.forgot_password({
                'email': email
            })
            
            if res.status_code == 200:
                global_var.verify_code_email = email
                global_var.navigate_page('verify_code')
            self.btn_confirm.is_loading = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(
            Assets.logo,
            (SCREEN_WIDTH / 2 - Assets.logo.get_width()  / 2,
             SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2)
        )

        self.input_email.draw(self.screen)
        self.btn_back.draw(self.screen)
        self.btn_confirm.draw(self.screen)