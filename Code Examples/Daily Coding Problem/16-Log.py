'''
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:
   record(order_id): adds the order_id to the log
   get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
'''

class Log:
  def __init__(self, n):
    self.max_size = n
    self.items = [None] * n
    self.cur_index = 0
  
  def record(self, order_id):
    self.items[self.cur_index] = order_id
    self.cur_index = (self.cur_index + 1) % self.max_size

  def get_last(self, i):
    if i > self.max_size:
      raise ValueError('Maximum look back is {} entries'.format(self.max_size))
    return self.items[self.cur_index - i % self.max_size]
  
  def __str__(self):
    return str(self.items)

l = Log(4)
l.record(1)
l.record(2)
l.record(3)
l.record(4)
l.record(5)
print(l)
print(l.get_last(3))
