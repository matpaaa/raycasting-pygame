from map import MAP
import pygame
import math
from pygame_actions import PygameActions
from ray_casting import RayCasting
from minimap import Minimap
from settings import DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, FPS, SCREEN_BACKGROUND, SCREEN_HEIGHT, SCREEN_WIDTH
from user import User


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    user = User(DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, MAP)
    ray_casting = RayCasting(screen, MAP, user)
    minimap = Minimap(screen, MAP, user)
    pygame_actions = PygameActions(user)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame_actions.actions(event)

        screen.fill(SCREEN_BACKGROUND)
        ray_casting.launch_fucking_rays(user)
        minimap.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()