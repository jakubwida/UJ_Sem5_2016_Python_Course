line = " jeden \n  dw.a \n 		\n  \n trzy \n cztery "
line_list=line.split()
out=""
for ch in line_list:
	out= out+ch[0]
print(out)

out=""
for ch in line_list:
	out= out+ch[-1:]
print(out)
