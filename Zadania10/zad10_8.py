from random import randint
import collections
class RandomQueue:

	def __init__(self):
		self.dict ={}
		self.count=0

	def insert(self, item): 
		self.dict[self.count]=item
		self.count=self.count+1

	def remove(self):   # zwraca losowy element
		index = randint(0,self.count-1)
		out = self.dict[index]
		self.dict[index]=self.dict[self.count-1]
		del self.dict[self.count-1]
		self.count=self.count-1
		return out

	def is_empty(self): 
		return self.count==0

	def is_full(self):
		return False


rd = RandomQueue()

rd.insert("a")
rd.insert("b")
rd.insert("c")
rd.insert("d")
rd.insert("e")
rd.insert("f")


print(rd.remove())
print(rd.remove())
print(rd.remove())
print(rd.remove())
print(rd.remove())
print(rd.remove())


