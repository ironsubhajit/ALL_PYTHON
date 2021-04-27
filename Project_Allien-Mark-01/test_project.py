import sys
import pygame


def run_game():
    # Initialize game & create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("test")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"event is -> {event.key}")
        pygame.display.flip()


run_game()