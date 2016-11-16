import math
class Cell: pass
class Water_Cell(Cell):
	def __init__(self):
		self.level=0
		self.new_level=0
		self.old_level=0
		self.capacity=100;
	
	def __str__(self):
        	return str(self.level).zfill(3)
class Solid_Cell(Cell): 
	def __str__(self):
        	return "sol"

class Cell_Map:
	def __init__(self,filename):
		self.parse_map(filename)
		self.left_focus=False
	def parse_map(self,filename):
		file =open(filename,'r')
		first_line=map(int,file.readline().replace("\n","").split(","))
		self.x_len=first_line[0]
		self.y_len=first_line[1]
		self.map=[]
		for x in range(self.y_len):
			line = file.readline().replace("\n","").split(",")
			print(line)
			for index,element in enumerate(line):
				line[index]= self.block_from_string(element)
			self.map.append(line)
			

		
	def block_from_string(self,block_name):
		if block_name=="sol":
			return Solid_Cell()
		else :
			wc = Water_Cell()
			wc.level=int(block_name)
			return wc 
	def __str__(self):
		out=""
		for line in self.map:
			for element in line:
				out=out+","+element.__str__()
			out=out+"\n"  
		return out
				#can be improved

	def get_cell(self,x,y):
		if x>=0 and x<self.x_len and y>=0 and y<=self.y_len:
			return self.map[y][x]
		else:
			return None;
	def check_cell(self,Cell):
		if Cell==None or Cell.__class__.__name__=="Solid_Cell":
			return False
		else:
			return True
	def calculate_capacity(self,x,y):
		cell_above = self.get_cell(x,y-1)
		if (self.check_cell(cell_above)):
			if(cell_above.old_level>=100):
				return cell_above.capacity+5
			else:
				return 100
		else:
			return 100
		#possible improvements
	def subtract_what_possible_from_level(self,cell,how_much):
		if(cell.level>how_much):
			cell.level=cell.level-how_much
			return how_much
		else:
			temp=cell.level
			cell.level=0
			return temp
	def execute_map(self):
		self.left_focus=not self.left_focus
		#initial iteration
		for y,row in enumerate(self.map):
			for x,element in enumerate(row):
				if element.__class__.__name__ =="Water_Cell":
					element.old_level=element.level
					element.new_level=0
					element.capacity=self.calculate_capacity(x,y)
		#calculation			
		for y,row in reversed(list(enumerate(self.map))):
			for x,element in enumerate(row):
				if element.__class__.__name__ =="Water_Cell":
					up=self.get_cell(x,y-1)
					down=self.get_cell(x,y+1)
					left=self.get_cell(x-1,y)
					right = self.get_cell(x+1,y)
					#down:
					if(self.check_cell(down)):
						down_level_difference = down.capacity-down.level
						if(down_level_difference>0):
							down.new_level+=self.subtract_what_possible_from_level(element,down_level_difference)
					#left/right 
					if(self.left_focus):
						self.do_left_right(element,left)
						self.do_left_right(element,right)
					else:
						self.do_left_right(element,right)
						self.do_left_right(element,left)
					#up
						#pressure might not work will try margulous
					if(self.check_cell(up) and element.level>element.capacity):
						if(up.old_level<element.level):
							given = element.level - element.capacity
							element.level=element.capacity
							up.new_level+=given
		#finalisation - can be optimized			
		for y,row in enumerate(self.map):
			for x,element in enumerate(row):
				if element.__class__.__name__ =="Water_Cell":
					element.level=element.new_level+element.level
					
			
	def do_left_right(self,element,neighbor):
		if(self.check_cell(neighbor)):
			want = element.level-neighbor.old_level
			if want>0:
				given = int(math.ceil(want/2.0))
				element.level-=given
				neighbor.new_level+=given
cm= Cell_Map("map_2.txt")
for i in range(400):
	cm.execute_map()	
	print(i)
print(cm)