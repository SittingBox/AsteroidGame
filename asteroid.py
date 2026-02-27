import random
import pygame
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        asteroid1Velocity = self.velocity.rotate(random_angle)
        asteroid2Velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        baby1 = Asteroid(self.position.x, self.position.y, new_radius)
        baby2 = Asteroid(self.position.x, self.position.y, new_radius)
        baby1.velocity = asteroid1Velocity * 1.2
        baby2.velocity = asteroid2Velocity * 1.2
        
