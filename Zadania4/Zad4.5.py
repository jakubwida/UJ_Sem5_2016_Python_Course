def odwracanie_iteracyjne(L,left,right):
	distance=right-left
	half_distance=int(distance/2)
	middle=left+int(half_distance)
	
	for i in range(half_distance):
		x=L[half_distance+left-i]
		L[half_distance+left-i]=L[half_distance+left+i]
		L[half_distance+left+i]=x
	print(L)
	return L

print(odwracanie_iteracyjne([1,2,3,4,5,6,7,8,9,10,11],3,6))
# niedokocznone, nie dziala
