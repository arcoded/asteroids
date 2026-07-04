import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_asteroid_point = random.uniform(20.0, 50.0)
            first_asteroid_velocity = self.velocity.rotate(new_asteroid_point)
            second_asteroid_velocity = self.velocity.rotate(-new_asteroid_point)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_asteroid.velocity = first_asteroid_velocity * 1.2
            second_asteroid.velocity = second_asteroid_velocity * 1.2