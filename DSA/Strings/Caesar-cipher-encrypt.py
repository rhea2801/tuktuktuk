"""CAESAR CIPHER ENCRYPTOR : Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.
Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.
"""
# O(N)T| O(N)S


def caesarCipherEncryptor(string, key):
    list = []
       for letter in string:
            list.append(letter)
        print(list)
        newList = []
        alphabets = ['a', 'b','c','d','e,'f',g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(list)):
            print(f"Initial value = {list[i]}")
            for j in range(len(alphabets)):
                if list[i] ==alphabets[j]:
                    newIndex = (j+1 + key)%(len(alphabets))
                    print(f'newIndex = {newIndex}')
                    print(f"new value = {alphabets[newIndex]}")
                    list[i] = alphabets[newIndex]
        return ''.join(list)
