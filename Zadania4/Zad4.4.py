


def fibonacci(n):
	x=0
	y=0
	z=1
	for i in range(n-1):
		x=y
		y=z
		z=x+y
	return z

print(fibonacci(10))
