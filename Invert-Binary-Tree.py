"""
Problem Link: https://www.algoexpert.io/questions/Invert%20Binary%20Tree

Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for 
its corresponding (mirrored) right node. Each Binary Tree node has a value stored in a property called "value" and two children nodes 
stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the 
None (null) value.
"""
def invertBinaryTree(tree):
    # Write your code here.
	if not tree:
		return None
	tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)