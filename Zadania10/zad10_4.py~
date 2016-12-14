import unittest

class Queue:  #implementacja wg. listy tablicowej

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
	if self.is_full():
		raise ValueError("list is already full")
	else:
		self.items[self.tail] = data
		self.tail = (self.tail + 1) % self.n

    def get(self):
	if self.is_empty():
		raise ValueError("list is already empty")
	else:
        	data = self.items[self.head]
        	self.items[self.head] = None      # usuwam referencje
        	self.head = (self.head + 1) % self.n
        	return data



class TestQueue(unittest.TestCase): 
	def setUp(self): pass
	
	def test_empty(self):
		queue=Queue(5)
		self.assertTrue(queue.is_empty())
		queue.put("a")
		self.assertFalse(queue.is_empty())
		queue.get()
		self.assertTrue(queue.is_empty())

	def test_full(self):
		queue=Queue(5)
		self.assertFalse(queue.is_full())
		queue.put("a")
		self.assertFalse(queue.is_full())		
		queue.put("b")
		queue.put("c")
		queue.put("d")
		queue.put("e")
		self.assertTrue(queue.is_full())
		queue.get()
		self.assertFalse(queue.is_full())


	def test_errors(self):
		queue=Queue(5)
		self.assertRaises(ValueError,queue.get)
		queue.put("a")
		queue.put("b")
		queue.put("c")
		queue.put("d")
		queue.put("e")	
		self.assertRaises(ValueError,queue.put,"f")
	
	def test_get(self):
		queue=Queue(5)
		queue.put("a")
		queue.put("b")				
		queue.put("c")
		self.assertEqual("a",queue.get())
		self.assertEqual("b",queue.get())
		self.assertEqual("c",queue.get())
if __name__ == '__main__':
    unittest.main()  
