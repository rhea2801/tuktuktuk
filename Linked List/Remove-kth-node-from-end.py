"""Remove Kth Node From End 
Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list. 
The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created). Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer. Note that your function doesn't need to return anything. You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes. 
Each Linked List node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
"""
# O(N)T | O(1)S


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 1
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
