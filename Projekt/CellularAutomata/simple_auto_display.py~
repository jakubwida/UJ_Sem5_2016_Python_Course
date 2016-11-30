

import sys
print(sys.version)
import time
import simple_auto
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


def get_color_from_block(block):
	if block.__class__.__name__ =="Water_Cell":
		return (255-block.level,255-block.level,255)
	else:
		return (0,0,0)


def display_map(cell_map):
	y_len = cell_map.x_len
	x_len = cell_map.y_len
	size = 32
	for x in range(x_len):
		for y in range(y_len):
			pygame.draw.rect(DISPLAYSURF, get_color_from_block(cell_map.get_cell(x,y)), (size*x, size*y, size, size))
			

	
	
cell_map=simple_auto.Cell_Map("map_2.txt");		
#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	cell_map.execute_map()
	display_map(cell_map)
	
	#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
	pygame.display.update()
	
	
	time.sleep(1.0/25)
	
	
	pygame.display.update()
