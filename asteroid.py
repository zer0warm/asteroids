import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        s1 = Asteroid(*self.position, split_asteroid_radius)
        s2 = Asteroid(*self.position, split_asteroid_radius)
        s1.velocity = self.velocity.rotate(split_angle) * 1.2
        s2.velocity = self.velocity.rotate(-split_angle) * 1.2
