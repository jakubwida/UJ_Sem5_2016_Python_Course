
def swap(array,index_1,index_2):
	temp = array[index_1]
	array[index_1]=array[index_2]
	array[index_2]=temp

''' Wszystkie ponizsze funkcje to pojedyncze kroki sortowania '''
class Bubble_Sort:



	def __init__(self,array):
		self.array=array
		self.index=1
		self.was_changed=False #True, jesli w jednym cyklu bubblesort nastapila jakakolwieka zmiana, jesli bubblesort doszedl do konca tablicy i jest False, to znazy ze jest posortowane
		self.max_index=len(self.array)-1
		if(len(array)<=1):
			raise ValueError("podana tablica jest zbyt krotka")

	def step(self):
		if(self.array[self.index]<self.array[self.index-1]):
			swap(self.array,self.index,self.index-1)
			self.was_changed=True
		if self.index<self.max_index:
			self.index=self.index+1
			return self.array	
		elif self.was_changed==False:
			return None
		else:
			self.index=1
			self.was_changed=False	
			return self.array
