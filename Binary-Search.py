"""
Problem Link: https://www.algoexpert.io/questions/Binary%20Search

Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm 
to find if the target number is contained in the array and should return its index if it is, otherwise -1.
"""
def binarySearch(array, target):
    # Write your code here.
	start, end  = 0, len(array)-1
	while start <= end:
		mid = (start+end)//2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	return -1