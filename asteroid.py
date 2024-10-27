import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
