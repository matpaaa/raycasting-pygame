from map import MAP
import pygame
import math
from pygame_actions import PygameActions
from ray_casting import RayCasting
from minimap import Minimap
from user import User


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    clock = pygame.time.Clock()
    running = True


    user = User(1, 1, math.pi / 4, MAP)
    ray_casting = RayCasting(screen, MAP)
    minimap = Minimap(screen, MAP, user)
    pygame_actions = PygameActions(user)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame_actions.actions(event)

        screen.fill("black")
        ray_casting.launch_fucking_rays(user)
        minimap.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()