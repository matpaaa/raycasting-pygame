from constants.ui import *
from settings import *
from constants.assets import *
from ui.input import *
from ui.button import *
import global_var
from ui.line import *
from sounds import *
from ui.text import *
from constants.color import *

class ForgotPasswordCodeScreen:

    def __init__(self, screen):
        self.screen = screen

        self.title = Text(
            "CONFIRMER VOTRE EMAIL",
            'center',
            224,
            WHITE,
            'title'
        )

        self.subtitle_1 = Text(
            "NOUS AVONS ENVOYÉ UN CODE DE VALIDATION.",
            'center',
            270,
            TEXT_GRAY,
            'subtitle'
        )

        self.subtitle_2 = Text(
            "SI VOUS NE TROUVEZ PAS LE MESSAGE, VÉRIFIEZ DANS VOS DOSSIERS DE SPAM.",
            'center',
            300,
            TEXT_GRAY,
            'subtitle'
        )

        self.input_code = Input(
            'ENTRER LE CODE',
            SCREEN_WIDTH/2 - ELEMENT_WIDTH_LARGE/2,
            348,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT
        )

        self.btn_back = Button(
            'BACK',
            SCREEN_WIDTH/2 - GAP_BETWEEN_ELEMENT/2 - ELEMENT_WIDTH_SMALL,
            368 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )

        self.btn_confirm = Button(
            'VALIDER',
            SCREEN_WIDTH/2 + GAP_BETWEEN_ELEMENT/2,
            368 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT
        )

    def handle_event(self, event):
        self.input_code.handle_event(event)

        if self.btn_back.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'forgot_password'

        if self.btn_confirm.is_clicked(event):
            Sounds.click()
            global_var.current_page = 'new_password'

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(
            Assets.logo,
            (SCREEN_WIDTH / 2 - Assets.logo.get_width()  / 2,
             SCREEN_HEIGHT / 2 - Assets.logo.get_height() / 2)
        )
        self.screen.blit(Assets.window, ((SCREEN_WIDTH - Assets.window.get_width()) / 2, (SCREEN_HEIGHT - Assets.window.get_height()) / 2))
        self.title.draw(self.screen)

        self.subtitle_1.draw(self.screen)
        self.subtitle_2.draw(self.screen)
        self.input_code.draw(self.screen)
        self.btn_back.draw(self.screen)
        self.btn_confirm.draw(self.screen)
        