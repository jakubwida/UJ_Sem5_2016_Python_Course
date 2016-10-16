import sys
# program przyjmuje argument dlugosci, bedacy liczba calkowita

dlugosc = sys.argv[1]
print(dlugosc)
if not dlugosc.isdigit():
	print("argument nie jest dodatnia liczba calkowita")	
	sys.exit()
dlugosc=int(dlugosc)
if not dlugosc>=1:
	print("argument nie jest dodatnia liczba calkowita")	
	sys.exit()


linijka="|"+"...|"*(dlugosc-1)

cyferki = list(map(str,(range(dlugosc))))
itercyferki=iter(cyferki)

next(itercyferki)
cyferki = [x.rjust(4) for x in itercyferki]
cyferki = "0"+"".join(cyferki)

print(linijka+"\n"+cyferki)
