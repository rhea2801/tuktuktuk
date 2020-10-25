"""Invert Binary Tree - Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node. 
Each Binary Tree node has an integer value, a left child node, and a right child node. Children nodes can either be Bina ry Tree nodes themselves or None / null.
"""
# For dynamic user input

numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)

print("User List is ", numberList)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert(numberList)
        invertBinaryTree(tree)


# ITERATIVE
# O(N)T | O(N)S


def invertBinaryTree(tree):
    queue = [tree]
    while len(queue) != 0:
        currNode = queue.pop(0)
        if currNode is None:
            continue
        swap(currNode)
        queue.append(currNode.left)
        queue.append(currNode.right)


def swap(tree):
    tree.left, tree.right = tree.right, tree.left


# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# RECURSIVE
# O(N)T | O(d)S


def invertBinaryTree(tree):
    if tree is not None:
        swap(tree)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    return


def swap(tree):
    tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
