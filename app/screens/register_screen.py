from app.constants.ui import *
from app.constants.settings import *
from app.constants.assets import *
from app.ui.input import Input
from app.ui.button import *
import app._utils.global_var as global_var
from app.ui.line import *
from app._utils.sounds import *

class RegisterScreen:

    def __init__(self, screen):
        self.screen = screen

        self.username_input = Input(
            placeholder="VOTRE NOM D'UTILISATEUR",
            x=100, y=self._get_y(0),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="NOM D'UTILISATEUR"
        )
        self.email_input = Input(
            placeholder="VOTRE EMAIL",
            x=100, y=self._get_y(1),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="EMAIL"
        )
        self.password_input = Input(
            placeholder="VOTRE MOT DE PASSE",
            x=100, y=self._get_y(2),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="MOT DE PASSE"
        )
        self.confirm_input = Input(
            placeholder="CONFIRMER LE MOT DE PASSE",
            x=100, y=self._get_y(3),
            input_w=ELEMENT_WIDTH_LARGE, h=ELEMENT_HEIGHT,
            label="CONFIRMER"
        )

        self.btn_create = Button(
            'CREER',
            ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL + ELEMENT_WIDTH_SMALL + GAP_BETWEEN_ELEMENT, self._get_y(4),
            ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT,
        )
        self.btn_back = Button(
            'RETOUR',
            ELEMENT_WIDTH_LARGE + GAP_BETWEEN_ELEMENT_LABEL, self._get_y(4),
            ELEMENT_WIDTH_SMALL, ELEMENT_HEIGHT,
            'danger'
        )

        self.line = Line(100, self._get_y(5), SEPARATOR_LINE_WIDTH)

        self.btn_login = Button(
            'CONNECTEZ VOUS',
            100, self._get_y(5) + GAP_BETWEEN_ELEMENT,
            ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT,
            'default', 'VOUS AVEZ UN COMPTE'
        )

    def _get_y(self, num):
        return 164 + ELEMENT_HEIGHT * num + GAP_BETWEEN_ELEMENT * num

    def handle_event(self, event):
        self.username_input.handle_event(event)
        self.email_input.handle_event(event)
        self.password_input.handle_event(event)
        self.confirm_input.handle_event(event)

        if self.btn_back.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'login'

        if self.btn_login.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'login'

        if self.btn_create.is_clicked(event):
            Sounds.click()
            self._handle_register()

    def _handle_register(self):
        username = self.username_input.value
        email    = self.email_input.value
        password = self.password_input.value
        confirm  = self.confirm_input.value

        if not username or not email or not password or not confirm:
            return
        if password != confirm:
            return

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(
            Assets.logo,
            (SCREEN_WIDTH / 2 - Assets.logo.get_width()  / 2,
             SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2)
        )

        self.username_input.draw(self.screen)
        self.email_input.draw(self.screen)
        self.password_input.draw(self.screen)
        self.confirm_input.draw(self.screen)

        self.btn_create.draw(self.screen)
        self.btn_back.draw(self.screen)

        self.line.draw(self.screen)

        self.btn_login.draw(self.screen)