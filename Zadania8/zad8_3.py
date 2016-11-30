import random
import math



def is_inside(x,y):
	if(math.sqrt(math.pow(x,2.0)+math.pow(y,2.0))<=0.5):
		return True
	else:
		return False




def calc_pi(n=100):
	point_num=n
	inside_num=0
	for i in range(point_num):
		x = random.uniform(-0.5,0.5)
		y = random.uniform(-0.5,0.5)
		if(is_inside(x,y)):
			inside_num=inside_num+1;

	area=float(inside_num)/float(point_num)
	return(area/(math.pow(0.5,2)))

print(calc_pi(100000))	
