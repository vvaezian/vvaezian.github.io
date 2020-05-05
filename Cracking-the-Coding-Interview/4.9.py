# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

def weave(list1, list2):
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

