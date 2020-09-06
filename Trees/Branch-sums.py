"""BRANCH SUMS : Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.
Each Binary Tree node has an integer value, a left child node, and a right child node. Children nodes can either be Binary Tree nodes themselves or None / null.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(N) T | O(N) S

def branchSums(root):
    sums = []
    getBranchSums(root, 0, sums)
    return sums


def getBranchSums(node, runningSum, sums):
    if node is None:
        return

    runningSum += node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
        return

    getBranchSums(node.left, runningSum, sums)
    getBranchSums(node.right, runningSum, sums)
