from app.constants.ui import *
from app.constants.settings import *
from app.constants.assets import *
from app.ui.input import Input
from app.ui.button import *
import app._utils.global_var as global_var
from app.ui.line import *
from app._utils.sounds import *
from app.api.auth_api import *
from app.ui.error_bubble import *

class LoginScreen:

    def __init__(self, screen):
        self.screen = screen
        self.username_input = Input(
            placeholder="VOTRE NOM D'UTILISATEUR",
            x=100, y=self._get_y(0),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="NOM D'UTILISATEUR"
        )
        self.input_password = Input(
            placeholder="VOTRE MOT DE PASSE",
            x=100, y=self._get_y(1),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="MOT DE PASSE"
        )

        self.btn_back = Button('RETOUR', ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL, self._get_y(2), ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT, 'danger')
        self.btn_connect = Button('CONNEXION', ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL + ELEMENT_WIDTH_SMALL + GAP_BETWEEN_ELEMENT, self._get_y(2), ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT)

        self.line = Line(100, self._get_y(3), SEPARATOR_LINE_WIDTH)

        self.btn_forgot_password = Button('RECUPERER VOTRE MOT DE PASSE', 100, self._get_y(3) + GAP_BETWEEN_ELEMENT, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT, 'default', 'MOT DE PASSE OUBLIE')
        self.btn_create_account = Button('CREER VOTRE COMPTE', 100, self._get_y(4) + GAP_BETWEEN_ELEMENT, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT, 'default', 'VOUS ETES NOUVEAU ?')

        self.error_bubble = ErrorBubble(self.screen)

    def handle_event(self, event):
        self.username_input.handle_event(event)
        self.input_password.handle_event(event)
        self.error_bubble.handle_event(event)

        if self.btn_back.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'home'

        if self.btn_connect.is_clicked(event):
            # Sounds.click()
            # global_var.current_page = 'game'

            data = {
                "name": self.username_input.value,
                "password": self.input_password.value
            }
            res = AuthApi.login(data)
            if res.status_code == 200:
                global_var.current_page = 'saves'
            else:
                self.error_bubble.set_content('Username ou mot de passe invalide')

        if self.btn_forgot_password.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'forgot_password'

        if self.btn_create_account.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'register'

    def _get_y(self, num):
        return 164 + ELEMENT_HEIGHT*num + GAP_BETWEEN_ELEMENT*num

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(Assets.logo, (SCREEN_WIDTH/2 - Assets.logo.get_width()/2, SCREEN_HEIGHT/2 - Assets.logo.get_height()/2))

        self.username_input.draw(self.screen)
        self.input_password.draw(self.screen)

        self.btn_back.draw(self.screen)
        self.btn_connect.draw(self.screen)

        self.line.draw(self.screen)

        self.btn_forgot_password.draw(self.screen)
        self.btn_create_account.draw(self.screen)

        self.error_bubble.draw()