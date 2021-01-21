import pygame
from ships import PlayerShip
from ships import AlienShip
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
        self.alien_surface = None
        self.alien_mask = None
        self.alien_red = None
        self.alien_orange = None
        self.alien_green = None

        self.load_surfaces()

        self.player_area = Area(0, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player_ship = PlayerShip(self.ship_surface, self.player_area, 5)

        self.bullet_area = Area(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.alien_area = Area(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.alien_ships = []
        self.alien_delay = 1000
        self.alien_spawn_event = pygame.USEREVENT + 1

        self.score = 0
        self.exit_window = False

    def load_surfaces(self):
        self.ship_surface = pygame.image.load("assets/ship.bmp").convert()
        self.bullet_surface = pygame.image.load("assets/ship.bmp").convert()
        self.bullet_surface.set_colorkey((0, 0, 0))
        self.bullet_surface = pygame.transform.scale(self.bullet_surface, (20, 30))
        self.alien_surface = pygame.image.load("assets/alien.png").convert_alpha()
        self.alien_surface = pygame.transform.scale(self.alien_surface, (75, 75))

        self.alien_mask = pygame.Surface(self.alien_surface.get_size()).convert_alpha()
        self.alien_red = self.alien_mask.copy()
        self.alien_orange = self.alien_mask.copy()
        self.alien_green = self.alien_mask.copy()

        self.alien_red.fill((255, 0, 0))
        self.alien_orange.fill((255, 140, 0))
        self.alien_green.fill((0, 255, 0))

    def setup_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])

    def spawn_alien(self):
        # print("Spawned alien")
        self.alien_ships.append(AlienShip(self.alien_surface, self.alien_area, 3))

    def update(self):
        self.screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()
        self.player_ship.update(pressed_keys)
        self.screen.blit(self.player_ship.surf, self.player_ship.rect)

        for bullet in self.player_ship.bullets:
            bullet.update()
            if not bullet.alive:
                self.player_ship.bullets.remove(bullet)
                del bullet
            else:
                self.screen.blit(bullet.surf, bullet.rect)

        for alien in self.alien_ships:
            if not alien.update(self.player_ship.bullets):
                pygame.display.set_caption(
                    f"GAME OVER!")
                pygame.time.wait(3000)
                self.exit_window = True
            if not alien.alive:
                self.score += 1
                self.alien_ships.remove(alien)
                del alien
                # print("killed alien ship")
            else:
                final_surf = alien.surf.copy()
                if alien.health == 3:
                    final_surf.blit(self.alien_red, (0, 0), special_flags=pygame.BLEND_MULT)
                elif alien.health == 2:
                    final_surf.blit(self.alien_orange, (0, 0), special_flags=pygame.BLEND_MULT)
                else:
                    final_surf.blit(self.alien_green, (0, 0), special_flags=pygame.BLEND_MULT)
                self.screen.blit(final_surf, alien.rect)
        pygame.display.flip()

    def run(self, fps):
        pygame.time.set_timer(self.alien_spawn_event, self.alien_delay)
        fps_clock = pygame.time.Clock()
        while not self.exit_window:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_window = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player_ship.get_bullet_no() < self.player_ship.max_bullets:
                        self.player_ship.bullets.append(Bullet(self.bullet_surface, self.bullet_area, self.player_ship))
                if event.type == self.alien_spawn_event:
                    self.spawn_alien()

            self.update()
            fps_clock.tick(fps)
            pygame.display.set_caption(f"Alien invasion | Current Score: {self.score} | FPS: {int(fps_clock.get_fps())}")
        pygame.quit()