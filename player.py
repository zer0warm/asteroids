import pygame

from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shoot_timer = 0

    def triangle(self):
        """Return positions of 3 triangle vertices"""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        """Draw a white player"""
        pygame.draw.polygon(screen, (0xff, 0xff, 0xff), self.triangle(), 2)

    def update(self, dt):
        """Update player rotation on key pressed"""
        keys = pygame.key.get_pressed()

        # rotate
        # Weird bug: J/K + H + Space doesn't shoot. If J/K + Space and then +H
        # it shoots but never curve left. Change H to another key works
        # perfectly.
        if keys[pygame.K_h]:
            # anti-clockwise
            self.rotate(-dt)
        if keys[pygame.K_l]:
            # clockwise
            self.rotate(dt)

        # move
        if keys[pygame.K_k]:
            # up
            self.move(dt)
        if keys[pygame.K_j]:
            # down
            self.move(-dt)

        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def rotate(self, dt):
        """Rotate player"""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.__shoot_timer <= 0:
            # Shot(x, y, radius=SHOT_RADIUS)
            shot = Shot(*self.position)
            shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.__shoot_timer = PLAYER_SHOOT_RATE
        self.__shoot_timer -= dt
