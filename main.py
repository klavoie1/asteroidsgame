import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_state, log_event
from player import Player
from shot import Shot

def main():

    pygame.init()

    dt = 0
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x, y)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while (running == True):
        log_state()
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()
        pygame.display.flip()


if __name__ == "__main__":
    main()
