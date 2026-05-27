import pygame
import constants
from circleshape import CircleShape 


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, constants.SHOT_RADIUS, constants.LINE_WIDTH) #surface is the methods first paramter which are pushing screen in as the argument

    def update(self, dt: float):
        self.position += self.velocity * dt