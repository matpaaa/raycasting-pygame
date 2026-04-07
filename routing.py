import global_var

class Routing:
    
    def __init__(self, home_screen, login_screen):
        self.home_screen = home_screen
        self.login_screen = login_screen
        

    def route(self):
        if global_var.current_page == 'home':
            self.home_screen.draw()
        elif global_var.current_page == 'login':
            self.login_screen.draw()