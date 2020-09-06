"""Suffix Trie Construction - Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the root node of the trie and should support: - Creating the trie from a string this will be done by calling the populateSuffixTrieFrom method upon class instantiation, which should populate the root of the class. - Searching for strings in the trie. Note that every string added to the trie should end with the special endSymbol character: "*" . """


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(N^2)T | O(N^2)S
    def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)

	def insertSubstringStartingAt(self,i,string):
		node = self.root
		for j in range(i,len(string)):
			letter=string[j]
			if letter not in node:
				node[letter]={}
			node = node[letter]
		node[self.endSymbol]=True
		
    # O(M)T | O(1)S
    def contains(self, string):
        node = self.root
		for j in range(len(string)):
			letter = string[j]
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node
