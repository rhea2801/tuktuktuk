"""PALINDROME CHECK : Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that single ¬character strings are palindromes.
"""

# O(N^2)T | O(N)S


def isPalindrome(string):
    # O(N) T | O(1) S
    left = 0
    right = len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
