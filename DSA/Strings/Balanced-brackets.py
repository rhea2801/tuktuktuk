"""Balanced Brackets - Write a function that takes in a string made up of brackets ( ( , [ , { , ) , ] , and ) and other optional characters. The function should return a boolean representing whether the string is balanced with regards to brackets.
A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes after it. Also, brackets can't overlap each other as in [0) .
"""

# O(N) T | O(n) S


def balancedBrackets(string):
	bracketMatch = {}
	bracketMatch["}"] = "{"
	bracketMatch["]"] = "["
	bracketMatch[")"] = "("
	bracketStack = []
    for bracket in string:
		if bracket == '[' or bracket == '{' or bracket == '(':
			bracketStack.append(bracket)
		elif bracket == ']' or bracket == '}' or bracket ==')': 
			if len(bracketStack)>0 and bracketMatch[bracket] == bracketStack[-1]:
				bracketStack.pop()
			else:
				return False
	return not len(bracketStack)
		
