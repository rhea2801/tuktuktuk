"""INSERTION - Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort algorithm to sort the array. """

# BEST : O(N)T | O(1)S
# AVG : O(N^2)T | O(1)S
# WORST : O(N^2)T | O(1)S


def insertionSort(array):
    for i in range(1, len(array), 1):
        j = i
        print(i)
        while(j > 0 and array[j-1] > array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
        # print(array)
    return array
