"""SUB-ARRAY SORT - Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order).
If the input array is already sorted, the function should return [-1, -1]
"""

# O(N) T | O(1) S


def subarraySort(array):
    minOuttaOrder = float("inf")
      maxOuttaOrder = float("-inf")
       for i in range(len(array)):
            num = array[i]
            if isOuttaOrder(num, i, array):
                minOuttaOrder = min(minOuttaOrder, num)
                maxOuttaOrder = max(maxOuttaOrder, num)
        if minOuttaOrder == float("inf"):
            return [-1, -1]
        leftSubArrayIdx = 0
        rightSubArrayIdx = len(array)-1
        while minOuttaOrder >= array[leftSubArrayIdx]:
            leftSubArrayIdx += 1
        while maxOuttaOrder <= array[rightSubArrayIdx]:
            rightSubArrayIdx -= 1
        return [leftSubArrayIdx, rightSubArrayIdx]


def isOuttaOrder(num, i, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array)-1:
        return num < array[i-1]
    return num < array[i - 1] or num > array[i + 1]
