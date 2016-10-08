
"""instruction: first argument value = file to copy from, second = file to copy to"""
from sys import argv


from_file = open(argv[1],"r")
to_file =open(argv[2],"w")


for line in from_file:
	if not( line[0]=="#"): 
		to_file.write(line)
		
