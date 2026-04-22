import pygame
from pygame import Surface
from sounds import *
from user import User
from pygame.event import Event
from sounds import *
from sprite.sprite import *
from sprite.human_sprite import *
from sprite.object_sprite import *

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

    def actions(self, sprite: Sprite | None, event: Event | None):
        keys = pygame.key.get_pressed()
        self._moving = False
        
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.user_move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.user_move_right()
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.user_move_up()
            self._moving = True
        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
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

        if keys[pygame.K_1] or keys[pygame.K_AMPERSAND]:
            self.user.handle_select_slot(0)

        if keys[pygame.K_2]:
            self.user.handle_select_slot(1)

        if event and event.type == pygame.TEXTINPUT:
            if event.text == 'é':
                self.user.handle_select_slot(1)

        if keys[pygame.K_3]:
            self.user.handle_select_slot(2)

        if keys[pygame.K_4]:
            self.user.handle_select_slot(3)

        if keys[pygame.K_e]:
            if (sprite is not None):
                if isinstance(sprite, HumanSprite):
                    sprite.handle_interaction(self.screen)
                elif isinstance(sprite, ObjectSprite):
                    sprite.handle_interaction(self.user)

            else:
                self.user.use_item()

        if keys[pygame.K_SPACE]:
            self.user.handle_shoot()