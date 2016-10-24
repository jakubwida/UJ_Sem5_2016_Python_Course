import pygame
import random


Block_Img=pygame.image.load("Block_Img.png")
Rock_Img=pygame.image.load("Rock_Img.png")
Ant_Img=pygame.image.load("Ant_Example.png")


#niedkonczone ponizej
class Abstract_Block:
	#self.container_key="Abstract_Block"
	def __init__(self,xyz_coords,game_map,block_list_container):
		self.image=Block_Img
		self.xyz=xyz_coords
		self.Game_Map=game_map
		self.Block_List_Container=block_list_container
		
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
	def add_to_container(Block):
		if(Block.container_key in self.dictionary):
			self.dictionary.get(Block.container_key).append(Block)
		else:
			self.dictionary[Block.container_key]=[Block]
	def remove_from_container(Block):
		list = self.dictionary.get(Block.container_key)
		list.remove(Block)

	def get_list_of_blocks_by_container_key(key):
		return self.dictionary.get(key)





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

class Empty_Block(Abstract_Block):
	def __init__(self,xyz_coords,game_map,block_container):
		Abstract_Block.__init__(self,xyz_coords,game_map,block_container)
		self.image=None
class Rock_Block(Abstract_Block):
	def __init__(self,xyz_coords,game_map,block_container):
		Abstract_Block.__init__(self,xyz_coords,game_map,block_container)
		self.image=Rock_Img



def random_bool(percent=50):
	return random.randrange(100)<percent

class Game_Map:
	def __init__(self):
		print("Game_Map created")
		self.block_container=Block_List_Container()
	def construct_world(self,xyz_size):
		self.world=[[[ self.random_block([x,y,z])  for z in range(xyz_size[2])] for  x in range(xyz_size[0])] for y in range(xyz_size[1])]
		
	def get_block_at_xyz(x,y,z):
		return self.world[x][y][z]
	def set_block_at_xyz(x,y,z,Block):
		self.world[x][y][z]=Block
	
	def random_block(self,xyz_coords):
		coin=random_bool(50)
		if coin:
			return Rock_Block(xyz_coords,self,self.block_container)
		else:
			return Empty_Block(xyz_coords,self,self.block_container)
			
