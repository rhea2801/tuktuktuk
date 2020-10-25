"""Kadane's Algorithm - Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers."""

# O(N) T | O(1) S


def kadanesAlgorithm(array):
    maxEndingHere, maxSoFar = array[0], array[0]
    for num in array[1:]:
        maxEndingHere = max(maxEndingHere+num, num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
