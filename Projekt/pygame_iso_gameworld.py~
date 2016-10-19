import pygame
import random


Block_Img=pygame.image.load("Block_Img.png")
Ant_Img=pygame.image.load("Ant_Example.png")



class Empty_Block:
	def __init__(self):
		self.image=None
class Rock_Block:
	def __init__(self):
		self.image=Block_Img

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
			