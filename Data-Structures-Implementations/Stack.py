class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []
  
  def peek(self):
    if self.isEmpty():
      print('The stack is empty.')
      return False
    return self.items[-1]
  
  def pop(self):
    if self.isEmpty():
      print('The stack is empty. Cannot perform pop().')
      return False
    return self.items.pop()
  
  def push(self, item):
    self.items.append(item)

  def __str__(self):
    return str(self.items)
