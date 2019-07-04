"""
Problem Link: https://www.algoexpert.io/questions/Breadth-first Search

You are given a Node class that has a name and an array of optional children Nodes. When put together, 
Nodes form a simple tree-like structure. Implement the breadthFirstSearch method on the Node class, 
which takes in an empty array, traverses the tree using the Breadth-first Search approach 
(specifically navigating the tree from left to right), stores all of the Nodes' names in the input array, and returns it.
"""
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
		queue = [self]
		while queue:
			curValue = queue.pop(0)
			array.append(curValue.name)
			for child in curValue.children:
				queue.append(child)
		return array
