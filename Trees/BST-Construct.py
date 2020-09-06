"""BST Construction - Write a BST class for a Binary Search Tree. The class should support: - Inserting values with the insert method. - Removing values with the remove method: this method should only remove the first instance of a given value. - Searching for values with the contains method.
Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.
Each BST node has an integer value , a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left: its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null .
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(logN) T (best,avg) | O(N) T worst case | O(1) S : Applies for all methods listed below

    def insert(self, value):
        currentNode = self
           while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = BST(value)
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = BST(value)
                        break
                    else:
                        currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False

    def remove(self, value, parentNode=None):
        currentNode = self
           while currentNode is not None:
                if value < currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                else:
                    if currentNode.left is not None and currentNode.right is not None:
                        currentNode.value = currentNode.right.getMinValue()
                        currentNode.right.remove(
                            currentNode.value, currentNode)
                    elif parentNode is None:
                        if currentNode.left is not None:
                            currentNode.value = currentNode.left.value
                            currentNode.right = currentNode.left.right
                            currentNode.left = currentNode.left.left
                        elif currentNode.right is not None:
                            currentNode.value = currentNode.right.value
                            currentNode.left = currentNode.right.left
                            currentNode.right = currentNode.right.right
                        else:
                            # this is a single node tree
                            # currentNode.value = None
                            pass
                    elif parentNode.left == currentNode:
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                    elif parentNode.right == currentNode:
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                    break
            return self

        def getMinValue(self):
            currentNode = self
            while currentNode.left is not None:
                currentNode = currentNode.left
            return currentNode.value
