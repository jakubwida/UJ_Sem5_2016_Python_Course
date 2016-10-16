#program przyjmuje rzymski numeral jako pierwszy argument. pisany wielkimi literami
import sys

dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}


def roman2int(roman_string):
	number_list=[dictionary[element] for element in list(roman_string)]
	last =number_list[0]
	i=1;
	while i< (len(number_list)):
		if last < number_list[i]:
			number_list[i-1]=-number_list[i-1]
			i=i+1
			
		i=i+1
		if(i<len(number_list)):
			last=number_list[i-1]
	return(sum(number_list))

print(roman2int(sys.argv[1]))
