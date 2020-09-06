"""FIND 3 LARGEST NOS. : Write a function that takes in an array of integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.
The function should return duplicate integers if necessary; for example, it should return [10,10,12] for an input array of [10,5,9,10,12].
"""
# O(N)T | O(1)S


def findThreeLargestNumbers(array):
    res = [None, None, None]
       for num in array:
            threeLargest(num, res)
        return res

def threeLargest(num, res):
    if(res[2] is None or num >res[2] ):
        shiftNUpdata(num, res,2)
    elif(res[1] is None or num >res[1] ):
        shiftNUpdata(num, res,1)
    elif(res[0] is None or num >res[0] ):
        shiftNUpdata(num, res,0)

def shiftNUpdata(num, res,idx):
    for i in range(idx+1):
        if i == idx:
            res[i] = num
        else:
            res[i] = res[i+1]
