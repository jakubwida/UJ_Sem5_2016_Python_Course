

import sys
print(sys.version)
import time
import automaton
import pygame
from pygame.locals import*

pygame.init()
FPS = 1
fpsClock = pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Hello world")
rectangle = pygame.Rect(10,20,200,300)

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(100,100,100)
BACKGROUND_GRAY=(200,200,200)
BLUE=(0,0,255)
DISPLAYSURF.fill(WHITE)

# 0= air, 1 = solid 2= water


color_dict={0:BACKGROUND_GRAY,1:BLACK,2:BLUE}



def display_map(cell_map):
	y_len = len(cell_map.map)
	x_len = len(cell_map.map[0])
	size = 16
	for x in range(x_len):
		for y in range(y_len):
			pygame.draw.rect(DISPLAYSURF, color_dict[cell_map.map[y][x]], (size*x, size*y, size, size))
			#print(size*(x+1),size*(y+1),size*x,size*y)

	
	
cell_map=automaton.get_cell_map()		
#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	display_map(cell_map)
	#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
	pygame.display.update()
	
	
	time.sleep(1)
	
	
	pygame.display.update()