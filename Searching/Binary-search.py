"""BINARY SEARCH : Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1"""

# INPUT ARRAY IS ALREADY SORTED !!!!

# ITERATIVE SOLUTION
# O(logN) T | O(logN)


def binarySearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        middle = (left+right)//2
        if(array[middle] == target):
            return middle
        elif(array[middle] > target):
            right = middle-1
        else:
            left = middle+1
    return -1

# RECURSIVE SOLUTION
# O(logN)t | O(logN)S


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle+1
            binarySearchHelper(array, target, left, right)
        else:
            right = middle-1
            binarySearchHelper(array, target, left, right)
    return -1
