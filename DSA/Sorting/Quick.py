"""QUICK SORT - Write a function that takes in an array of integers and returns a sorted version of that array. Use the Quick Sort algorithm to sort the array. """

# BEST,AVG : O(NlogN)T | O(logN)S
# WORST : O(N^2)T | O(logN)S


def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = pivotIdx+1
    rightIdx = endIdx
    while leftIdx <= rightIdx:
        if(array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]):
            swap(leftIdx, rightIdx, array)
        if(array[leftIdx] <= array[pivotIdx]):
            leftIdx += 1
        if(array[rightIdx] >= array[pivotIdx]):
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    isLeftSubArraySmaller = (rightIdx-1)-startIdx < endIdx-(rightIdx+1)
    if isLeftSubArraySmaller:
        quickSortHelper(array, startIdx, rightIdx-1)
        quickSortHelper(array, rightIdx+1, endIdx)
    else:
        quickSortHelper(array, rightIdx+1, endIdx)
        quickSortHelper(array, startIdx, rightIdx-1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
