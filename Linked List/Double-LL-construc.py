"""Linked List Construction
Write a Doubly Linked List class that has a head and a tail , both of which point to either a linked list Node or None / null . The class should support:
- Setting the head and tail of the linked list. - Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1 ). - Removing given nodes and removing nodes with given values. - Searching for nodes with given values.
Note that the setHead , setTail , insertBefore, insertAfter, insertAtPosition
and remove methods all take in actual Node s as input parameters—not integers (except for insertAtPosition which also takes in an integer
representing the position); this means that you don't need to create any new Node s in these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be movingthe nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario. If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language like Java or TypeScript to get a better idea of what each input parameter is. Each Node has an integer value as well as a prey node and a next node, both of which can point to either another node or None / null .
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

	# O(1) T | O (1) S
    def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

	# O(1) T | O(1) S
    def setTail(self, node):
		if self.tail is None:
			self.setHead(node)
		self.insertAfter(self.tail, node)

	# O(1) T | O(1) S
	# First we gotta tackle case that what if n=there is no linked list therefore no node. In that case, we were asked to insert a node before something that does not exist and hence, we gotta return
    def insertBefore(self, node, nodeToInsert):
		if (nodeToInsert == self.head and nodeToInsert == self.tail):
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	# O(1) T | O(1) S
    def insertAfter(self, node, nodeToInsert):
		if (nodeToInsert == self.head and nodeToInsert == self.tail):
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	# O(P) T | O(1) S
    def insertAtPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
			return
		currentPosition = 1
		node = self.head
		while node is not None and currentPosition != position:
			currentPosition += 1
			node = node.next
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)

	# O(N) T | O(1) S
    def removeNodesWithValue(self, value):
		node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

	# O(1) T | O(1) S
    def remove(self, node):
		if (node == self.head):
			self.head = self.head.next
		if(node == self.tail):
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

	# O(1) T | O(1) S
	def removeNodeBindings(self,node):
		if node.prev is not None:
			node.prev.next=node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev=None
		node.next=None

	# O(N) T | O(1) S
    def containsNodeWithValue(self, value):
		node = self.head
		while node is not None and node.value!=value:
			node=node.next
		return node is not None
