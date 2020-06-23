# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

def q4_3(bt_root):

  def linkedListOfDepths(node, level, aDict):
    if node:
      if not node.visited:
        node.visited = True
        aDict[level].add(node)  # 'add' is a method of LinkedList class
      level += 1
      linkedListOfDepths(node.left, level, aDict)
      linkedListOfDepths(node.right, level, aDict)
    return aDict

  
  from collections import defaultdict
  aDict = defaultdict(LinkedList) # keys are levels, and values are LinkedLists of the nodes at that level
  return linkedListOfDepths(bt_root, 0, aDict)
