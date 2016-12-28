import random
def generate_array(size,width):
	return [random.randint(0,width-1) for i in range(size)]

def choose_and_find_in(array):
	number = random.choice(array)
	indexes=[]
	for index,val in enumerate(array):
		if val== number:
			indexes.append(index)
	return [number,indexes]

arr= generate_array(100,10)
indexes = choose_and_find_in(arr)
print("szukana wartosc:"+str(indexes[0]))
print("lista indeksow na ktorych ja odnaleziono:"+ str(indexes[1]))
print("ilosc odnalezionych pozycji:"+ str(len(indexes[1])))


