import pygame

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision_check(Self, other):

        if Self.radius + other.radius > Self.position.distance_to(other.position):
            return True
        return False



    def draw(self, screen):
        # sub-calsses must overrride
        pass

    def update(self, dt):
        # sub-calsses must overrride
        pass