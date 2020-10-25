"""SMALLEST DIFFERENCE : Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position. 
You can assume that there will only be one pair of numbers with the smallest difference.
"""

# O(NlogN + MLlogM) T | O(1) S


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pter1 = 0
    pter2 = 0
    current = 0
    smallest = float("inf")
    smallestPair = []
    while pter1 < len(arrayOne) and pter2 < len(arrayTwo):
        firstNum = arrayOne[pter1]
        secondNum = arrayTwo[pter2]
        if(firstNum > secondNum):
            current = firstNum - secondNum
            pter2 += 1
        elif(firstNum < secondNum):
            current = secondNum - firstNum
            pter1 += 1
        else:
            return [firstNum, secondNum]
        if(smallest > current):
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
