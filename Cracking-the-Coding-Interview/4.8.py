# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
# NOTE: This is not necessarily a binary search tree.


# I'm not assuming that the nodes are given, but the NodeKeys are given (this makes more sense to me). 
# So We first find the nodes. While doing this we record the path to them as well. Then we compare the path and find
# the the first common ancesstor based on that

def firstCommonAncestor(BinaryTreeInstance, key1, key2):

  def _findPathToNodeKey(key, rootNode, path=[]):
    if rootNode:
      if rootNode.key == key:
        global returnPath
        returnPath = path[:]
        return
      path2 = path[:]
      path2.append('L')
      _findPathToNodeKey(key, rootNode.left, path2)
      path2 = path[:]
      path2.append('R')
      _findPathToNodeKey(key, rootNode.right, path2)
    return returnPath
  
  path1 = _findPathToNodeKey(key1, BinaryTreeInstance.root)
  path2 = _findPathToNodeKey(key2, BinaryTreeInstance.root)
  cur = BinaryTreeInstance.root
  i = 0
  while True:
    if path1[i] != path2[i]:
      break
    cur = cur.left if path1[i] == 'L' else cur.right
    i += 1
  return cur.key
