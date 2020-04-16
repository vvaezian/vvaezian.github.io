class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtFront(self, val):
    n = Node(val)
    n.nxt = self.head
    self.head = n

  def append_to_end(self, val):
    n = Node(val)
    if not self.head:
      self.head = n
    else:
      cur = self.head
      while cur.nxt:
        cur = cur.nxt
      cur.nxt = n

  def insert_after(self, val1, val2):
    """ inserts a node with value val_1 after the node with value val_2
    Assuming all values are distinct. If this is not the case, inserts after the first occurence.
    We need to use "keys" for nodes, if we want a general approach for nodes with duplicate values.
    """
    cur = self.head
    while cur:
      if cur.val == val1:
        n = Node(val2)
        n.nxt = cur.nxt
        cur.nxt = n
        return True
      cur = cur.nxt
    print("Didn't find a node with value {}".format(val1))
    return False

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
