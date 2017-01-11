''' edytor przyjmuje 3 argumenty- nazwe pliku, rszerokosc i wysokosc mapy. Jesli plik juz istnieje to zostanie otwarty, a argumenty dot rozmiaru zostana zignorowane, i nie musza byc wprowadzane. Edytor kliknieciem lewego przycisku myszy ustawia blok w miejscu klikniecia, prawym zmiena rodzaj bloku, przycisk na klawiaturze "s" zapisuje mape do podanej na starcie nazwy pliku'''



''' import bibliotek'''
import sys
print(sys.version)
import time
import simple_auto
import pygame
import os
from pygame.locals import*


''' przyjmowanie argumentow'''
#argument 1= map.txt, argument 2= x_size, arguemnt 3= y_size
arguments =sys.argv
map_filename=str(arguments[1])


''' inicjalizacja zegara pygame'''
pygame.init()
FPS = 25
fpsClock = pygame.time.Clock()


''' stale uzywanych kolorow '''
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)



''' funkcja przetwarzajaca zaladowany plik i zwracajaca tablice int, uzywana w edytorze '''
def int_array_from_file(file):
	int_map=[]
	for x in range(y_len):
			line = file.readline().replace("\n","").split(",")
			print(line)
			for index,element in enumerate(line):
				line[index]= simplify_block(element)
			int_map.append(line)
	return int_map

''' funkcja uzywana w powyzszej, zamieniajaca string na odpowiadajacy integer'''
def simplify_block(string):
	if string=="sol":
		return 2
	elif string =="000":
		return 0
	else:
		return 1


''' slowniki tlumaczace int mapy na kolor, oraz int na string do zapisu pliku'''
color_dict={0:WHITE,1:BLUE,2:BLACK}
string_dict={0:"000",1:"100",2:"sol"}


''' ladowanie pliku, jesli nie istnieje- tworzenie go'''
if not os.path.exists(map_filename):
	map_file =open(map_filename, 'w')
	x_len = int(arguments[2])
	y_len = int(arguments[3])
	int_map=[[0 for i in range(x_len)] for j in range(y_len)]
else:
	map_file =open(map_filename, 'r+')
	first_line=map(int,map_file.readline().replace("\n","").split(","))
	x_len=first_line[0]
	y_len=first_line[1]
	int_map=int_array_from_file(map_file)
	map_file.close()
	
size = 32

print(int_map)

''' funkcja zapisujaca zmiany do pliku. wpypisuje mape do terminala przy wywolaniu'''
def save_map():
	output = str(x_len)+","+str(y_len)+"\n"
	for y in range(y_len):
			for x in range(x_len):
				output = output+string_dict[int_map[y][x]]
				if x<x_len-1:
					output=output+","
			output=output+"\n"
	map_file =open(map_filename, 'w')
	map_file.write(output)
	map_file.close()
	print(output)


'''inicjalizacja pygame - wyswietlanie'''
DISPLAYSURF=pygame.display.set_mode((x_len*size,y_len*size),0,32)
pygame.display.set_caption("editor")

DISPLAYSURF.fill(WHITE)


'''
# 0= air, 1 = solid 2= water
def get_color_from_block(block):
	if block.__class__.__name__ =="Water_Cell":
		return (255-block.level,255-block.level,255)
	else:
		return (0,0,0)
'''



''' funkcja rysujaca mape'''
def display_map(cell_map):
	for x in range(x_len):
		for y in range(y_len):
			pygame.draw.rect(DISPLAYSURF, color_dict[cell_map[y][x]], (size*x, size*y, size, size))
			



''' funkcja rysujaca kwadrat w kolorze dodawanej komorki przy kursorze'''
cursorval=2
def draw_cursor_rectangle():
	cursor_pos = pygame.mouse.get_pos()
	pygame.draw.rect(DISPLAYSURF, color_dict[cursorval], (cursor_pos[0], cursor_pos[1], size, size))	
	
''' funkcja znajdujaca bloczek, na ktorym jest kurosor'''
def set_int_map_to_cursorval_from_pos(pos):
	x_pos = int(pos[0]/size)
	y_pos = int(pos[1]/size)
	#print(x_pos,y_pos)
	int_map[y_pos][x_pos]=cursorval

''' glowan petla'''
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
      			pos = pygame.mouse.get_pos()
			pressed = pygame.mouse.get_pressed()
			if(pressed[2]==True):
				cursorval=cursorval+1
				if cursorval == 3:
					cursorval =0	
			if(pressed[0]==True):
				set_int_map_to_cursorval_from_pos(pos)	
		if event.type == pygame.KEYDOWN:
        		if event.key == pygame.K_s:
				save_map()


	DISPLAYSURF.fill(WHITE)
	display_map(int_map)
	draw_cursor_rectangle()
	pygame.display.update()
	

	
	
	#pygame.display.update()
