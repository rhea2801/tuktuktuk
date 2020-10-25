"""`Number Of Ways To Make Change` 
Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations. 
Note that an unlimited amount of coins is at your disposal.
"""

# O (N) T | O(N) S


def costChange(denoms, n):
    ways = [0 for counter in range(n+1)]
    ways[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
        return ways[n]
