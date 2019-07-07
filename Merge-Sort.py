"""
Problem Link: https://www.algoexpert.io/questions/Merge%20Sort

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Merge Sort algorithm to sort 
the array.
"""
def mergeSort(array):
    # Write your code here.
	if len(array) <= 1:
		return array
	mid = len(array)//2
	leftArray = array[:mid]
	rightArray = array[mid:]
	return mergeSortedArray(mergeSort(leftArray),mergeSort(rightArray))

def mergeSortedArray(leftArray, rightArray):
	sortedArray = []
	i = j = 0
	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] < rightArray[j]:
			sortedArray.append(leftArray[i])
			i += 1
		else:
			sortedArray.append(rightArray[j])
			j += 1
	while i < len(leftArray):
		sortedArray.append(leftArray[i])
		i += 1
	while j < len(rightArray):
		sortedArray.append(rightArray[j])
		j += 1
	return sortedArray