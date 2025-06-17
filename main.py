import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	reloj = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	nave = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
	
	dt = 0.0

	#Linea innecesaria nave.containers = (updatable, drawable)
	
	fieldOfAsteroids = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		updatable.update(dt)



		for asteroid in asteroids:
			for shot in shots:
				if shot.collision_check(asteroid):
					asteroid.split()
					shot.kill()
			
			if asteroid.collision_check(nave):
				print("Game Over!")
				return
			 

		screen.fill("black")

		for object in drawable:
			object.draw(screen)
	
		pygame.display.flip()

		#Guardamos la cantidad de tiempo que ha pasado desde el ultimo frame en segundos(milisegundos / 1000)
		dt = reloj.tick(60)/1000.0
            


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")      	
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
