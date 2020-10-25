"""Depth-first Search - You're given a Node class that has a name and an array of optional chi ldren nodes. When put together, nodes form an acyclic tree-like structure. Implement the depthFirstsearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it. """

# O(V+E) T | O(V)S


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # O(V+E) T | O(V) T
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
