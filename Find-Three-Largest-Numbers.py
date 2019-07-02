"""
Problem Link: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers

Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the input array. 
Note that the function should return duplicate integers if necessary; for example, it should return [10, 10, 12] 
for an input array of [10, 5, 9, 10, 12].
"""
def findThreeLargestNumbers(array):
    # Write your code here.
	largest = secondLargest = thirdLargest = float("-inf")
	for no in array:
		if no >= largest:
			thirdLargest = secondLargest
			secondLargest = largest
			largest = no
		elif no >= secondLargest:
			thirdLargest = secondLargest
			secondLargest = no
		elif no >= thirdLargest:
			thirdLargest = no
	return [thirdLargest, secondLargest, largest]
			