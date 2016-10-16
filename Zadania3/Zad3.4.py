while True:
	tekst = input("wprowadz liczbe calkowita:")
	# dla pythona 2:
	#tekst = raw_input("wprowadz liczbe:")
	if tekst == "stop":
		break
	elif not tekst.isdigit():
		print("wprowadzono tekst inny niz liczbe calkowita.")
	else:
		print(tekst,": ",int(tekst)**3)
	
