import pygame
import sys
from settings import *
from constants.assets import *
from screens.home_screen import *
from screens.login_screen import *
from screens.register_screen import *
from screens.forgot_password_screen import *
from screens.forgot_password_code_screen import *
from screens.new_password_screen import *
from constants.fonts import *
from ui.button import *
import global_var
from routing import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infected Prison")

Assets.load()
Fonts.load()

home_screen = HomeScreen(screen)
login_screen = LoginScreen(screen)
register_screen = RegisterScreen(screen)
forgot_password_screen = ForgotPasswordScreen(screen)
forgot_password_code_screen = ForgotPasswordCodeScreen(screen)
new_password_screen = NewPasswordScreen(screen)

routing = Routing(home_screen, login_screen, register_screen, forgot_password_screen, forgot_password_code_screen, new_password_screen)


pygame.mixer.music.load('./assets/sounds/home-music.mp3')
pygame.mixer.music.play(loops=-1)

clock = pygame.time.Clock()

while global_var.running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global_var.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            global_var.running = False

        routing.handle_event(event)

    routing.route()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()