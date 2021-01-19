class Area:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.left = x
        self.top = y
        self.right = self.left + width
        self.bottom = self.top + height
