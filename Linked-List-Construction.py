"""
Problem Link: https://www.algoexpert.io/questions/Linked%20List%20Construction

Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, both of which should point to 
either the None (null) value or to a Linked List node. Every node will have a "value" property as well as "next" and "prev" 
properties, both of which can point to either the None (null) value or another node. The class should support setting the head 
and tail of the linked list, inserting nodes before and after other nodes as well as at certain positions, removing given nodes 
and removing nodes with specific values, and searching for nodes with values. Only the searching method should return a value: 
specifically, a boolean.
"""
# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head,node)

    def setTail(self, node):
        # Write your code here.
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail,node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
		if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPos = 1
		while node is not None and currentPos != position:
			node = node.next
			currentPos += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)
			
    def removeNodesWithValue(self, value):
        # Write your code here.
		node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

    def remove(self, node):
        # Write your code here.
		if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
		node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
	
	def removeNodeBindings(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = node.next = None