"""BUBBLE - Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array. """

# BEST : O(N)T | O(1) S
# AVG : O(N^2)T | O(1) S
# WORST : O(N^2)T | O(1) S


def bubbleSort(array):
    isSorted = False
    counter = 0
    while(not isSorted):
        isSorted = True
        for i in range(len(array)-1-counter):
            if(array[i] > array[i+1]):
                swap(i, i+1, array)
                i += 1
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
