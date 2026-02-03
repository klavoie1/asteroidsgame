import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():

    dt = 0
    running = True

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()

    while (running == True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)



    


if __name__ == "__main__":
    main()
