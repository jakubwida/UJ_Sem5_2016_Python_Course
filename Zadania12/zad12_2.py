def recurrent_search(L,left,right,y):
	if left <= right:
		k = int((left+right)/2)
		if y == L[k]:
			return k
		if y > L[k]:
			return recurrent_search(L,k+1,right,y)
		else:
			return recurrent_search(L,left,k-1,y)
		return None


arr = list(range(20))
print(arr)
print(arr.index(10))
print(recurrent_search(arr,0,19,10))
