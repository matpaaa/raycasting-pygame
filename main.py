import pygame
import sys
from settings import *
from constants.assets import *
from screens.home_screen import *
from screens.login_screen import *
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

routing = Routing(home_screen, login_screen)


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

        home_screen.handle_event(event)
        login_screen.handle_event(event)

    routing.route()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()