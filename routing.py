import global_var
from sounds import *

class Routing:

    _playing_sound_home = False
    _playing_sound_game = False
    
    def __init__(
            self,
            home_screen,
            login_screen,
            register_screen,
            forgot_password_screen,
            forgot_password_code_screen,
            new_password_screen,
            game
        ):

        self.home_screen = home_screen
        self.login_screen = login_screen
        self.register_screen = register_screen
        self.forgot_password_screen = forgot_password_screen
        self.forgot_password_code_screen = forgot_password_code_screen
        self.new_password_screen = new_password_screen

        self.game = game

    def load_sound(self):
        if global_var.current_page == 'game' and not self._playing_sound_game:
            Sounds.game()
            self._playing_sound_game = True
            self._playing_sound_home = False
        elif global_var.current_page != 'game' and not self._playing_sound_home:
            Sounds.home()
            self._playing_sound_home = True
            self._playing_sound_game = False

    def route(self):
        self.load_sound()

        if global_var.current_page == 'home':
            self.home_screen.draw()
            return
        elif global_var.current_page == 'login':
            self.login_screen.draw()
            return
        elif global_var.current_page == 'register':
            self.register_screen.draw()
            return
        elif global_var.current_page == 'forgot_password':
            self.forgot_password_screen.draw()
            return
        elif global_var.current_page == 'forgot_password_code':
            self.forgot_password_code_screen.draw()
            return
        elif global_var.current_page == 'new_password':
            self.new_password_screen.draw()
            return
        elif global_var.current_page == 'game':
            self.game.draw()
            return
        
    def handle_event(self, event):
        if global_var.current_page == 'home':
            self.home_screen.handle_event(event)
            return
        elif global_var.current_page == 'login':
            self.login_screen.handle_event(event)
            return
        elif global_var.current_page == 'register':
            self.register_screen.handle_event(event)
            return
        elif global_var.current_page == 'forgot_password':
            self.forgot_password_screen.handle_event(event)
            return
        elif global_var.current_page == 'forgot_password_code':
            self.forgot_password_code_screen.handle_event(event)
            return
        elif global_var.current_page == 'new_password':
            self.new_password_screen.handle_event(event)
            return
        elif global_var.current_page == 'game':
            self.game.handle_event(event)
            return