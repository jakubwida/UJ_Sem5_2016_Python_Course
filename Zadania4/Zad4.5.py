# funkcja odwraca elementy listy o indeksach >= left i <= right

def odwracanie_iteracyjne(L,left,right):
	while left <= right:
		temp =L[left]
		L[left]=L[right]
		L[right]=temp
		left=left+1
		right=right-1
		
	return L

print("odwracanie iteracyjne:")
print([1,2,3,4,5,6,7,8,9,10,11])
print(odwracanie_iteracyjne([1,2,3,4,5,6,7,8,9,10,11],3,6))


def odwracanie_rekurencyjne(L,left,right):
	if left <= right:
		temp =L[left]
		L[left]=L[right]
		L[right]=temp
		L=odwracanie_rekurencyjne(L,left+1,right-1)
	else:
		return L
	return L

print("odwracanie rekurencyjne:")
print([1,2,3,4,5,6,7,8,9,10,11])
print(odwracanie_rekurencyjne([1,2,3,4,5,6,7,8,9,10,11],3,6))
