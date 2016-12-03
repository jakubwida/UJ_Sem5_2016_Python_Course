def solve(a,b,c):
	return (-c) /a

print(solve(2.0,3.0,5.0))

#Musze przyznac ze do konca nie rozumiem tresci zadania:
#Pojedyncze rownanie liniowe o niezerowych wspolczynnikach samo w sobie nie ma rozwiazania-
#zatem jedyna rzecz ktora moge policzyc to miejsce zerowe funkcji liniowej 
#opisujacej ta sama prosta co to rownanie. Jest to trywialne i zostalo powyzej wykonane.

#Kolejna mozliwoscia jest odnalezienie rozwiazan rownania jest ono "zredukowane", to jest
#ktroas z niewiadomych posiada wspolczynnik 0. W takiej sytuacji podaje ponizej rozwiazanie:

def solve_1(a,b,c):
	if a==0 and b!=0:
		return "y={}".format((-c)/b)
	elif a!=0 and b==0:
		return "x={}".format((-c)/a)
	elif a==0 and b==0:
		raise ValueError("rownanie jest nieoznaczone")
print(solve_1(5,0,3))
