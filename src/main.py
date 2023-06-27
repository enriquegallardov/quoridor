import configparser

import pygame
from pygame.locals import *

config = configparser.ConfigParser()
config.read("config/config.ini")

TILESIZE = int(config["TILESIZE"]["TILESIZE"])
WHITE = pygame.Color(config["COLORS"]["WHITE"])
BLACK = pygame.Color(config["COLORS"]["BLACK"])
MARGIN = TILESIZE / 8


class Board:
    """Board representation"""

    def __init__(self, screen):
        self.board = []
        self.background = self.draw_background(screen)

    def draw_background(self, screen):
        """Fill background"""
        background = pygame.Surface(screen.get_size()).convert()
        background.fill(BLACK)

        return background


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((TILESIZE * 41 / 4, TILESIZE * 41 / 4))
    pygame.display.set_caption("Quoridor")

    # Prepare game objects
    board = Board(screen)
    clock = pygame.time.Clock()

    # Event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(board.background, (0, 0))

        for row in range(9):
            for column in range(9):
                pygame.draw.rect(
                    screen,
                    WHITE,
                    [
                        (MARGIN + TILESIZE) * column + MARGIN,
                        (MARGIN + TILESIZE) * row + MARGIN,
                        TILESIZE,
                        TILESIZE,
                    ],
                )
        pygame.display.flip()


if __name__ == "__main__":
    main()
