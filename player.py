# coding=utf-8
"""
Player Module
"""

import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)

from settings import FileUtil


class Player(pygame.sprite.Sprite):
    """ Player Class. """

    def __init__(self, display_size):
        super(Player, self).__init__()
        self._display_size = display_size
        img = FileUtil('./images/planes.png').get()
        rect = (10, 28, 81, 50)
        self.image = pygame.image.load(img).subsurface(rect)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.move_up_sound = pygame.mixer.Sound(FileUtil('./sound/Jet_up.ogg').get())
        self.move_up_sound.set_volume(0.4)
        self.move_down_sound = pygame.mixer.Sound(FileUtil('./sound/Jet_down.ogg').get())
        self.move_down_sound.set_volume(0.4)
        self.collision_sound = pygame.mixer.Sound(FileUtil('./sound/Boom.ogg').get())
        self.collision_sound.set_volume(1)

    def sound_effect(self):
        """ Execute sound effect """
        self.move_up_sound.stop()
        self.move_down_sound.stop()
        pygame.time.delay(50)
        self.collision_sound.play()
        pygame.time.delay(500)

    def move(self, pressed_keys):
        """ Set _player movement """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            self.move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            self.move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        self.check_limits()

        return self

    def check_limits(self):
        """ Check borders limits to _player """
        if self.rect.left <= 0:
            self.rect.left = 1
        if self.rect.top <= 0:
            self.rect.top = 1
        if self.rect.right >= self._display_size[0]:
            self.rect.right = self._display_size[0] - 1
        if self.rect.bottom >= self._display_size[1]:
            self.rect.bottom = self._display_size[1] - 1
        return self

    def update(self, *args, **kwargs) -> None:
        """ Update """
        pressed_keys = kwargs.get('pressed_keys')
        if pressed_keys:
            self.move(pressed_keys)
