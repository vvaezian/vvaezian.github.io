# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
# NOTE: This is not necessarily a binary search tree.

# If nodes have parents, it's easy. In the following we assume nodes don't have parents.
# If it hadn't said "Avoid storing additional nodes in a data structure." we could simulate the tree with another identical tree
# but where nodes have parents (building a mapping between original nodes and simulated nodes along the way) 
# and then solve the problem similar to the case when nodes have parents.
# But since we clearly have been instructed not to do that we can use the follwoing approach (assumes we have access to the 
# root of the tree):
# We first find the paths to the nodes from the root. Then we compare the path and find the the first common ancesstor
# based on that

def firstCommonAncestor(BinaryTreeInstance, n1, n2):

  def _findPathToNodeKey(node, rootNode, path=[]):
    if rootNode:
      if rootNode.key == node.key:
        global returnPath
        returnPath = path[:]
        return
      path2 = path[:]
      path2.append('L')
      _findPathToNodeKey(node, rootNode.left, path2)
      path2 = path[:]
      path2.append('R')
      _findPathToNodeKey(node, rootNode.right, path2)
    return returnPath
  
  path1 = _findPathToNode(n1, BinaryTreeInstance.root)
  path2 = _findPathToNode(n2, BinaryTreeInstance.root)
  cur = BinaryTreeInstance.root
  i = 0
  while True:
    if path1[i] != path2[i]:
      break
    cur = cur.left if path1[i] == 'L' else cur.right
    i += 1
  return cur.key
