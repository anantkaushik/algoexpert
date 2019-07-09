"""
Problem Link: https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End

Write a function that takes in the head of a Singly Linked List and an integer k (assume that the list has at least k nodes). 
The function should remove the kth node from the end of the list. Note that every node in the Singly Linked List has a "value" 
property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.
"""
def removeKthNodeFromEnd(head, k):
    # Write your code here.
	fast = head
	while fast and k:
		fast = fast.next
		k -= 1
	if not fast:
		head.value = head.next.value
		head.next = head.next.next
		return
	slow = head
	while fast.next:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next