"""Longest Common Subsequence - Write a function that takes in two strings and returns their longest common subsequence. A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string. For instance, the characters [a", "c", "d"] form a subsequence of the string "abcd", and so do the characters [“b”,”d”] You can assume that there will only be one longest common subsequence. """

# O(NMmin(N,M)) T | O(NMmin(N,M)) S


def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)
    return lcs[-1][-1]

# O(NM) T | O(NM) S


def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None]
            for x in range(len(str1)+1)] for y in range(len(str2)+1)]
       for i in range(1, len(str2)+1):
            for j in range(1, len(str1)+1):
                if str2[i-1] == str1[j-1]:
                    lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1, i-1, j-1]
                else:
                    if lcs[i-1][j][1] > lcs[i][j-1][1]:
                        lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
                    else:
                        lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
        return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs)-1
    j = len(lcs[0])-1
    while i != 0 and j != 0:
        currentLCS = lcs[i][j]
        if currentLCS[0] is not None:
            sequence.append(currentLCS[0])
        i = currentLCS[2]
        j = currentLCS[3]
    return list(reversed(sequence))
