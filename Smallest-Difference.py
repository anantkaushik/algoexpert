"""
Problem Link: https://www.algoexpert.io/questions/Smallest%20Difference

Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from the first array, 
one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, 
with the number from the first array in the first position. Assume that there will only be one pair of numbers with the smallest difference.
"""
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = idxTwo = 0 
	smallest = current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum == secondNum:
			return [firstNum, secondNum]
		elif firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		else:
			current = firstNum - secondNum
			idxTwo += 1
		if current < smallest:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair