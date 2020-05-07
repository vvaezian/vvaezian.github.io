# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

class tNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def minBST(a_list):

  if len(a_list) == 1:
    return tNode(a_list[0])
  if len(a_list) == 0:
    return None

  m_idx = len(a_list)//2
  m_node = tNode(a_list[m_idx])
  m_node.left, m_node.right = minBST(a_list[:m_idx]), minBST(a_list[m_idx + 1:])

  return m_node
