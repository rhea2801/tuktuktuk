"""Permutations - Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order. if the input array is empty, the function should return an empty array."""

# O(n^2*n!) T | O(n*n!) S


def getPermutations(array):
    perms = []
    permsHelperMeth(array, [], perms)
    return perms


def permsHelperMeth(array, currPerm, perms):
    if not len(array) and len(currPerm):
        perms.append(currPerm)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            print(currPerm)
            newPerm = currPerm + [array[i]]
            permsHelperMeth(newArray, newPerm, perms)

# MORE EFFICIENT METHOD
# O(n*n!) T | O(n*n!) S


def getPermutations(array):
    perms = []
    permsHelper(0, array, perms)
    return perms


def permsHelper(i, array, perms):
    if i == len(array) - 1:
        perms.append(array[:])
    else:
        for j in range(i, len(array)):
            print(f"i={i} and j={j}")
            swap(array, i, j)
            print(f"After 1st swap : {array}")
            permsHelper(i+1, array, perms)
            swap(array, i, j)
            print(f"After 2nd swap : {array}")
            print('/////////////////')


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
