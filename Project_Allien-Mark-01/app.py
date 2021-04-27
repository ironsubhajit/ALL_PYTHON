import pygame
from pygame.sprite import Group
from settings_alien_invasion import setting
from game_stats import GameStats as gS
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game & create a screen object.
    pygame.init()
    ai_settings = setting.Settings()
    screen = pygame.display.set_mode((ai_settings.screenWidth, ai_settings.screenHeight))
    pygame.display.set_caption("🛸Alien Invasion🛸")

    # Create an instance to store game statistics.
    stats = gS(ai_settings)

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
