from Points import Point

class Triangle:
	"""Klasa reprezentująca trójkąty na płaszczyźnie."""

	def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
		# Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
		if not (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0.0:
			point_list = [Point(x1, y1),Point(x2, y2),Point(x3, y3)]
			point_list.sort(key = lambda obj: (obj.x,obj.y))
			self.pt1 = point_list[0]
			self.pt2 = point_list[1]
			self.pt3 = point_list[2]
		else:
			raise ValueError("not a valid triangle")

	def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
		return "[({},{}),({},{}),({},{})]".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt2.y)

	def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
		return "Triangle({},{},{},{},{},{})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt2.y)

	def __eq__(self, other):    # obsługa tr1 == tr2
		if(self.pt1==other.pt1 and self.pt2 == other.pt2 and self.pt3==other.pt3):
			return True
		else:
			return False

	def __ne__(self, other):        # obsługa tr1 != tr2
		return not self == other

	def center(self):          # zwraca środek trójkąta
		x = (self.pt1.x+self.pt2.x+self.pt3.x) /3
		y = (self.pt1.y+self.pt2.y+self.pt3.y) /3
		return Point(x,y)

	def area(self):            # pole powierzchni
		 return ((self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))/2)

	def move(self, x, y):      # przesunięcie o (x, y)
		return Triangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y,self.pt3.x+x,self.pt3.y+y)

	def midpoint(self,point1,point2):
		x = (point1.x+point2.x) /2
		y = (point1.y+point2.y) /2
		return Point(x,y)

	def make4(self):           # zwraca listę czterech mniejszych
		p1_2 = self.midpoint(self,pt1,self.pt2)
		p1_3 = self.midpoint(self,pt1,self.pt3)
		p2_3 = self.midpoint(self,pt2,self.pt3)
		tr1= Triangle(self.pt1.x,self.pt1.y,p1_2.x,p1_2.y,p1_3.x,p1_3.y)
		tr2= Triangle(self.pt2.x,self.pt2.y,p1_2.x,p1_2.y,p2_3.x,p2_3.y)
		tr3= Triangle(self.pt3.x,self.pt3.y,p1_3.x,p1_3.y,p2_3.x,p2_3.y)
		tr4= Triangle(p2_3.x,p2_3.y,p1_2.x,p1_2.y,p1_3.x,p1_3.y)
		return [tr1,tr2,tr3,tr4]

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
	def setUp(self):pass
	
	def test_str(self):
		self.assertEqual(Triangle(0,0,1,1,2,1).__str__(),"[(0.0,0.0),(1.0,1.0),(2.0,1.0)]");

	def test_repr(self):
		self.assertEqual(Triangle(0,0,1,1,2,1).__repr__(),"Triangle(0.0,0.0,1.0,1.0,2.0,1.0)");

	def test_eq(self):
		self.assertTrue(Triangle(0,0,1,1,2,1)==Triangle(0,0,1,1,2,1))
		self.assertTrue(Triangle(0,0,1,1,2,1)==Triangle(2,1,1,1,0,0))

	def test_center(self):
		self.assertEqual(Triangle(0,0,1,1,1,2).center(),Point(2/3,1))

	def test_area(self):
		self.assertEqual(Triangle(0,0,1,1,1,2).area(),0.5)

	def test_move(self):
		self.assertEqual(Triangle(0,0,1,1,1,2).move(1,1),Triangle(1,1,2,2,2,3))

if __name__ == '__main__':
    unittest.main()  





