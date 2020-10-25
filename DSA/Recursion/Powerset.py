"""POWERSET - Write a function that takes in an array of unique integers and returns its powerset. The powerset P (X) of a set X is the set of all subsets of X . For example, the powerset of [1,2] is [[ ] , [1] , [2] , [1,2]]. Note that the sets in the powerset do not need to be in any particular order."""

# ITERATIVE SOLUTION O(n*2^n) ST


def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append([ele]+currentSubset)
    return subsets

# METHOD 2
# RECURSIVE SOLUTION O(n*2^n) ST


def powerset(array, counter=None):
    if counter is None:
        counter = len(array)-1
    if counter < 0:
        return [[]]
    ele = array[counter]
    subsets = powerset(array, counter-1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset+[ele])
    return subsets
