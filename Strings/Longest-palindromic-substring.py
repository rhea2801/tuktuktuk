"""Longest Palindromic Substring - Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes. You can assume that there will only be one longest palindromic substring.
"""
# O(n^2) T | O(n) S


def longestPalindromicSubstring(string):
	if len(string) == 1:
		return string
	maxLen = 0
	maxPalin = ''
    for i in range(len(string)):
		for j in range(i+1,len(string)):
			testString = string[i:j+1]
			isPalindrome = palinCheck(testString,0)
			if isPalindrome:
				currLen = len(testString) 
				if currLen>maxLen:
					maxLen = currLen
					maxPalin = testString
	return maxPalin
	
	
def palinCheck(string,i):
	j = len(string)-i-1
	return True if i>=j else string[i]==string[j] and palinCheck(string,i+1)
	
