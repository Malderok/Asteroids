import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):



    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.rate_limit = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right


        return [a, b, c]
    
    def draw(self, screen):

        # screen object, color, list of points, line width
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):

        distance = pygame.Vector2(0,1).rotate(self.rotation)

        self.position += distance * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.rate_limit -= dt
        

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE] and self.rate_limit <= 0:
            self.rate_limit = PLAYER_SHOOT_COOLDOWN
            self.shoot()  


    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        