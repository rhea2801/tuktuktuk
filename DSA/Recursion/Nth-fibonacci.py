"""Nth FIBONACCI : The Fibonacci sequence is defined as follows: the first number of the sequence is 0 , the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number. Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1 . For the purpose of this question, the first Fibonacci number Is Fo ; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1 , etc.."""

# O(N) T | O(1) S


def getNthFib(n):
    if n == 1:
        return 0
    if (n == 2):
        return 1
    counter = 3
    lastTwo = [0, 1]
    while counter <= n:
        nextFib = lastTwo[0]+lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1]


# O(2^N) T | O(N) S
# Recursive

def getNthFib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return (getNthFib(n-1)+getNthFib(n-2))

# O(N) T | O(N) S
# Memoization and caching


def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return n
    else:
        memoize[n] = n
    return getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
