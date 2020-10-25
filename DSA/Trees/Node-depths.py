"""NODE DEPTHS : The distance between a node in a Binary Tree and the tree's root is called the node's depth. Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
Each Binary Tree node has an integer value, a left child node, and a right child node. Children nodes can either be Binary Tree nodes themselves or None / null.
"""


# RECURSION O(n) T | O(h) S or O(d) S

def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# METHOD 2
# ITERATION O(N) T | O(d) S or O(h) S


def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return sumOfDepths

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
