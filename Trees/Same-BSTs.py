"""Same BSTs - An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array, from left to right into the BST. Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST. Note that you're not allowed to construct any BSTs in your code. A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null ."""

#METHOD 1
#O(N^2) T | O(N^2) S
def sameBsts(arrayOne, arrayTwo):
	if len(arrayOne) != len(arrayTwo):
		return False
 
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False
		
	leftOne = getSmaller(arrayOne)
	leftTwo = getSmaller(arrayTwo)
	rightOne = getBiggerOrEqual(arrayOne)
	rightTwo = getBiggerOrEqual(arrayTwo)
	
	return sameBsts(leftOne,leftTwo) and sameBsts(rightOne,rightTwo)
	
def getSmaller(array):
	smaller = []
	
	for i in range(1,len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller

def getBiggerOrEqual(array):
	bigOrEqual = []
	
	for i in range(1,len(array)):
		if array[i] >= array[0]:
			bigOrEqual.append(array[i])
	return bigOrEqual

#METHOD 2
#O(N^2) T | O(d) S

def sameBsts(arrayOne, arrayTwo):
	return sameBSTHelper(arrayOne, arrayTwo,0,0, float("-inf"), float("inf"))


def sameBSTHelper(arrayOne, arrayTwo, idxOne, idxTwo, minVal, maxVal):
	if idxOne == -1 and idxTwo == -1:
		return True
		
	if arrayOne[idxOne] != arrayTwo[idxTwo]:
		return False
		
	leftIdxOne = getSmallerFirstIdx(arrayOne, idxOne, minVal)
	leftIdxTwo = getSmallerFirstIdx(arrayTwo, idxTwo, minVal)
	rightIdxOne = getBigOrEqual(arrayOne, idxOne, maxVal)
	rightIdxTwo = getBigOrEqual(arrayTwo, idxTwo, maxVal)
	
	currVal = arrayOne[idxOne]
	leftAreSame = sameBSTHelper(arrayOne, arrayTwo, leftIdxOne, leftIdxTwo, minVal, currVal)
	rightAreSame = sameBSTHelper(arrayOne, arrayTwo, rightIdxOne, rightIdxTwo, currVal, maxVal)
	
	return leftAreSame and rightAreSame
	
def getBigOrEqual(array, startIdx, maxVal):
	for i in range(startIdx+1,len(array)):
		if array[i] >= array[startIdx] and array[i] < maxVal:
			return i
	return -1

def getSmallerFirstIdx(array, startIdx, minVal):
	for i in range(startIdx+1,len(array)):
		if array[i] < array[startIdx] and array[i] >= minVal:
			return i
	return -1