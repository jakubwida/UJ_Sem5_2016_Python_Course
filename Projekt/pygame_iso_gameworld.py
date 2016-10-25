import pygame
import random


Block_Img=pygame.image.load("Block_Img.png")
Rock_Img=pygame.image.load("Rock_Img.png")
Ant_Img=pygame.image.load("Ant_Example.png")



class Abstract_Block:
	#self.container_key="Abstract_Block"
	def __init__(self,xyz_coords,game_map,block_list_container):
		self.image=Block_Img
		self.xyz=xyz_coords
		self.Game_Map=game_map
		self.Block_List_Container=block_list_container
		
		
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
		
	def get_block_at_xyz(self,x,y,z):
		return self.world[x][y][z]
	def set_block_at_xyz(self,x,y,z,Block):
		self.world[x][y][z]=Block
	
	def execute_turn(self):
		print("trying to execute world")
		for key,value in self.block_container.iteritems():
			print(key,value);
			#unfinished


	def random_block(self,xyz_coords):
		coin=random_bool(10)
		if coin:
			return Rock_Block(xyz_coords,self,self.block_container)
		else:
			return Empty_Block(xyz_coords,self,self.block_container)
			
