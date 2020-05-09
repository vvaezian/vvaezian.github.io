# Implement an algorithm to find the kth to last element of a singly linked list.

def kth_to_last(head, k):
    p1 = head
    p2 = head
    counter = 0
    # calculating the size of linked list
    while p1.nxt:
        p1 = p1.nxt
        counter += 1
    # traversing size - k nodes
    for _ in range(counter - k):
        p2 = p2.nxt
    return p2.val
