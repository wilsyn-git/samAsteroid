# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    dt = 0

    print("Starting Asteroids!")
        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        
        
        dt = (clock.tick(60))/1000
        

if __name__ == "__main__":
    main()
