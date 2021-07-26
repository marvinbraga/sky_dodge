# coding=utf-8
"""
Cloud Module
"""
import random

import pygame
from pygame.locals import RLEACCEL

from settings import FileUtil


class Cloud(pygame.sprite.Sprite):
    """ Cloud Class """

    def __init__(self, display_size):
        super(Cloud, self).__init__()
        self.display_size = display_size
        img = FileUtil('./images/cloud.png').get()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(display_size[0] + 20, display_size[0] + 100),
                random.randint(0, display_size[1]),
            )
        )
        self.speed = random.randint(5, 7)

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
