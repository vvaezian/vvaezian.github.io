# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.


def weave(list1, list2):
  # recursion-termination criteria
  if list1 == [] or list2 == []:
    return [list1 + list2]
  if len(list1) == 1:
    out = []
    for i in range(len(list2) + 1):
      c = list2[:]
      c.insert(i, list1[0])
      out.append(c)
    return out
  if len(list2) == 1:
    out = []
    for i in range(len(list1) + 1):
      c = list1[:]
      c.insert(i, list2[0])
      out.append(c)
    return out
  
  # recursive calcs
  c1 = list1[:]
  c2 = list2[:]
  output = []
  for i in weave(c1[:-1], c2):
    i.append(c1[-1])
    output.append(i)
  for i in weave(c1, c2[:-1]):
    i.append(c2[-1])
    output.append(i)
  return output


def all_seq(root):
  if not root:
    return [ [] ]
  if not root.left and not root.right:
    return [ [root.val] ]
    
  weaved_all = []
  for i in all_seq(root.left):
    for j in all_seq(root.right):
      weaved = weave(i, j)
      weaved_root_added = [ [root.val] + k for k in weaved ]
      weaved_all.extend(weaved_root_added)
  return weaved_all

class tNode:
  def __init__(self, val, l=None, r=None):
    self.val = val
    self.left = l
    self.right = r


a1 = tNode(1)
a3 = tNode(3)
a2 = tNode(2, a1, a3)
a5 = tNode(5)
a7 = tNode(7)
a6 = tNode(6, a5, a7)
a4 = tNode(4, a2, a6)

print(all_seq(a4))
