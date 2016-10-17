

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
Block_Img=pygame.image.load("Block_Img.png")

class Map_Block():
	def __init__(self):
		self.image = Block_Img
Map_of_blocks =\
[
[Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block()],
]			

block_x_size=16
block_y_size=16

def carthesian_to_iso(xy):
	iso_x=(xy[0]-xy[1])/2.0
	iso_y=(xy[0]+xy[1])/2.0
	return [iso_x,iso_y]

def draw_blocks(map_of_blocks):
	x_len=len(map_of_blocks)
	y_len=len(map_of_blocks[0])

	for x in range(x_len):
		for y in range(y_len):
			iso_pos=carthesian_to_iso([x*16,y*16])
			DISPLAYSURF.blit(map_of_blocks[x][y].image,(iso_pos[0],iso_pos[1]))
		
				
		
#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	
	
	
	draw_blocks(Map_of_blocks)
	pygame.display.update()
