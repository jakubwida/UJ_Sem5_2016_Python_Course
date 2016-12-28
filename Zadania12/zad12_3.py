def med_sort(List):
	List.sort()
	med=int(len(List)/2)
	return List[med]

arr = list(range(11))
print(arr)
print(med_sort(arr))
