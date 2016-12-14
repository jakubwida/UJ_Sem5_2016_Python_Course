from random import randint
import collections
class RandomQueue:

    def __init__(self):
	self.deque = collections.deque()
	self.count=0;

    def insert(self, item): 
	self.deque.appendleft(item)
	self.count=self.count+1

    def remove(self):   # zwraca losowy element
	self.deque.rotate(randint(0,self.count))
	self.count=self.count-1
	return self.deque.pop()

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



