class Node:
	"""Klasa reprezentujaca wezel listy jednokierunkowej."""
	
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		if self.next!=None :
			return str(self.data)+str(self.next)   # bardzo ogolnie
		else:
			return str(self.data)
head = None
# pusta lista

head = Node("front")
# lista jednoelementowa


class Tree_Node:
	"""Klasa reprezentujaca wezel drzewa binarnego."""

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def str_help(self,depth):
		out="___."*depth+str(self.data)
		if self.left !=None:
			out = out +"\n"+ self.left.str_help(depth+1)
		else:
			out = out +"\n" + "___."*(depth+1)+"-"	
		if self.right !=None:
			out = out +"\n"+ self.right.str_help(depth+1)
		else:
			out = out +"\n" + "___."*(depth+1)+"-"	
		return out

	def __str__(self):
		return self.str_help(0)
		
