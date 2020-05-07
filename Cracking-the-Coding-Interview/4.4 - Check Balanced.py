# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this
# question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

def checkBalanced(bt):
  """ the idea is to make a list of all leaf nodes' depth, and compare the max and min of the list. """
  def _checkBalanced(node, index, leavesDepth):
    if node.left:
      _checkBalanced(node.left, index + 1, leavesDepth)
    else:
      leavesDepth.append(index)
    if node.right:
      _checkBalanced(node.right, index + 1, leavesDepth)
    else:
      leavesDepth.append(index)

  leavesDepth = []
  if not bt.root:
    return True
  else:
    _checkBalanced(bt.root, 0, leavesDepth)

  return max(leavesDepth) - min(leavesDepth) <= 1
