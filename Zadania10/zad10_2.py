import unittest

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementow na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
	if self.is_full():
		raise ValueError("stack is already empty")
	else:
        	self.items[self.n] = data
        	self.n = self.n + 1

    def pop(self):
	if self.is_empty():
		raise ValueError("stack is already empty")
	else:
		self.n = self.n - 1
		data = self.items[self.n]
		self.items[self.n] = None    # usuwam referencje
		return data



class TestStack(unittest.TestCase): 
	def setUp(self): pass
	def test_empty(self):
		stack = Stack(5)
		self.assertTrue(stack.is_empty())
		stack.push("a")
		self.assertFalse(stack.is_empty())
		stack.pop()
		self.assertTrue(stack.is_empty())

	def test_full(self):
		stack = Stack(5)
		self.assertFalse(stack.is_full())
		stack.push("a")
		self.assertFalse(stack.is_full())
		stack.push("b")
		stack.push("c")
		stack.push("d")
		stack.push("e")	
		self.assertTrue(stack.is_full())
		stack.pop()
		self.assertFalse(stack.is_full())

	def test_errors(self):
		stack=Stack(5)
		self.assertRaises(ValueError,stack.pop)
		stack.push("a")
		stack.push("b")
		stack.push("c")
		stack.push("d")
		stack.push("e")	
		self.assertRaises(ValueError,stack.push,"f")	

	def test_pop(self):
		stack=Stack(5)
		stack.push("a")
		stack.push("b")	
		self.assertEqual(stack.pop(),"b")
		self.assertEqual(stack.pop(),"a")
		self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()  

