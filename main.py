import pygame
import sys
from app.constants.settings import *
from app.constants.assets import *
from app.screens.home_screen import *
from app.screens.login_screen import *
from app.screens.register_screen import *
from app.screens.forgot_password_screen import *
from app.screens.new_password_screen import *
from app.screens.verify_code_screen import *
from app.screens.saves_screen import *
from app.core.game import *
from app.constants.fonts import *
from app.ui.button import *
import app._utils.global_var as global_var
from app.screens.routing import *
from app.screens.loading_screen import *
from app.screens.settings_screen import *
from app.screens.error_screen import *

pygame.init()
Sounds.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infected Prison")

Assets.load()
Fonts.load()

home_screen = HomeScreen(screen)
login_screen = LoginScreen(screen)
register_screen = RegisterScreen(screen)
forgot_password_screen = ForgotPasswordScreen(screen)
verify_code_screen = VerifyCodeScreen(screen)
new_password_screen = NewPasswordScreen(screen)
saves_screen = SavesScreen(screen)
game = Game(screen)
loading = LoadingScreen(screen)
settings = SettingsScreen(screen)
error_screen = ErrorScreen(screen)

routing = Routing(
    home_screen,
    login_screen,
    register_screen,
    forgot_password_screen,
    new_password_screen,
    saves_screen,
    verify_code_screen,
    loading,
    game,
    settings,
    error_screen
)


clock = pygame.time.Clock()

while global_var.running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global_var.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and global_var.current_page != 'game':
            global_var.running = False

        routing.handle_event(event)

    routing.route()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()