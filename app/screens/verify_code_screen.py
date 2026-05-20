from app.constants.ui import *
from app.constants.settings import *
from app.constants.assets import *
from app.ui.input import *
from app.ui.button import *
import app._utils.global_var as global_var
from app.ui.line import *
from app._utils.sounds import *
from app.ui.text import *
from app.constants.color import *
from app.api.auth_api import *

class VerifyCodeScreen:

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
            global_var.navigatePage(global_var.last_page)

        if self.btn_confirm.is_clicked(event):
            Sounds.click()
            res = AuthApi.verify_code({
                'code': self.input_code.value,
                'email': global_var.verify_code_email
            })
            if res.status_code == 200:
                if global_var.last_page == 'register':
                    global_var.verify_code_email = None
                    global_var.navigatePage('login')
                else:
                    global_var.navigatePage('new_password')

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
        