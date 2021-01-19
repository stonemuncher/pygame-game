import pygame
from ships import PlayerShip
from area import Area

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
exit_window = False

test_area = Area(0, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
player_ship = PlayerShip(test_area)

while not exit_window:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_window = True

    pressed_keys = pygame.key.get_pressed()
    player_ship.update(pressed_keys)

    screen.fill((0, 0, 0))
    screen.blit(player_ship.surf, player_ship.rect)
    pygame.display.flip()

pygame.quit()