


def funkcja_3_5(dlugosc): 
	if not dlugosc>=1:
		print("argument nie jest dodatnia liczba calkowita")	
		sys.exit()


	linijka="|"+"...|"*(dlugosc-1)

	cyferki = list(map(str,(range(dlugosc))))
	itercyferki=iter(cyferki)

	next(itercyferki)
	cyferki = [x.rjust(4) for x in itercyferki]
	cyferki = "0"+"".join(cyferki)

	return(linijka+"\n"+cyferki)


def funkcja_3_6(szerokosc_int,wysokosc_int):

	linijka="+-"*szerokosc_int+"+\n"+"| "*szerokosc_int+"|\n"
	linijka =linijka*wysokosc_int+"+-"*szerokosc_int+"+"

	return(linijka)


print(funkcja_3_5(10))
print(funkcja_3_6(10,6))
