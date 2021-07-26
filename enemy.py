# coding=utf-8
"""
Enemy Module
"""
import random

import pygame
from pygame.locals import RLEACCEL

from settings import FileUtil


class Enemy(pygame.sprite.Sprite):
    """ Enemy class """

    def __init__(self, display_size):
        super(Enemy, self).__init__()
        self.display_size = display_size
        img = FileUtil('./images/missile.png').get()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(display_size[0] + 20, display_size[0] + 100),
                random.randint(0, display_size[1]),
            )
        )
        self.speed = random.randint(5, 20)

    def move(self):
        """ Set _player movement """
        self.rect.move_ip(-self.speed, 0)
        self.check_limits()

        return self

    def check_limits(self):
        """ Check borders limits to _player """
        if self.rect.left < 0 - self.rect.width:
            self.kill()
        return self

    def update(self, *args, **kwargs) -> None:
        """ Update """
        self.move()
