"""Max Path Sum In Binary Tree - Write a function that takes in a Binary Tree and returns its max path sum. A path is a collection of connected nodes in a tree where no node is connected to more than two other nodes; a path sum is the sum of the values of the nodes in a particular path. Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null ."""

# O(N) T | O(1) S


def maxPathSum(tree):
    eh, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return(0, float("-inf"))

    leftSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftSumAsBranch, rightSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch+value, value)
    maxSumUsingRootNode = max(
        maxSumAsBranch, leftSumAsBranch + value + rightSumAsBranch)
    runningMaxPathSum = max(
        leftMaxPathSum, rightMaxPathSum, maxSumUsingRootNode)

    return (maxSumAsBranch, runningMaxPathSum)
