

import sys
print(sys.version)
import time
import copy
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

def generate_map(x_size,y_size):
	return [[0 for x in range(x_size)] for y in range(y_size)]
def parse_map(filename):
	file =open(filename,'r')
	y_len=int(file.readline())
	list_of_lists=[]
	for y in range(y_len):
		inner_string = file.readline().replace("\n","")
		inner_list = map(int,list(inner_string))
		
		list_of_lists.append(inner_list)
	file.close()
	print(list_of_lists)
	return list_of_lists

map = parse_map("map_1.txt")


color_dict={0:BACKGROUND_GRAY,1:BLACK,2:BLUE}

def display_map(map):
	y_len = len(map)
	x_len = len(map[0])
	size = 16
	for x in range(x_len):
		for y in range(y_len):
			pygame.draw.rect(DISPLAYSURF, color_dict[map[y][x]], (size*x, size*y, size, size))
			#print(size*(x+1),size*(y+1),size*x,size*y)

turn = False

def simulate_water(map):
	map_2 = [map[y][:] for y in range(len(map)) ]
	
	y_len = len(map)
	x_len = len(map[0])
	for x in range(x_len):
		for y in range(y_len):
			if map[y][x]==2:
				if map[y+1][x]==0:
					map_2[y][x]=0
					map_2[y+1][x]=2
	
	for x in range(x_len):
		for y in range(y_len):
			map[y][x]=map_2[y][x]
	
	
	
	
		
#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE)
	print("map 1",map)
	simulate_water(map)
	print(map)
	display_map(map)
	#pygame.draw.rect(DISPLAYSURF, BLACK, (200, 150, 100, 50))
	pygame.display.update()
	
	
	time.sleep(1)
	
	
	pygame.display.update()
