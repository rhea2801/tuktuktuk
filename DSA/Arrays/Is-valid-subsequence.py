"""VALIDATE SUBSEQUENCE : Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that am in the same order as they appear in the array. For instance, the numbers [1, 3, a] form a subsequence of the array [1, 2, 3, a] , and so do the numbers [2, 4] . Note that a single number in an array and the array itself are both valid subsequences of the array.
"""
# O(N+M)T | O(1) S


def isValidSubsequence(array, sequence):
    seqIdx = 0
    arrIdx = 0
    while seqIdx < len(sequence) and arrIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            if seqIdx == len(sequence-1):
                return True
            seqIdx += 1
        arrIdx += 1
    return False
