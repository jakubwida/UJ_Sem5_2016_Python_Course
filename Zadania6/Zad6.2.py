import math
class Point:
	""" Klasa reprezentujaca punkty na plaszczyznie. """
	def __init__(self, x=0, y=0):  # konstuktor
		self.x = x
        	self.y = y

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

class TestPoint(unittest.TestCase): pass

p1 = Point(10.10,2)
p2 = Point(10.20,10.20)
print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1.cross(p2))
print(p1.length())
