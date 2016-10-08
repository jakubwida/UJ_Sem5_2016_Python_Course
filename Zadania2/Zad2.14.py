line = " jeden \n  dw.a \n 		\n  \n trzy \n cztery "
list=line.split()
list.sort(key=len,reverse=True)
print(list[0],len(list[0]))

