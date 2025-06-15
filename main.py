import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField

def main():

	negro = pygame.Color(0,0,0)

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)


	pygame.init()
	reloj = pygame.time.Clock()
	dt = 0.0
	#Ya no hace falta nave = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
	#Linea innecesaria nave.containers = (updatable, drawable)
	
	fieldOfAsteroids = AsteroidField()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(negro)

		for object in updatable:
			object.update(dt)

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
