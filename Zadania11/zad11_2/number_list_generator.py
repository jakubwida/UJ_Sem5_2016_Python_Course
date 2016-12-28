import random

class Number_List_Generator:
	def random_list(self,size):
		arr = list(range(size))
		random.shuffle(arr)
		return arr

	def almost_random_list(self,size):
		arr=list(range(size))
		for i in range(int(size/3)):
			a = random.randint(0,size-1)
			while True:
				b = a + random.randint(-size/5,size/5)
				if b<= (size-1) and b>=0:
					break
			temp = arr[a]
			arr[a]=arr[b]
			arr[b]=temp
		return arr

	def almost_random_list_reversed(self,size):
		return list(reversed(self.almost_random_list(size)))

	def gauss_list(self,size,mean,std_dev):
		return([random.gauss(mean,std_dev) for i in range(size)])
	
	def repeated_set(self,set_size,out_size):
		arr = range(set_size)
		return([random.choice(arr) for i in range(out_size)])


