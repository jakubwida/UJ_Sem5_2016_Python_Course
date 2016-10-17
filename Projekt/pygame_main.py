import pygame
class ExampleClass:
	def __init__(self):
		print("hello world")
		self.banan =5;
	def printbanan(self):
		print(self.banan)
class MainClass:
	def __init__(self,pygame_display_surface):
		print("this is temporry constructor")
		self.displaysurface=pygame_display_surface
		WHITE=(255,255,255)
		BLACK=(0,0,0)
	def gameloop(self):
		displaysurface.fill(WHITE)
		pygame.display.update()

class Display: # generates display based on map
	def __init__(self)
		print("this is display constructor")
		self.focus =[0,0]
		
 	
		
class Game_Map: #class dedicated to handling insides of the game
	def __init(self,map_x_size,map_y_size)
		self.two_dimension_array= [[0  for x in range(map_x_size)] for y in range(y)]