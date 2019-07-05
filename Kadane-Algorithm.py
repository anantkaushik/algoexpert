"""
Problem Link: https://www.algoexpert.io/questions/Kadane's%20Algorithm

Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all the numbers in a non-empty 
subarray of the input array. A subarray must only contain adjacent numbers.
"""
def kadanesAlgorithm(array):
    # Write your code here.
		maxSum = array[0]
		tempMaxSum = array[0]
		for i in range(1,len(array)):
			tempMaxSum = tempMaxSum + array[i] if tempMaxSum + array[i] > array[i] else array[i]
			maxSum = tempMaxSum if tempMaxSum > maxSum else maxSum
		return maxSum