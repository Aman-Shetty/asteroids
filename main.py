import pygame
from pygame.display import update
from constants import *
from player import Player

def main():
    pygame.init()
    disp = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)

        pygame.Surface.fill(disp, (0,0,0))
        for object in drawable:
            object.draw(disp)
        pygame.display.flip()
        dt = clock.tick(60) /1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
