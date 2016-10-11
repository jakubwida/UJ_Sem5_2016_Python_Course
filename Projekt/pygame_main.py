import pygame
class ExampleClass:
	def __init__(self):
		print("hello world")
		self.banan =5;
	def printbanan(self):
		print(self.banan)
class MainClass:
	def__init__(self,pygame_display_surface):
		print("this is temporry constructor")
		self.displaysurface=pygame_display_surface
		WHITE=(255,255,255)
		BLACK=(0,0,0)
	def gameloop(self):
		displaysurface.fill(WHITE)
		pygame.display.update()
