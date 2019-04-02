class Entity:
    """
    A generic object to represent player, items, monsters and just about everything else
    """
    def __init__(self, x, y, char, color):
        self.char = char
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        # move entity by a given amount
        self.x += dx
        self.y += dy

