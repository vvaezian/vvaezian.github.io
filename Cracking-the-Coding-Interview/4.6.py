# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
# You may assume that each node has a link to its parent.

def findNextNode(node, target):
  """traverse bst in-order, when spotted the target node, return the node that comes after that 
  node: root of the bst (or the subtree)
  target: the given node that we want to find its 'next' node
  """
  global reachedTargetNode  # made true when we reach the target node
  global flag               # To stop the recursion
  global nextNode           # the node we are looking for
  if flag:
    return
  if node:
    findNextNode(node.left, target)
    if reachedTargetNode:
      nextNode = node # when we get here, we have found the target variable in the previous recursion step, 
                      # so the current node is the node we are looking for
      flag = True   # we have found what we were looking for, no need to look further
    if node.key == target.key:
      reachedTargetNode = True
    findNextNode(node.right, target)
  return nextNode

bst = BST()
bst.creatBST([0, 1, 2, 3, 4, 5])  # This creates a bst out of a sorted list (see answer to question 4.2 in the parent folder) 
reachedTargetNode = False
flag = False
nextNode = None
print(findNextNode(bst.root, bst.root.left.right).key)
