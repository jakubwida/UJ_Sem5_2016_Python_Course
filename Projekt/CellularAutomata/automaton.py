
import math

class Abstract_Block:
	color=(0,0,0)
	def __init__(self,x,y,cell_map):
		self.x=x
		self.y=y
		Abstract_Block.cell_map=cell_map
	def __str__(self):
		retrun(color)
	def execute(self):
		print("executing Abstract Blocks")

class Empty_Block(Abstract_Block):
	color=(255,255,255)
	def execute(self):
		print("executing Empty Blocks")

class Water_Block(Abstract_Block):
	color=(0,0,255)
	def __init__(self,x,y,cell_map):
		super(Water_Block,self).__init__(x,y,cell_map)
		self.level=100;
	def execute(self):
		for i in range(len(cell_map[0])):
			for j in range(0, (len(cell_map)),2):
				margulous_result= execute_vertical_margulous(i,j)
				cell_map[j][i]=margulous_result[0]
				cell_map[j+1][i]=margulous_result[1]

		for i in range(0, len(cell_map[0]),2):
			for j in range((len(cell_map))):
				margulous_result= execute_horizontal_margulous(i,j)
				cell_map[j][i]=margulous_result[0]
				cell_map[j][i+1]=margulous_result[1]

		for i in range(len(cell_map[0])):
			for j in range(1, (len(cell_map)),2):
				margulous_result= execute_vertical_margulous(i,j)
				cell_map[j][i]=margulous_result[0]
				cell_map[j+1][i]=margulous_result[1]
		
		for i in range(1, len(cell_map[0]),2):
			for j in range((len(cell_map))):
				margulous_result= execute_horizontal_margulous(i,j)
				cell_map[j][i]=margulous_result[0]
				cell_map[j][i+1]=margulous_result[1]

		for i in range( len(cell_map[0])):
			for j in range((len(cell_map))):
				if cell_map[j][i].__class__.__name__=="Water_Block":
					if cell_map[j][i].level == 0:
						cell_map[j][i]==Empty_Block(i,j,cell_map)


		print("executing Water Blocks")
	
	def execute_vertical_margulous(x,y):
		top= cell_map[y][x]
		bottom= cell_map[y+1][x]
		bottom_capacity=128
		if top.__class__.__name__=="Water_Block" and bottom.__class__.__name__=="Water_Block" and bottom!=None:
			level_sum=top.level+bottom.level
			if top.level> 128:
				bottom_capacity=top+1
			bottom.level= bottom_capacity
			top.level = level_sum- bottom_capacity
		return [top,bottom]

	def execute_horizontal_margulous(x,y):
		left= cell_map[y][x]
		right= cell_map[y][x+1]
		if left.__class__.__name__=="Water_Block" and right.__class__.__name__=="Water_Block" and right!=None:
			level_sum=left.level+right.level
			left.level=math.ceil(level_sum/2.0)
			right.level=math.floor(level_sum/2.0)
		return [left,right]
	def normalise_block(block):
		if block.__class__.__name__=="Water_Block":
			return block.level
		else:
			return 0

		
	
	


	
class Solid_Block(Abstract_Block):
	def execute(self):
		print("executing Solid Blocks")

class Rock_Block(Abstract_Block,Solid_Block):
	color=(128,128,128)
	def execute(self):
		print("executing Rock Blocks")

def generate_map(x_size,y_size):
	return [[0 for x in range(x_size)] for y in range(y_size)]	

class Cell_Map:
	def __init__(self,filename):
		self.parse_map(filename)

	def parse_block_from_string(self,string):
		type_dictionary={"e":Empty_Block,"r":Rock_Block,"w":Water_Block}
		return type_dictionary.get(string,Abstract_Block)	
		
	def parse_map(self,filename):
		file =open(filename,'r')
		types_number=int(file.readline())
		self.types_list=[self.parse_block_from_string(\
file.readline().replace("\n",""))(-1,-1,self) for i in range(types_number)]
		
		print(self.types_list)

		y_len=int(file.readline())


		list_of_lists=[]
		for y in range(y_len):
			inner_string = file.readline().replace("\n","")
			inner_list = list(inner_string)
		
			list_of_lists.append(inner_list)
		file.close()

		x_len=len(inner_list)
		y_len=len(list_of_lists)
		for y in range(y_len):
			for x in range(x_len):
				block = list_of_lists[y][x]
				list_of_lists[y][x]=self.parse_block_from_string(block)(x,y,self)
		self.map = list_of_lists	
	
	def execute_map(self):
		for element in self.types_list:
			element.execute()

def get_cell_map():
	return Cell_Map("map_1.txt")



