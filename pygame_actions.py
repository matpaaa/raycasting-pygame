import pygame
from pygame import Surface
from sounds import *
from user import User
from pygame.event import Event
from sounds import *
from sprite.sprite import *
from sprite.human_sprite import *
from sprite.object_sprite import *
from sprite.door_sprite import *
import time
from sprite.collision_sprite import *

class PygameActions:

    _walk_sound = None
    _moving = False
    _min_time_action_e = 1
    _min_time_action_l = 0.3
    _last_action = None
    _last_action_light = None

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

        if event is not None and event.type == pygame.KEYUP:
            if sprite is not None and isinstance(sprite, HumanSprite):
                if event.key == pygame.K_e:
                    sprite.interaction_released()

        if keys[pygame.K_q]:
            self.user_move_left()
        if keys[pygame.K_d]:
            self.user_move_right()
        if keys[pygame.K_z]:
            self.user_move_up()
            self._moving = True
        if keys[pygame.K_s]:
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

                    if keys[pygame.K_RIGHT]:
                        sprite.next_dialog()
                    elif keys[pygame.K_LEFT]:
                        sprite.previous_dialog()

                elif isinstance(sprite, ObjectSprite):
                    sprite.handle_interaction(self.user)
                elif isinstance(sprite, CollisionSprite):
                    if self._last_action is None or time.time() - self._last_action >= self._min_time_action_e:
                        self._last_action = time.time()
                        sprite.handle_open(self.user)

            else:
                self.user.use_item()

        if keys[pygame.K_SPACE]:
            self.user.handle_shoot()

        if keys[pygame.K_l]:
            if self._last_action_light is None or time.time() - self._last_action_light >= self._min_time_action_l:
                self._last_action_light = time.time()
                self.user.toogle_light()