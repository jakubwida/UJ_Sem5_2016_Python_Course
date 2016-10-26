


import math

print(math.factorial(5))


def own_factorial(n):
	result =1
	for i in range(1,n+1):
		result=result*i
	return result
print(own_factorial(5))
