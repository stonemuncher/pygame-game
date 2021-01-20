from pygame.sprite import Sprite
import pygame.image
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Ship(Sprite):
    def __init__(self, surf, area, x=0, y=0):
        super().__init__()
        self.surf = surf
        self.rect = self.surf.get_rect()
        self.width = self.rect.right - self.rect.left
        self.height = self.rect.top - self.rect.bottom
        self.x = x
        self.y = y
        self.area = area
        self.rect.update(self.x, self.y, self.width, self.height)
        self.speed = area.width*area.height/1600000

    def move(self, x_change, y_change):
        if self.area.left < self.x + x_change + self.width/2 < self.area.right:
            self.x += x_change
        if self.area.top < self.y + y_change - self.height/2 < self.area.bottom:
            self.y += y_change
        # print(f"x: {self.x}, y: {self.y}")
        self.rect.update(self.x, self.y, self.width, self.height)

    def update(self, pressed_keys):
        pass


class PlayerShip(Ship):
    def __init__(self, surf, area, max_bullets):
        super().__init__(surf, area)
        self.bullets = []
        self.max_bullets = max_bullets
        self.x = (self.area.width / 2) - (self.width / 2)
        self.y = self.area.height + self.height
        self.move(0, 0)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.move(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.move(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.move(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.move(self.speed, 0)

    def get_bullet_no(self):
        return len(self.bullets)


class AlienShip(Ship):
    def __init__(self, surf, area, health=1):
        super().__init__(surf, area)
        self.health = health
        self.alive = True
        self.x = (self.area.width / 2) - (self.width / 2)
        self.y = self.area.top
        self.direction = 1
        self.move(0, 0)

    def update(self, bullets):
        for bullet in bullets:
            if self.y > bullet.y - bullet.height/2 > self.y + self.height:
                if self.x < bullet.x + bullet.width/2 < self.x + self.width:
                    self.health -= 1
                    if self.health == 0:
                        print("Killed alien")
                        self.alive = False
                    bullet.alive = False

        if self.direction:
            if self.x - 10 < self.area.left or self.x + self.width + 10 > self.area.right:
                self.direction *= -1
                self.move(0, 100)
                if self.y > self.area.bottom + self.height - 10:
                    return 0
            self.move(-0.25*self.direction, 0)
        return 1