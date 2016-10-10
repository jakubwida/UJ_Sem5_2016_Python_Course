

import sys
print(sys.version)

import pygame
from pygame.locals import*

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Hello world")
rectangle = pygame.Rect(10,20,200,300)

WHITE=(255,255,255)
BLACK=(0,0,0)
DISPLAYSURF.fill(WHITE)
Ant_Img=pygame.image.load("Ant_Example.png")


x=20

#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	
	x=x+0.0005
	
	DISPLAYSURF.blit(Ant_Img,(x,20))
	pygame.display.update()
