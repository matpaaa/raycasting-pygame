from map import MAP
import pygame
import math
from pygame_actions import PygameActions
from ray_casting import RayCasting
from user import User

pygame.init()

SCREEN_SIZE = 500

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
running = True


user = User(1, 1, math.pi / 4)
ray_casting = RayCasting(screen, MAP)
pygame_actions = PygameActions(user)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame_actions.actions(event)

    screen.fill("black")
    ray_casting.launch_fucking_rays(user)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()