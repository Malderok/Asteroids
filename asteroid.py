import pygame
from circleshape import CircleShape
from constants import *

# Base class for game objects

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, ASTEROID_MIN_RADIUS)
        print(type(self.radius))


    def draw(self, screen):
        # overrrided
        
        pygame.draw.circle(screen,"white", (0,0), self.position, self.radius, 2)

    def update(self, dt):
        # overrrided
        self.position += self.velocity * dt