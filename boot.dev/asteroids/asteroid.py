import pygame
import constants
from circleshape import CircleShape
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH) #surface is the methods first paramter which are pushing screen in as the argument

    def update(self, dt: float):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            pygame.sprite.Sprite.kill(self)
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            dir1 = self.velocity.rotate(angle) #If I wrote the full pygame notation it would require me to input two arguments as it thinks it is a class however if I do it on an instance I can pass in one argument like what it is now, the angle.
            dir2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = dir1 * 1.2
            ast2.velocity = dir2 * 1.2
        pygame.sprite.Sprite.kill(self)

