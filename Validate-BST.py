"""
Problem Link: https://www.algoexpert.io/questions/Validate%20BST

You are given a Binary Tree data structure consisting of Binary Tree nodes. Each Binary Tree node has an integer value stored in a property called "value" 
and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None 
(null) value. Write a function that returns a boolean representing whether or not the Binary Tree is a valid BST. A node is said to be a BST node if and 
only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the 
values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values.
"""
def validateBst(tree,minn = float('-inf'), maxx=float('inf')):
    # Write your code here.
	if not tree:
        return True
    if tree.value < minn or tree.value >= maxx:
        return False
    if not validateBst(tree.left,minn,tree.value):
        return False
    if not validateBst(tree.right,tree.value,maxx):
        return False
    return True