

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
	def execute(self):
		print("executing Water Blocks")

class Rock_Block(Abstract_Block):
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



