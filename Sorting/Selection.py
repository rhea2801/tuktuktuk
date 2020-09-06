"""ECTION - Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array. """

# BEST, AVG, WORST : O(N^2)T | O(1)S


def selectionSort(array):
    currentIdx = 0
    while (currentIdx < len(array)-1):
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if(array[i] < array[smallestIdx]):
                smallestIdx = i
        swap(smallestIdx, currentIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
