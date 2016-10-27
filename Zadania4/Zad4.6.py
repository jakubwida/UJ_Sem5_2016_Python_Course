def sum_seq(sequence):
	if isinstance(sequence,(list,tuple)):
		return sum(map(sum_seq,sequence))
	else:
		return sequence

print(sum_seq([1,1,(1,1,[1,1],1),1,(),1,1]))
	
		
