class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, val):
        tmp = self.head
        self.head = Node(val)
        self.head.nxt = tmp

    def insertAtEnd(self, val):
        if self.head:
            tmp = self.head
            while True:
                if tmp.nxt is None:
                    tmp.nxt = Node(val)
                    break
                else:
                    tmp = tmp.nxt
        else:
            self.head = Node(val)

    def insertAfter(self, val_1, val_2):
        """ Assuming all values are distinct. If not, we need to use "keys" for nodes.
            inserts a node with value val_1 after the node with value val_2"""
        if self.head is None:
            print "There is no node with value " + str(val_2)
            return
        else:
            cur = self.head
            while True:
                if cur.val == val_2:
                    tmp = Node(val_1)
                    tmp.nxt = cur.nxt
                    cur.nxt = tmp
                    break
                else:
                    if cur.nxt is not None:
                        cur = cur.nxt
                    else:
                        print "There is no node with value " + str(val_2)
                        return

    def insertBehind(self, val_1, val_2):
        """ Assuming all values are distinct. If not, we need to use "keys" for nodes.
            inserts a node with value val_1 behind the node with value val_2"""
        if self.head is None:
            print "There is no node with value " + str(val_2)
        else:
            if val_2 == self.head:
                self.insertAtFront(val_1)
            else:
                cur = self.head
                while True:
                    if cur.nxt.val == val_2:
                        tmp = Node(val_1)
                        tmp.nxt = cur.nxt
                        cur.nxt = tmp
                        break
                    else:
                        if cur.nxt:
                            cur = cur.nxt
                        else:
                            print "There is no node with value " + str(val_2)
                            break

    def reverse(self):
        cur = self.head
        prev = None
        next = cur.nxt
        while True:
            cur.nxt = prev
            if next is None:
                break
            prev = cur
            cur = next
            next = next.nxt
        self.head = cur

    def __str__(self):
        if self.head is None:
            return "The linked list is empty"
        else:
            cur = self.head
            output = []
            while cur is not None:
                output.append(cur.val)
                cur = cur.nxt
            return ''.join(str(i) + ' -> ' for i in output)[:-4]
            # '-4' is for excluding the last arrow and spaces


ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtFront(0)
print ll
ll.insertAfter(6, 1)
ll.insertAfter(7, 3)
print ll
ll.insertBehind(9, 6)
print ll
ll.reverse()
print ll
