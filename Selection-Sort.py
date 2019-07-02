"""
Problem Link: https://www.algoexpert.io/questions/Selection%20Sort

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.
"""
def selectionSort(array):
    # Write your code here.
	for i in range(len(array)):
		minn = array[i]
		for j in range(i+1,len(array)):
			if array[j] < minn:
				array[j], minn = minn, array[j]
		array[i] = minn
	return array