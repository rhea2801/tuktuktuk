"""Validate BST- Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid. 
Each BST node has an integer value , a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null. A BST is valid if and only if all of its nodes are valid BST nodes.
"""

# O(N)T | O(d)S


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return BSThelper(tree, float("-inf"), float("inf"))


def BSThelper(tree, minVal, maxVal):
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    leftIsValid = BSThelper(tree.left, minVal, tree.value)
    rightIsValid = BSThelper(tree.right, tree.value, maxVal)
    return leftIsValid and rightIsValid
