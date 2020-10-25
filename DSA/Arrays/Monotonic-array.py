"""MONOTONIC ARRAY - Monotonic Array Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic. An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing. Note that empty arrays and arrays of one element are monotonic."""

# O(N) T | O(1) S


def isMonotonic(array):
    isNonI = True
    isNonD = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonD = False
        if array[i] > array[i - 1]:
            isNonI = False

    return (isNonI or isNonD)
