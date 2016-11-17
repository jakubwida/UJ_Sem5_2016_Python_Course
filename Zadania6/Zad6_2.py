import math

class Point:
	""" Klasa reprezentujaca punkty na plaszczyznie. """
	def __init__(self, x=0, y=0):  # konstuktor
		self.x = round(float(x),6)
		self.y = round(float(y),6)

	def __str__(self):         # zwraca string "(x, y)"
		return("({},{})".format(self.x,self.y))

	def __repr__(self):        # zwraca string "Point(x, y)"
		return("Point({},{})".format(self.x,self.y))

	def __eq__(self, other):   # obsluga point1 == point2
		if(self.x==other.x and self.y==other.y):
			return True
		else:
			return False
	def __ne__(self, other):        # obsluga point1 != point2
		return not self == other

    # Punkty jako wektory 2D.
	def __add__(self, other):  # v1 + v2
		return Point(self.x+other.x,self.y+other.y)

	def __sub__(self, other):  # v1 - v2
		return Point(self.x-other.x,self.y-other.y)

	def __mul__(self, other):  # v1 * v2, iloczyn skalarny
		return (self.x*other.x+self.y*other.y)

	def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
		return self.x * other.y - self.y * other.x

	def length(self):          # dlugosc wektora
		return math.sqrt(self.x ** 2.0 +self.y ** 2.0)
# Kod testujacy modul. TODO

import unittest

class TestPoint(unittest.TestCase): 
	def setUp(self): pass

	def test_str(self):
		self.assertEqual(Point(1.2,5).__str__(),"(1.2,5.0)")

	def test_repr(self):
		self.assertEqual(Point(1.2,5).__repr__(),"Point(1.2,5.0)")

	def test_eq(self):
		self.assertTrue(Point(1.2,5)==Point(1.2,5))
		self.assertFalse(Point(1.2,5)==Point(1.4,5))

	def test_ne(self):
		self.assertFalse(Point(1.2,5)!=Point(1.2,5))
		self.assertTrue(Point(1.2,5)!=Point(1.4,5))

	def test_add(self):
		self.assertEqual(Point(1.2,5)+Point(1.2,5.7),Point(2.4,10.7))

	def test_sub(self):
		self.assertEqual(Point(1.2,5)-Point(1.2,5.7),Point(0,-0.7))

	def test_mul(self):
		self.assertEqual(Point(1.2,5)*Point(1.2,3),16.44)

	def test_cross(self):
		self.assertEqual(Point(1.2,5).cross(Point(1.2,3)),(1.2*3-5*1.2))

	def test_length(self):
		self.assertEqual(Point(4,3).length(),5)

if __name__ == '__main__':
    unittest.main()  



