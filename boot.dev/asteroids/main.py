import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state #if I am saying exactly what I am importing I don't need to define the module before calling it in the code below
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    print("Starting Asteroids with pygame version: 2.6")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x, y)
    asteroidField = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the main function and shuts down the script cleanly
        screen.fill("black")
        updatable.update(dt) #need to update the state before drawing it to the screen and then flipping it onto it

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot) == True:
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
                    log_event("asteroid_shot")
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for item in drawable:
            item.draw(screen) #Because in computer graphics, drawing happens on a hidden background buffer (called "double buffering"). When you call pygame.display.flip(), Pygame takes everything drawn on that background buffer and instantly slaps it onto the real monitor screen which requires the draw to be before the flip.

        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
