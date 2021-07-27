# coding=utf-8
"""
Sky Dodge Game Module.
"""
import pygame
from pygame.locals import *

from sky_dodge_game import SkyDodgeGame


def start(game):
    """  Start game method """
    screen = pygame.display.set_mode(game.display_size)
    game.set_screen(screen)
    pygame.display.set_caption(game.title())

    # Game Loop
    while game.running:
        # Update background
        game.fill_background(color=(135, 206, 250))
        # Event loop
        for event in pygame.event.get():
            # Key to exit
            if event.type == QUIT:
                game.running = False
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game.running = False
            else:
                game.check_events(event)

        # Update game info.
        game.update()
        # Update pygame screen.
        pygame.display.flip()


if __name__ == '__main__':
    pygame.mixer.init()
    pygame.init()
    try:
        start(SkyDodgeGame(display_size=(800, 600)))
    finally:
        # pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
