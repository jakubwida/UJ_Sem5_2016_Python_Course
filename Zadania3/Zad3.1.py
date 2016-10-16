#1 czesc: dziala
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
print "1 czesc: ",result



#2 czesc: nie kompiluje
# for i in "qwerty": if ord(i) < 100: print i
# jest niepoprawny, zamiast tego: 
for i in "qwerty": 
	if ord(i) < 100: 
		print "2 czesc: ",i


#3 czesc: dziala
for i in "axby": print ord(i) if ord(i) < 100 else i

