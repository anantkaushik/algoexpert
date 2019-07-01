"""
Problem Link: https://www.algoexpert.io/questions/Palindrome%20Check

Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is a palindrome. 
A palindrome is defined as a string that is written the same forward and backward.
"""
def isPalindrome(string):
    # Write your code here.
	start, end = 0, len(string)-1
	while start < end:
		if string[start] != string[end]:
			return False
		start += 1
		end -= 1
	return True