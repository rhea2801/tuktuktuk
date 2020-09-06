"""MOVE ELEMENT TO END : You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array. The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers."""

# O(N) T | O(1)S


def moveElementToEnd(array, toMove):
    left = 0
    right = len(array)-1
    while left < right:
        while (array[right] == toMove and left < right):
            right -= 1
        if(array[left] == toMove):
            array[left], array[right] = array[right], array[left]
        left += 1
    return array
