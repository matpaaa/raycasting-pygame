import pygame

from user import User
from pygame.event import Event

class PygameActions:
    def __init__(self, user: User):
        self.user = user

    def user_move_left(self):
        self.user.move_left()

    def user_move_right(self):
        self.user.move_right()

    def user_move_up(self):
        self.user.move_up()

    def user_move_down(self):
        self.user.move_down()

    def actions(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.user_move_left()
            if event.key == pygame.K_RIGHT:
                self.user_move_right()
            if event.key == pygame.K_UP:
                self.user_move_up()
            if event.key == pygame.K_DOWN:
                self.user_move_right()