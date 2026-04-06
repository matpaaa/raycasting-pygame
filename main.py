import pygame
import sys
from settings import *
from constants.assets import *
from screens.home_screen import *
from constants.fonts import *
from ui.button import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infected Prison")

Assets.load()
Fonts.load()

homeScreen = HomeScreen(screen)

clock = pygame.time.Clock()

current_page = 'home'

btn_connect = Button('SE CONNECTER', 650, SCREEN_HEIGHT-150, 460, 50)
btn_quit = Button('QUITTER LE JEU', 650, SCREEN_HEIGHT-150 + 62 , 460, 50, 'danger')

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if btn_connect.is_clicked(event):
            print('clic')

        if btn_quit.is_clicked(event):
            running = False

    if current_page == 'home':
        homeScreen.draw()
        btn_connect.draw(screen)
        btn_quit.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()