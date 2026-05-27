from circleshape import CircleShape
from shot import Shot
import constants #trying to call constants.PLAYER_RADIUS and constants.LINE_WIDTH with module prefix so need to import whole file, not just specific ones
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0 #must use the self argument in order to initialise the variable of rotation as it wasn't defined in the __init__ parameters
        self.shotCooldown = 0
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        triangle_input = self.triangle() #because triangle is a method belonging to this class instance, you must call it using self.
        pygame.draw.polygon(screen, "white", triangle_input, constants.LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shotCooldown <= 0:
                self.shoot()
        self.shotCooldown -= dt
            
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        self.shotCooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS