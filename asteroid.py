import pygame
from circleshape import CircleShape
from constants import *
import random

# Base class for game objects

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        # overrrided
        
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        # overrrided
        self.position += self.velocity * dt


    def split(self):



        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(angle)

        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = self.velocity.rotate(-angle)

