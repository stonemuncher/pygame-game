class Bullet:
    def __init__(self, surf, area, ship):
        # print("bullet spawned")
        self.surf = surf
        self.rect = self.surf.get_rect()
        self.width = self.rect.right - self.rect.left
        self.height = self.rect.top - self.rect.bottom

        self.area = area
        self.ship = ship

        self.x = ship.x + ship.width/2 - 10
        self.y = ship.y

        self.in_area = True
        self.speed = 0.5
        self.rect.update(self.x, self.y, self.width, self.height)

    def update(self):
        if self.area.top < self.y + self.speed - self.height/2 < self.area.bottom:
            self.y -= self.speed
        else:
            self.in_area = False

        self.rect.update(self.x, self.y, self.width, self.height)