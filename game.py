import pygame
from ships import PlayerShip
from area import Area
from bullet import Bullet

class Game:
    def __init__(self, screen_w, screen_h):
        self.SCREEN_WIDTH = screen_w
        self.SCREEN_HEIGHT = screen_h

        self.screen = None
        self.setup_window()

        self.ship_surface = None
        self.bullet_surface = None
        self.load_surfaces()

        self.player_area = Area(0, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player_ship = PlayerShip(self.ship_surface, self.player_area, 5)

        self.bullet_area = Area(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.exit_window = False

    def load_surfaces(self):
        self.ship_surface = pygame.image.load("assets/ship.bmp").convert()
        self.bullet_surface = pygame.image.load("assets/ship.bmp").convert()
        self.bullet_surface.set_colorkey((0, 0, 0))
        self.bullet_surface = pygame.transform.scale(self.bullet_surface, (20, 30))

    def setup_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])

    def update(self):

        while not self.exit_window:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_window = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player_ship.get_bullet_no() < self.player_ship.max_bullets:
                        self.player_ship.bullets.append(Bullet(self.bullet_surface, self.bullet_area, self.player_ship))
            self.screen.fill((0, 0, 0))

            pressed_keys = pygame.key.get_pressed()
            self.player_ship.update(pressed_keys)
            self.screen.blit(self.player_ship.surf, self.player_ship.rect)

            for bullet in self.player_ship.bullets:
                bullet.update()
                if not bullet.in_area:
                    self.player_ship.bullets.remove(bullet)
                    del bullet
                else:
                    self.screen.blit(bullet.surf, bullet.rect)

            pygame.display.flip()

    def run(self):

        self.update()

        pygame.quit()