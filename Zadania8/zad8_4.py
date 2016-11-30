import math
def heron(a,b,c):
	sides=[a,b,c]
	sides.sort()
	if(sides[2]>=sides[1]+sides[0]):
		raise ValueError("this is not a triangle")
	s= float(a+b+c)/2.0
	return(math.sqrt(s*(s-float(a))*(s-float(b))*(s-float(c))))

print(heron(5,2,6))

