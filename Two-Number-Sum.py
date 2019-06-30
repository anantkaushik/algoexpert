"""
Problem Link: https://www.algoexpert.io/questions/Two%20Number%20Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. 
If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one 
pair of numbers summing up to the target sum.
"""
def twoNumberSum(array, targetSum):
    # Write your code here.
	temp = set()
	for no in array:
		diff = targetSum - no
		if diff in temp:
			return [diff if diff < no else no,no if diff < no else diff]
		temp.add(no)
	return []