class Cell: pass
class Water_Cell(Cell):
	def __init__l(self):
		self.level=0
		self.new_level=0
	def __str__(self):
        	return level.zfill(3)
class Solid_Cell(Cell): 
	def __str__(self):
        	return "sol"

class Cell_Map:
	def __init__(self,filename):
		self.parse_map(filename)

	def parse_map(self,filename):
		file =open(filename,'r')
		first_line=map(int,file.readline().replace("\n","").split(","))
		self.x_len=first_line[0]
		self.y_len=first_line[1]
		self.map=[]
		for x in range(self.y_len):
			line = file.readline().replace("\n","").split(",")
			print(line)
			for element in line:
				element= self.block_from_string(element)
			self.map.append(line)
			

		
	def block_from_string(self,block_name):
		if block_name=="sol":
			return Solid_Cell()
		else :
			wc = Water_Cell()
			wc.level=int(block_name)
			return wc 
	def __str__(self):
		return self.map

cm= Cell_Map("map_2.txt")
print(cm)
