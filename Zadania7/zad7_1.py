from fractions import gcd
class Frac:
	"""Klasa reprezentujaca ulamki."""

	def __init__(self, x=0, y=1):
		# Sprawdzamy, czy y=0.
		if y==0:
			raise IndexError("Divide by 0 error")
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
			raise IndexError("Improper type added")

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

	def __cmp__(self, other): # porownywanie
		if self.x==other.x and self.y==other.y:
			return True;
		else:
			return False;

	def __add__(self, other):   # frac1+frac2, frac+int
		frac_2 = self.frac_from_ambigous(other);
		frac_1 = Frac(self.x,self.y)
		frac_1_coef= frac_1.x
		frac_1.x = frac_1.x*frac_2.y
		frac_1.y = frac_1.y*frac_2.y
		frac_2.x = frac_2.x *frac_1_coef

		return Frac(frac_1.x+frac_2.x,frac_1.y)
	
	__radd__ = __add__              # int+frac


	def __sub__(self, other):  # frac1-frac2, frac-int
		return self.add(self,-self.frac_from_ambigous(other))

	def __rsub__(self, other):      # int-frac  //moze generowac problemy
		# tutaj self jest frac, a other jest int!
		return Frac(self.y * other - self.x, self.y)


	def __mul__(self, other):  # frac1*frac2, frac*int
		frac_2 = self.frac_from_ambigous(other);
		return Frac(self.x*frac_2.x,self.y*frac_2.y)

	__rmul__ = __mul__              # int*frac //moze generowac problemy

	def __div__(self, other):  # frac1/frac2, frac/int
		return(self*(~self.frac_from_ambigous(other)))

	def __rdiv__(self, other): pass# int/frac
		
	# operatory jednoargumentowe
	def __pos__(self):  # +frac = (+1)*frac
		return Frac(self.x,self.y)

	def __neg__(self):         # -frac = (-1)*frac
		return Frac(-self.x,self.y)

	def __invert__(self):      # odwrotnosc: ~frac
		return Frac(self.y,self.x)

	def __float__(self):       # float(frac)
		return float(x/y)

# Kod testujacy modul.

f1 = Frac(5,20)
f2= Frac(3,16)

print(f1);
print(~f1);
print(-f1);

print(f1);
print(f2);
print(f1/f2);
print(f2/f1);
print(f1*f2);
print(f1+f2);
print(f1-f2);
import unittest

class TestFrac(unittest.TestCase): pass
