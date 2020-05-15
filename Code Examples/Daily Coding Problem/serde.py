# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

################################

class Node:
  def __init__(self, val, left_node=None, right_node=None):
    self.val = val
    self.left = left_node
    self.right = right_node

def serialize(root):
  out = ''
  q = Queue()
  q.enq(root)
  while not q.isEmpty():
    n = q.deq()
    for node in [n.left, n.right]:
      if node:
        q.enq(node)
        out += ' ' + node.val
      else:
          out += ' None'
          return out


def deSerialize(string):

  def populate(array, index):
    if index >= len(array):
      return
    root = Node(array[index])
    root.left = populate(array, 2 * index + 1)
    root.right = populate(array, 2 * index + 2)
    return root

    node_val_list = string.split()
    return populate(node_val_list, 0)

r = deSerialize('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14')  # 2^n - 1
print(r.val)
print(r.left.val, r.right.val)
print(r.left.left.val, r.left.right.val, r.right.left.val, r.right.right.val)
