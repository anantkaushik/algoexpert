"""
Problem Link: https://www.algoexpert.io/questions/Balanced%20Brackets

Write a function that takes in a string made up of brackets ("(", "[", "{", ")", "]", and "}") and other optional characters. 
The function should return a boolean representing whether or not the string is balanced in regards to brackets. 
A string is said to be balanced if it has as many opening brackets of a given type as it has closing brackets of that type and 
if no bracket is unmatched. Note that a closing bracket cannot match a corresponding opening bracket that comes after it. 
Similarly, brackets cannot overlap each other as in "[(])".
"""
def balancedBrackets(string):
    # Write your code here.
	stack = []
	for c in string:
		if c in ["(","{","["]:
			stack.append(c)
		else:
			if len(stack) < 1:
				return False
			if stack.pop()+c not in ["()","[]","{}"]:
				return False
	return len(stack) == 0
			