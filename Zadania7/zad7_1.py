

from fractions import gcd

class FractionError(Exception): 
	"""Klasa bledow obslugujaca ulamki"""




class Frac:
	"""Klasa reprezentujaca ulamki."""
	

	def __init__(self, x=0, y=1):
		# Sprawdzamy, czy y=0.
		if y==0:
			raise FractionError("Divide by 0 error")
		else:
			self.x = int(x)
			self.y = int(y)
			self.simplify()

	def frac_from_int(self,integer):
		return Frac(integer,1)

	def frac_from_ambigous(self,ambigous):
		if ambigous.__class__.__name__=="Frac":
			return ambigous;
		elif ambigous.__class__.__name__=="int":
			return self.frac_from_int(ambigous)
		else:
			raise FractionError("Improper type added")

	def simplify(self):
		gcd_val = gcd(self.x,self.y)
		self.x=self.x/gcd_val
		self.y=self.y/gcd_val	

	def __str__(self):         # zwraca "x/y" lub "x" dla y=1
		if self.y!=1:
			return("{}/{}".format(self.x,self.y))
		else:
			return("{}".format(self.x))

	def __repr__(self):        # zwraca "Frac(x, y)"
		return("Frac({},{})".format(self.x,self.y))

	def __eq__(self, other): 
		other = self.frac_from_ambigous(other)
		#print("testing cmp",self,other,self.x,self.y,other.x,other.y,( self.x==other.x and self.y==other.y))
		return (float(self) ==float(other))

	def __cmp__(self, other): # porownywanie
		other = self.frac_from_ambigous(other)
		return cmp(float(self),(float(other)))

	def __add__(self, other):   # frac1+frac2, frac+int
		frac_2 = self.frac_from_ambigous(other);
		frac_1 = Frac(self.x,self.y)
		
		temp =frac_1.y
		frac_1.x=frac_1.x*frac_2.y
		frac_1.y=frac_1.y*frac_2.y

		frac_2.x=frac_2.x*temp
		frac_2.y=frac_2.y*temp

		out_x = frac_1.x+frac_2.x;
		return Frac(out_x,frac_2.y)
	
	__radd__ = __add__              # int+frac


	def __sub__(self, other):  # frac1-frac2, frac-int
		try:
			out = self+-self.frac_from_ambigous(other)
		except FractionError as exception:
			raise FractionError("Improper type subtracted")
		return self+-self.frac_from_ambigous(other)

	def __rsub__(self, other):      # int-frac  //moze generowac problemy
		# tutaj self jest frac, a other jest int!
		return Frac(self.y * other - self.x, self.y)


	def __mul__(self, other):  # frac1*frac2, frac*int
		frac_2 = self.frac_from_ambigous(other);
		return Frac(self.x*frac_2.x,self.y*frac_2.y)

	__rmul__ = __mul__              # int*frac //moze generowac problemy

	def __div__(self, other):  # frac1/frac2, frac/int
		return(self*(~self.frac_from_ambigous(other)))

	def __rdiv__(self, other): # int/frac
		return(self.frac_from_ambigous(other)*(~self))
	# operatory jednoargumentowe
	def __pos__(self):  # +frac = (+1)*frac
		return Frac(self.x,self.y)

	def __neg__(self):         # -frac = (-1)*frac
		return Frac(-self.x,self.y)

	def __invert__(self):      # odwrotnosc: ~frac
		return Frac(self.y,self.x)

	def __float__(self):       # float(frac)
		return (float(self.x)/float(self.y))

# Kod testujacy modul.

f1 = Frac(5,20)
f2= Frac(3,4)

print(f1);
print(float(f2));


import unittest

class TestFrac(unittest.TestCase): 
	def setUp(self): pass
	def test_str(self):
		self.assertEqual(Frac(10,20).__str__(),"1/2")
		self.assertEqual(Frac(10,1).__str__(),"10")
	def test_repr(self):
		self.assertEqual(Frac(10,20).__repr__(),"Frac(1,2)")
	def test_eq(self):
		self.assertTrue(Frac(10,20)==Frac(1,2))
		self.assertFalse(Frac(5,20)==Frac(10,20))

	def test_cmp(self):
		self.assertTrue(Frac(15,20)>Frac(10,20))
		self.assertTrue(Frac(10,20)==Frac(10,20))
		self.assertTrue(Frac(5,20)<Frac(10,20))

	def test_add(self):
		self.assertEqual(Frac(10,20)+Frac(5,20),Frac(15,20))
		self.assertEqual(Frac(10,20)+1,Frac(3,2))
		self.assertEqual(1+Frac(10,20),Frac(3,2))
	def test_sub(self):
		self.assertEqual(Frac(10,20)-Frac(5,20),Frac(5,20))
		self.assertEqual(Frac(10,20)-1,Frac(-1,2))
		self.assertEqual(1-Frac(10,20),Frac(1,2))
	def test_mul(self):
		self.assertEqual(Frac(10,20)*Frac(5,20),Frac(5,40))
		self.assertEqual(Frac(10,20)*2,1)
		self.assertEqual(2*Frac(10,20),1)
	def test_div(self):
		self.assertEqual(Frac(10,20)/Frac(5,20),2)
		self.assertEqual(Frac(10,20)/2,Frac(1,4))
		self.assertEqual(2/Frac(10,20),4)
	def test_pos(self):
		self.assertEqual(Frac(10,20),+Frac(10,20))
	def test_neg(self):
		self.assertEqual(Frac(-5,20),-Frac(5,20))
		self.assertEqual(Frac(5,20),-Frac(-5,20))
	def test_invert(self):
		self.assertEqual(Frac(5,20),~Frac(20,5))
		self.assertEqual(20,~Frac(1,20))
	def test_float(self):
		self.assertEqual(float(Frac(5,20)),5.0/20.0)


if __name__ == '__main__':
    unittest.main()  

		

