# czesc 1:
print("czesc 1")
X= "qwerty"
def func():
	print(X)
func()
# output: "qwerty"
# funkcja uzywa zmienna i wypisuje jej wartosc. 

# czesc 2:
print("czesc 2")
X= "qwerty"
def func():
	X="abc"
	print(X)
func()
print(X)
# output: "qwerty","abc"
# funkcja uzywa zmienna i wypisuje jej wartosc. X to zmienna lokalna, i przypisanie jej nowej wartosci nie zmienia globalnej X, dlatego poza funkcja pozostaje niezmieniona.

# czesc 3:
print("czesc 3")
X="qwerty"
def func():
	global X
	X ="abc"
func()
print X
# output: "abc"
# funkcja uzywa zmiennej. X to zmienna globalna, i zmiana jej w funckji zmieni jej wartosc w kazdym innym miejscu
