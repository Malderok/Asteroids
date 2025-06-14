import pygame

from constants import *
from player import Player

def main():

	negro = pygame.Color(0,0,0)


	pygame.init()
	reloj = pygame.time.Clock()
	dt = 0.0
	nave = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(negro)

		nave.update(dt)
		nave.draw(screen)

		pygame.display.flip()

		#Guardamos la cantidad de tiempo que ha pasado desde el ultimo frame en segundos(milisegundos / 1000)
		dt = reloj.tick(60)/1000.0
            


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")      	
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
