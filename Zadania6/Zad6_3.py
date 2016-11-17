import math

from Zad6_2 import Point

class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie. wszystkie operacje nie modyfikuja oryginalnego prostokatu, jedynie zwracaja taki"""

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):        # "[(x1, y1), (x2, y2)]"
		return("["+self.pt1.__str__()+","+self.pt2.__str__()+"]")

	def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
		return("Rectangle({},{},{},{})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y))

	def __eq__(self, other):   # obsługa rect1 == rect2
		return(self.pt1==other.pt1 and self.pt2==other.pt2)

	def __ne__(self, other):        # obsługa rect1 != rect2
		return not self == other

	def center(self):          # zwraca środek prostokąta
		return Point((self.pt1.x +self.pt2.x)/2 ,(self.pt1.y + self.pt2.y)/2)

	def area(self):            # pole powierzchni
		return (abs(self.pt1.x-self.pt2.x)*abs(self.pt1.y-self.pt2.y))

	def move(self, x, y):      # przesunięcie o (x, y)
		return(Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y))

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
	def test_str(self):
		self.assertEqual(Rectangle(0.5,3,7,1.8).__str__(),"[(0.5,3.0),(7.0,1.8)]")

	def test_repr(self):
		self.assertEqual(Rectangle(0.5,3,7,1.8).__repr__(),"Rectangle(0.5,3.0,7.0,1.8)")

	def test_eq(self):
		self.assertTrue(Rectangle(0.5,3,7,1.8)==Rectangle(0.5,3,7,1.8))
		self.assertFalse(Rectangle(0.1,3,7,1.8)==Rectangle(0.5,3,7,1.8))

	def test_ne(self):
		self.assertFalse(Rectangle(0.5,3,7,1.8)!=Rectangle(0.5,3,7,1.8))
		self.assertTrue(Rectangle(0.1,3,7,1.8)!=Rectangle(0.5,3,7,1.8))

	def test_center(self):
		self.assertEqual(Rectangle(0.5,1,-2.5,0).center(),Point(-1,0.5))

	def test_area(self):
		self.assertEqual(Rectangle(0.5,1,-2.5,0).area(),3)

	def test_move(self):
		self.assertEqual(Rectangle(0.5,1,-2.5,0).move(1,2),Rectangle(1.5,3,-1.5,2))

if __name__ == '__main__':
	unittest.main()  



