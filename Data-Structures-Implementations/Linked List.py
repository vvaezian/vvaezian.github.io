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

  
  def insert_behind(self, val1, val2):
    """ inserts a node with value val_1 after the node with value val_2
    Same remarks as for the insert_after function
    """
    if not self.head:
      print('The linkedlist is empty.')
      return False
    cur = self.head
    if cur.val == val1:
      n = Node(val2)
      self.head = n
      n.nxt = cur
      return True
    while cur.nxt:
      if cur.nxt.val == val1:
        n = Node(val2)
        n.nxt = cur.nxt
        cur.nxt = n
        return True
      cur = cur.nxt
    print("Didn't find a node with value {}".format(val1))
    return False


  def reverse(self, in_place=True):
    if not in_place: # returns a copy with the order reversed
      ll = LinkedList()
      if not self.head:
        return ll
      node_list = []
      cur = self.head
      while cur:
        node_list.append(cur)
        cur = cur.nxt
      
      ll.head = node_list[-1]
      node_list[0].nxt = None
      for index, _ in enumerate(node_list[1:]):
        index += 1  # because we excluded the first element
        node_list[index].nxt = node_list[index - 1]

      return ll

    else:
      if not self.head or not self.head.nxt:
        return self
      
      prev = self.head
      cur = self.head.nxt
      self.head.nxt = None
      while cur:
        next_node = cur.nxt  # save the next node pointer
        cur.nxt = prev       # reverse the arrow
        prev = cur           # update prev
        cur = next_node      # update cur
      
      self.head = prev

      return self

    
  def delete_node(self, val1):
    if not self.head:
      return False  # didn't find the node
    if self.head.val == val1:
      self.head = self.head.nxt
      return True

    cur =  self.head
    while cur.nxt:
      if cur.nxt.val == val1:
        cur.nxt = cur.nxt.nxt
        return True
      cur = cur.nxt
    return False  # didn't find the node

  
  def __str__(self):
    if self.head is None:
      return "The linked list is empty."
    else:
      cur = self.head
      output = []
      while cur is not None:
        output.append(cur.val)
        cur = cur.nxt
      return ''.join(str(i) + ' -> ' for i in output)[:-4]  # '-4' is for excluding the last arrow
  
  
ll = LinkedList()
ll.append_to_end(1)
ll.append_to_end(2)
ll.append_to_end(3)
ll.insert_at_start(0)
ll.insert_after(0, 5)
ll.insert_behind(1, 9)
ll.insert_behind(0, -1)
print(ll)
# ll.reverse()
# print(ll)
# print(ll.reverse(in_place=False))
ll.delete_node(9)
print(ll)
ll.delete_node(-1)
print(ll)

