"""Heap Sort - Write a function that takes in an array of integers and returns a sorted version of that array. Use the Heap Sort algorithm to sort the array.
"""

# BEST,AVG,WORST : O(NlogN)T | O(1)S


def heapSort(array):
    buildMaxHeap(array)
       for endIdx in reversed(range(1, len(array))):
            swap(0, endIdx, array)
            siftDown(0, endIdx-1, array)
        return array

def swap(i, j, array):
    array[i], array[j] = array[j],array[i]


def buildMaxHeap(array):
    firstParentIdx = ((len(array)-1)-1)//2
    for currIdx in reversed(range(firstParentIdx+1)):
        siftDown(currIdx, len(array)-1, array)


def siftDown(currIdx, endIdx, array):
    childOneIdx = currIdx*2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currIdx*2 + 2 if currIdx*2 + 2 <= endIdx else -1
        if childTwoIdx != -1 and array[childOneIdx] < array[childTwoIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if array[idxToSwap] > array[currIdx]:
            swap(idxToSwap, currIdx, array)
            currIdx = idxToSwap
            childOneIdx = currIdx*2+1
        else:
            return
