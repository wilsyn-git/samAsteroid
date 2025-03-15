# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from circleshape import *


def main():

    dt = 0

    print("Starting Asteroids!")
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0,0,0)
    screen.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt = (clock.tick(60))/1000



if __name__ == "__main__":
    main()
