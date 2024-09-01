import pygame
from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)


	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidField = AsteroidField()

	Shot.containers = (shots, updatable,drawable)
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for asteroid in asteroids:
			if player.check_collision(asteroid):
				print("Game over!")
				return
			for _shot in shots:
				if _shot.check_collision(asteroid):
					asteroid.split()



		for thing in updatable:
			thing.update(dt)
		
		screen.fill((0,0,0))

		for thing in drawable:
			thing.draw(screen)
		
		pygame.display.flip()
		
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
