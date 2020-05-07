# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

def q4_3(btInstance):

  def linkedListOfDepths(node, index, aDict):
    if node:
      if not node.visited:
        node.visited = True
        aDict[index].add(node.key)  # 'add' is a method of LinkedList class
      index += 1
      linkedListOfDepths(node.left, index, aDict)
      linkedListOfDepths(node.right, index, aDict)
    return aDict

  from collections import defaultdict
  aDict = defaultdict(LinkedList) # keys are levels, and values are LinkedLists of the nodes at that level
  returnedDict = linkedListOfDepths(btInstance.root, 0, aDict)
  
  for key, value in returnedDict.items():
    print(key, ': ', value)
