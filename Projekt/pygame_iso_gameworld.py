import pygame
import random


Block_Img=pygame.image.load("Block_Img.png")
Rock_Img=pygame.image.load("Rock_Img.png")
Ant_Img=pygame.image.load("Ant_Example.png")


#niedkonczone ponizej
class Abstract_Block:
	self.container_key="Abstract_Block"
	def __init__(self,xyz_coords,game_map):
		self.image=Block_Img
		self.xyz=xyz_coords
		self.Game_Map=game_map
		#trzeba dodac: 
		#private_container, ktory bedzie wsadzal bloczka do 
		#listy po utworzniu, i usuwal po zniszczeniu, 
		#najlepiej jako osobny obiekt, ze slownikiem list tak ze latwo odniesc sie do calej listy
		#
		#koordynaty bloczka na mapie, wstawiane w konstruktorze, trzeba sie ogarnac jak dziala dziedziczenie konstruktorow
		#jakis odnosnik do mapy
class Block_List_Container:
	def __init__(self):
		self.dictionary={}
	def add_to_container()






#ponizsze na raznie nie beda uzywane
class Tree_Block:
	def __init__(self):
		self.image=Tree_Img
class Fire_Block:
	def __init__(self):
		self.image=Fire_Img
class Soil_Block:
	def __init__(self):
		self.image=Block_Img
class Grass_Block:
	def __init__(self):
		self.image=Block_Img


#koniec niedkokonczenia

class Empty_Block:
	def __init__(self):
		self.image=None
class Rock_Block:
	def __init__(self):
		self.image=Rock_Img



def random_bool(percent=50):
	return random.randrange(100)<percent

class Game_Map:
	def __init__(self):
		print("Game_Map created")
	def construct_world(self,xyz_size):
		self.world=[[[ self.random_block()  for z in range(xyz_size[2])] for  x in range(xyz_size[0])] for y in range(xyz_size[1])]
		

	def random_block(self):
		coin=random_bool(50)
		if coin:
			return Rock_Block()
		else:
			return Empty_Block()
			
