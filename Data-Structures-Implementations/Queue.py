### Implemeting using a list
class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    if self.isEmpty():
      print('The queue is empty.')
      return False
    return self.items.pop()

  def peek(self):
    if self.isEmpty():
      print('The queue is empty.')
      return False
    return self.items[-1]

### Implementing using a doubly-linkedlist
# This is more efficient becuase enqueue operation for lists takes O(n) (as all items need to be shifted one cell) but here it takes O(1)
class Node:
  def __init__(self, val):
    self.val = val
    self.nxt = None
    self.prev = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def isEmpty(self):
    return self.size == 0
  
  def enqueue(self, item):
    n = Node(item)
    if self.isEmpty():
      self.head = self.tail = n
    else:
      n.nxt = self.head
      self.head.prev = n
      self.head = n
  
  def dequeue(self):
    if self.isEmpty():
      print('The queue is empty.')
      return False
    elif self.head = self.tail:  # there is only one item in the queue
      self.head = self.tail = None
    else:
      self.tail.prev.nxt = None
      self.tail = self.tail.prev

  def peek(self):
    if self.isEmpty():
      print('The queue is empty.')
      return False
    else:
      return self.tail.val
