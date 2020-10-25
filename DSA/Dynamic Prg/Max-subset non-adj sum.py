"""Max Subset Sum No Adjacent   
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array. 
If a sum can't be generated, the function should return 0 . 
"""
# O (N) T | O(N) S | New array of len N created so O(N) S


def maxSubsetNoAdjacentSum(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-2]+array[i], maxSums[i-1])


# O(N) T | O(1) S
def maxSubsetNoAdjacentSum(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second+array[i], first)
        second = first
        first = current
    return first
