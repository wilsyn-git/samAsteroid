# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from circleshape import *
from player import *


def main():

    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    dt = 0

    print("Starting Asteroids!")
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen) 


        player.update(dt)

        pygame.display.flip()
        
        
        dt = (clock.tick(60))/1000
        

if __name__ == "__main__":
    main()
