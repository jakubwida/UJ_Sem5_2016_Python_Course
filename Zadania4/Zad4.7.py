



def flatten_sequence(sequence):
	
	for element in sequence:
		if isinstance(element,(list,tuple)):
			yield from flatten_sequence(element)
		else:
			yield element

print(list(flatten_sequence([1,[2,[3],[4,5]],6,[7,8],9])))
		
	



		
