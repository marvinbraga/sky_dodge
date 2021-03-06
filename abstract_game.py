# coding=utf-8
"""
Abstract Game Module
"""
from abc import ABCMeta, abstractmethod

import pygame


class AbstractGame(metaclass=ABCMeta):
    """ Class main to game Zelda """

    def __init__(self, display_size):
        self._display_size = display_size
        self.running = True
        self._screen = None
        self.timer = pygame.time.Clock()
        self.background = None

    @property
    def display_size(self):
        """ Return tuple with display size. """
        return self._display_size

    def set_screen(self, value):
        """
        Set pygame screen
        :param value: pygame screen
        :return: self
        """
        self._screen = value
        return self

    @property
    def screen(self):
        """ Return screen """
        return self._screen

    @property
    @abstractmethod
    def title(self):
        """ Get title to window screen. """
        pass

    def fill_background(self, color=(0, 0, 0)):
        """ Update background. """
        self.timer.tick(60)
        self._screen.fill(color)
        if self.background:
            self._screen.blit(self.background, (0, 0))
        return self

    @abstractmethod
    def update(self):
        """ Method to update game history. """
        pass

    @abstractmethod
    def check_events(self, event):
        """ Method to check events updates. """
        pass
