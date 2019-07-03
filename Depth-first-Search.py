"""
Problem Link: https://www.algoexpert.io/questions/Depth-first%20Search

You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a simple tree-like structure. 
Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach 
(specifically navigating the tree from left to right), stores all the of the Nodes' names in the input array, and returns it.
"""
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array