
''' funkcja wymaga argumentu - nazwy pliku z ktorego pobiera mape. drugi opcjonalny argument to liczba klatek na sekunde - domyslna wartosc to 25'''
import sys
print(sys.version)
import time
import simple_auto
import pygame
from pygame.locals import*

#argument 1= map.txt, argument 2 = FPS (opcjonalny)
arguments =sys.argv


''' inicjalizacja Pygame, z okreslona iloscia klatek na sekunde'''
pygame.init()
if len(arguments)==2:
	arguments.append(25)
FPS = int(arguments[2])
fpsClock = pygame.time.Clock()


''' utworzenie instancji Cell_Map, na podstwie nazwy pliku z argumentu wywolania'''
cell_map=simple_auto.Cell_Map(str(arguments[1]));	
y_len = cell_map.x_len
x_len = cell_map.y_len
size = 32

''' tworzenie powierzchnie w Pygame, ktora '''
DISPLAYSURF=pygame.display.set_mode((x_len*size,y_len*size),0,32)
pygame.display.set_caption("Cellular Automata")


''' lista kolorow'''
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)




''' funkcja ktora pobiera kolor z obiektu bloku Cell Map'''
def get_color_from_block(block):  # 0= air, 1 = solid 2= water
	if block.__class__.__name__ =="Water_Cell":
		return (255-block.level,255-block.level,255)
	else:
		return (0,0,0)

'''funkcja rysujaca wizualna reprezentacje Cell Map, na podstawie powyzszej funkcji '''
def display_map(cell_map):
	for x in range(x_len):
		for y in range(y_len):
			pygame.draw.rect(DISPLAYSURF, get_color_from_block(cell_map.get_cell(x,y)), (size*x, size*y, size, size))
			

	
	
	
'''glowna petla '''
while True:
	for event in pygame.event.get():  #wychodzenie z programu
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill(WHITE) #rysowanie tla
	cell_map.execute_map()#wykonywanie cyklu mapy
	display_map(cell_map) #rysowanie mapy
	pygame.display.update()
	
	fpsClock.tick(FPS) #oczekiwanie na koniec czasu poswieconego na jeden cykl- klatke (FPS)
	pygame.display.update()
