"""FIND CLOSEST VALUE IN BST : Write a function that takes in a Binary Search Tree (BSI) and a target integer value and retums the closest value to that target value contained in the BST.
You can assume that there will only be one closestvalue.
Each BST node has an integer value , a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BSI property: its value is strictly greater than the value of every node to its let its value is less than or equal to the values of every node to its right and its children nodes are either valid BST nodes themselves or None / null. 
"""


# O(logN) T best,avg | O(N) T worst | O(N) S

def findClosestValueInBst(tree, target):
    return helperFunc(tree, target, tree.value)


def helperFunc(tree, target, closest):
    currNode = tree
    while currNode is not None:
        if abs(target-closest) > abs(target-currNode.value):
            closest = currNode.value
        if target > currNode.value:
            currNode = currNode.right
        elif target < currNode.value:
            currNode = currNode.left
        else:
            break
    return closest

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
