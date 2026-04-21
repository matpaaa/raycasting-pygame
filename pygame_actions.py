import pygame
from pygame import Surface
from sounds import *
from user import User
from pygame.event import Event
from sounds import *
from sprite.sprite import *
from sprite.human_sprite import *

class PygameActions:

    _walk_sound = None
    _moving = False

    def __init__(self, user: User, screen: Surface):
        self.user = user
        self.screen = screen

    def user_move_left(self):
        self.user.move_left()

    def user_move_right(self):
        self.user.move_right()

    def user_move_up(self):
        self.user.move_up()

    def user_move_down(self):
        self.user.move_down()

    def actions(self, sprite: Sprite | None):
        keys = pygame.key.get_pressed()
        self._moving = False
        if keys[pygame.K_LEFT]:
            self.user_move_left()
        if keys[pygame.K_RIGHT]:
            self.user_move_right()
        if keys[pygame.K_UP]:
            self.user_move_up()
            self._moving = True
        if keys[pygame.K_DOWN]:
            self.user_move_down()
            self._moving = True

        if self._moving and self._walk_sound is None:
            self._walk_sound = Sounds.walk()
        elif not self._moving and self._walk_sound is not None:
            self._walk_sound.stop()
            self._walk_sound = None

        if keys[pygame.K_x]:
            self.user.damage(10)

        if keys[pygame.K_c]:
            self.user.heal(10)

        if keys[pygame.K_1]:
            self.user.handle_select_slot(0)

        if keys[pygame.K_2]:
            self.user.handle_select_slot(1)

        if keys[pygame.K_3]:
            self.user.handle_select_slot(2)

        if keys[pygame.K_4]:
            self.user.handle_select_slot(3)

        if (sprite is not None and keys[pygame.K_e]):
            if (isinstance(sprite, HumanSprite)):
                sprite.handle_interaction(self.screen)