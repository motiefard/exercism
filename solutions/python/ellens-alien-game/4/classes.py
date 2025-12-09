"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.
    """
    total_aliens_created = 0
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1
        
    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, *args):
        pass

    
def new_aliens_collection(coordinates):
    """Return a list of Alien objects created from (x, y) coordinate pairs."""
    return [Alien(x, y) for x, y in coordinates]
    