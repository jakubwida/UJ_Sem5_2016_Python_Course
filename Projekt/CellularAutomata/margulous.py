def get_margulous_at(x,y,matrix):
	x_size=len(matrix[0])
	y_size=len(matrix)
	top_left=None
	if x>=0 and x<x_size and y>=0 and y<y_size
		top_left=matrix[y][x]
	top_right=None
	if x>=0 and (x+1)<x_size and y>=0 and y<y_size
		top_right=matrix[y][x+1]
	down_left=None
	if x>=0 and (x+1)<x_size and y>=0 and (y+1)<y_size
		down_left=matrix[y+1][x]
	down_right=None
	if x>=0 and (x+1)<x_size and >=0 and (y+1)<y_size
		down_right=matrix[y+1][x+1]
	return([[top_left,top_right],[down_left,down_right]])

def set_margulous_at(input,x,y,matrix):
	x_size=len(matrix[0])
	y_size=len(matrix)
	top_left=input[0][0]
	if x>=0 and x<x_size and y>=0 and y<y_size
		matrix[y][x]=top_left
	top_right=input[0][1]
	if x>=0 and (x+1)<x_size and y>=0 and y<y_size
		matrix[y][x+1]=top_right
	down_left=input[1][0]
	if x>=0 and (x+1)<x_size and y>=0 and (y+1)<y_size
		matrix[y+1][x]=down_left
	down_right=input[0][1]
	if x>=0 and (x+1)<x_size and >=0 and (y+1)<y_size
		matrix[y+1][x+1]=down_right
	
	