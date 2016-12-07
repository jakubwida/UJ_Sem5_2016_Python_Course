from Node import Node

def merge(node_1, node_2): 
	temp_node=node_1
	while temp_node.next != None :
		temp_node=temp_node.next
	temp_node.next=node_2
	return node_1

nI_1= Node("a1_")
nI_2= Node("a2_")
nI_1.next=nI_2
nI_3= Node("a3_")
nI_2.next=nI_3

print(nI_1)


nII_1= Node("b1_")
nII_2= Node("b2_")
nII_1.next=nII_2
nII_3= Node("b3_")
nII_2.next=nII_3

print(nII_1)

merged = merge(nI_1, nII_1)

print(merged)
