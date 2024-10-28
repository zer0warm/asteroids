import pygame

from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
