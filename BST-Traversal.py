"""
Problem Link: https://www.algoexpert.io/questions/BST%20Traversal

You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes 
stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is 
strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its 
children nodes are either BST nodes themselves or None (null) values. Write three functions that take in an empty array, traverse the BST, add its nodes' 
values to the input array, and return that array. The three functions should traverse the BST using the in-order traversal, pre-order traversal, and post-order 
traversal techniques, respectively.
"""
def inOrderTraverse(tree, array):
    # Write your code here.
	if tree:
		inOrderTraverse(tree.left,array)
		array.append(tree.value)
		inOrderTraverse(tree.right,array)
	return array

def preOrderTraverse(tree, array):
    # Write your code here.
	if tree:
		array.append(tree.value)
		preOrderTraverse(tree.left,array)
		preOrderTraverse(tree.right,array)
	return array

def postOrderTraverse(tree, array):
    # Write your code here.
	if tree:
		postOrderTraverse(tree.left,array)
		postOrderTraverse(tree.right,array)
		array.append(tree.value)
	return array
