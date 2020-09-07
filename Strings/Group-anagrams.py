"""Group Anagrams - Write a function that takes in an array of strings and groups anagrams together. Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams. Your function should return a list of anagram groups in no particular order."""

# O(N(strLen)log(strlen)) T | O(N) S


def groupAnagrams(words):
    res = []
    hashT = {}
    for i in range(len(words)):
        string = words[i]
        arrangedString = arrangeString(string)
        #print(f"String was = {string} and arranged string is {arrangedString}")
        if arrangedString in hashT:
            hashT[arrangedString].append(string)
        else:
            hashT[arrangedString] = [string]
    for anagram in hashT:
        res.append(hashT[anagram])
    return res


def arrangeString(string):
    array = list(string)
    array.sort()
    return ''.join(array)
