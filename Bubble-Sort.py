"""
Problem Link: https://www.algoexpert.io/questions/Bubble%20Sort

Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Bubble Sort algorithm to sort the array.
"""
def bubbleSort(array):
    # Write your code here.
	for i in range(len(array)):
		swap = False
		for j in range(len(array)-1-i):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1], array[j]
				swap = True
		if swap == False:
			break
	return array