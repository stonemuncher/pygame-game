from pygame.sprite import Sprite
import pygame.image
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Ship(Sprite):
    def __init__(self, area, x=0, y=0):
        super().__init__()
        self.surf = pygame.image.load("assets/ship.bmp").convert()
        self.rect = self.surf.get_rect()
        self.width = self.rect.right - self.rect.left
        self.height = self.rect.top - self.rect.bottom
        self.x = x
        self.y = y
        self.area = area
        self.rect.update(self.x, self.y, self.width, self.height)

    def move(self, x_change, y_change):
        if self.area.left < self.x + x_change + self.width/2 < self.area.right:
            self.x += x_change
        if self.area.top < self.y + y_change - self.height/2 < self.area.bottom:
            self.y += y_change
        print(f"x: {self.x}, y: {self.y}")
        self.rect.update(self.x, self.y, self.width, self.height)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.move(0, -0.5)
        if pressed_keys[K_DOWN]:
            self.move(0, 0.5)
        if pressed_keys[K_LEFT]:
            self.move(-0.5, 0)
        if pressed_keys[K_RIGHT]:
            self.move(0.5, 0)


class PlayerShip(Ship):
    def __init__(self, area):
        super().__init__(area)
        self.x = (self.area.width / 2) - (self.width / 2)
        self.y = self.area.height + self.height
        self.move(0, 0)
