"""
Problem Link: https://www.algoexpert.io/questions/Insertion%20Sort

Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Insertion Sort algorithm to sort the array.
"""
def insertionSort(array):
    # Write your code here.
	for i in range(1,len(array)):
		j = i
		value = array[j]
		while j > 0 and array[j-1] > value:
			array[j] = array[j-1]
			j -= 1
		array[j] = value
	return array