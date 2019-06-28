"""
Problem Link: https://www.algoexpert.io/questions/Nth%20Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and 
the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and 
returns the nth Fibonacci number.
"""
def getNthFib(n):
    # Write your code here.
	if n == 1:
		return 0
	elif n == 2:
		return 1
	a,b = 0,1
	for _ in range(3,n+1):
		a,b = b,a + b
	print(b)
	return b