
#1 czesc: 
print("czesc 1:")
L=[4,3,2,1]
L = L.sort()
print(L)

	# "L.sort()" zamiast "L=L.sort()"

L1=[4,3,2,1]
L1.sort()
print(L1)



#2 czesc:
print("czesc 2:")
#x, y = 1, 2, 3
	# blad: zbyt duzo przypisywanych wartosci
x, y = 1, 2
	#tyle powinno byc
print(x,y)



#3 czesc:
print("czesc 3:")
#X = 1, 2, 3 ; X[1] = 4
	#blad: nie mozna zmienic elementu listy w niezmienailnej krotce
X =[1,2,3] ; X[1] =4
print(X)



#4 czesc:
print("czesc 4:")
#X = [1, 2, 3] ; X[3] = 4
	#nie mozna przepisac elementu listy poza jej dlugoscia
X = [1, 2, 3, 5] ; X[3] = 4
print(X)



#5 czesc:
print("czesc 5:")
#X = "abc" ; X.append("d")
	# nie mozna wywolac metody "append" na stringu
X = "abc" ; Y = X+"d"
print(Y)



#6 czesc:
print("czesc 6:")
#map(pow, range(8))
	# funkcja pow przyjmuje kilka argumentow, a nie jeden. Nie wiadomo co chcemy zrobic
def pwr(x):
	return pow(x,2)
print(list(map(pwr, range(8))))
	#uwaga- uycie "list" jest niezbedne w pythonie 3








