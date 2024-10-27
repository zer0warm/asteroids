import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Subclass must override this method"""
        pass
    
    def update(self, dt):
        """Subclass must override this method"""
        pass

    def check_collision(self, other):
        radius_distance = self.position.distance_to(other.position)
        if self.radius + other.radius >= radius_distance:
            return True
        return False
