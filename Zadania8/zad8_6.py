#P(0, 0) = 0.5,
#P(i, 0) = 0.0 dla i > 0,
#P(0, j) = 1.0 dla j > 0,
#P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def Recurrent_P(i,j):
	if i<0 or j<0:
		raise ValueError("one of the provided values is below 0")
	if i==0 and j==0:
		return 0.5
	elif j==0 and i>0:
		return 0.0
	elif j>0 and i==0:
		return 1.0
	else:
		return 0.5 * (Recurrent_P(i-1.0,j)+ Recurrent_P(i,j-1.0))

def Table_P(i,j):
	if i<0 or j<0:
		raise ValueError("one of the provided values is below 0")
	if i==0 and j==0:
		return 0.5
	elif j==0 and i>0:
		return 0.0
	elif j>0 and i==0:
		return 1.0
	else:
		dictionary ={}
		for x in range(j+1):
			dictionary["0"+str(x)]=1.0
		for x in range(i+1):
			dictionary[str(x)+"0"]=0.0
		for x in range(1,i+1):
			for y in range (1,j+1):
				dictionary[str(x)+str(y)]=0.5*(dictionary[str(x-1)+str(y)]+dictionary[str(x)+str(y-1)])
		return dictionary[str(i)+str(j)]



print(Recurrent_P(3,4))
print(Table_P(3,4))	


