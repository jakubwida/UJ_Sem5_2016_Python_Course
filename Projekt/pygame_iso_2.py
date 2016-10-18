

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
Ant_Img=pygame.image.load("Ant_Example.png")

class Map_Block():
	def __init__(self):
		self.image = Block_Img
Map_of_blocks =\
[[
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()]
],			
[
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()]
],
[
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()],
[Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block(),Map_Block()]
]]			
			

Map_of_blocks[0][1][1].image=Ant_Img

block_x_size=16
block_y_size=16

def carthesian_to_iso(xyz):
	iso_x=(xyz[0]-xyz[1])/2.0
	iso_y=(xyz[0]+xyz[1]-xyz[2])/2.0
	return [iso_x,iso_y]

def draw_blocks(map_of_blocks,x_draw_size,y_draw_size,z_draw_size,map_x_offset,map_y_offset,map_z_offset,draw_zero_x,draw_zero_y):
	x_len=len(map_of_blocks)
	y_len=len(map_of_blocks[0])
	for z in range(map_z_offset,z_draw_size):
		for x in range(map_x_offset,x_draw_size):
			for y in range(map_y_offset,y_draw_size):
				iso_pos=carthesian_to_iso([x*16,y*16,z*16])
				DISPLAYSURF.blit(map_of_blocks[z][x][y].image,(iso_pos[0]+draw_zero_x,iso_pos[1]+draw_zero_y))
		
screen_x_center=DISPLAYSURF.get_width()/2	
screen_y_center=DISPLAYSURF.get_height()/2

			
		
#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	
	
	
	draw_blocks(Map_of_blocks,3,3,3,0,0,0,screen_x_center,screen_y_center)
	pygame.display.update()
