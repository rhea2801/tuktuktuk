"""Find Loop - Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail node points to some node in the list instead of None / null ). The function should return the node (the actual node--not just its value) from which the loop originates in constant space. Each LinkedList node has an integer value as well as a next node pointing to the next node in the list."""


# O(N) T | O(1) S
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
