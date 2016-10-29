
def generate_map(x_size,y_size):
	return [[0 for x in range(x_size)] for y in range(y_size)]
def parse_map(filename):
	file =open(filename,'r')
	y_len=int(file.readline())
	list_of_lists=[]
	for y in range(y_len):
		inner_string = file.readline().replace("\n","")
		inner_list = map(int,list(inner_string))
		
		list_of_lists.append(inner_list)
	file.close()
	print(list_of_lists)
	return list_of_lists
class Cell_Map:
	def __init__(self,map):
		self.map=map

def get_cell_map():
	return CellMap(parse_map(map_1.txt))

def simulate_world():
	print("tryingto simulate world")

def simulate_single_block(map,x_start,y_start,x_end,y_end):
	tempmap=[[map[y][x] for x in range(x_start,x_end)] for y in range(y_start,y_end)]
	if(x_start-x_end==2 && y_start-y_end==2):
		if tempmap== [[0,2],[0,0]]
		
	elif(x_start-x_end==1 && y_start-y_end==2)
	elif(x_start-x_end==2 && y_start-y_end==1)

	
#ruleset
rule_dictionary={\
[[0,0],[0,0]]:[[0,0],[0,0]],
[[0,0],[2,0]]:[[0,0],[0,2]],
[[0,0],[0,2]]:[[0,0],[2,0]],
[[2,0],[0,0]]:[[0,0],[2,0]],
[[0,2],[0,0]]:[[0,0],[0,2]],
[[2,2],[0,0]]:[[0,0],[2,2]],
[[0,0],[2,2]]:[[0,0],[2,2]],	
[[2,0],[2,2]]:[[0,2],[2,2]],
[[0,2],[2,2]]:[[2,0],[2,2]],
[[2,2],[2,2]]:[[2,2],[2,2]],
[[2,0],[0,0]]:[[0,0],[0,0]],
	too ard, going to abandon brb