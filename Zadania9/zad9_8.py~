from Node import Tree_Node

root = Tree_Node(5)
a = Tree_Node(3)
b = Tree_Node(7)
c = Tree_Node(1)
d = Tree_Node(4)
e = Tree_Node(6)

root.left=a
root.right=b
a.left=c
a.right=d
b.left=e

#print(root)

def bst_max(root):
	temp_node = root;
	while temp_node.right!=None:
		temp_node=temp_node.right
	return temp_node.data

def bst_min(root):
	temp_node = root;
	while temp_node.left!=None:
		temp_node=temp_node.left
	return temp_node.data

print(bst_max(root))
print(bst_min(root))
