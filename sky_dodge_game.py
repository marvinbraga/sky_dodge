# coding=utf-8
"""
Sky Dodge Game
"""
import os

import pygame

from abstract_game import AbstractGame
from cloud import Cloud
from enemy import Enemy
from player import Player


class SkyDodgeGame(AbstractGame):
    """ Sky Dodge Class """

    def __init__(self, display_size):
        self._display_size = display_size
        super(SkyDodgeGame, self).__init__(display_size)
        # Player
        self._player = Player(display_size)
        # sprite groups
        self._enemies = pygame.sprite.Group()
        self._clouds = pygame.sprite.Group()
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self._player)
        # events
        self.ADD_ENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADD_ENEMY, 250)
        self.ADD_CLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADD_CLOUD, 1000)
        # load background music
        background_music = os.path.join(os.path.dirname(__file__), os.path.normpath('./sound/Sky_dodge_theme.ogg'))
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.play(loops=1)
        pygame.mixer.music.set_volume(0.3)

    def title(self):
        """ Return game title. """
        return 'Sky Dodge Game'

    def update(self, **kwargs):
        """ Method to update de zelda game. """
        create_enemies = kwargs.get('create_enemies')
        create_clouds = kwargs.get('create_clouds')
        if create_enemies:
            self.create_enemies(create_enemies)
        if create_clouds:
            self.create_clouds(create_clouds)

        self._all_sprites.draw(self.screen)

        self._clouds.update()
        self._player.update(pressed_keys=pygame.key.get_pressed())
        self._enemies.update()

        # Check collision
        if pygame.sprite.spritecollideany(self._player, self._enemies):
            self._player.kill()
            self._player.sound_effect()
            self.running = False
        return self

    def create_enemies(self, create_enemies):
        """ Create instance of enemy """
        for i in range(create_enemies):
            enemy = Enemy(self._display_size)
            self._enemies.add(enemy)
            self._all_sprites.add(enemy)
        return self

    def create_clouds(self, create_clouds):
        """ Create instance of cloud """
        for i in range(create_clouds):
            cloud = Cloud(self._display_size)
            self._clouds.add(cloud)
            self._all_sprites.add(cloud)
        return self
