# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

def minHeightBST(sortedList):

  def _minHeightBST(sortedList, bst):
    if sortedList:
        mid = len(sortedList) // 2
        bst.add(sortedList[mid])
        if mid > 0:
          _minHeightBST(sortedList[:mid], bst)
          _minHeightBST(sortedList[mid + 1:], bst)
          
  bst = BST()
  _minHeightBST(sortedList, bst)
  return bst

# we could use only start and end variables instead of passing half the list, but since the function is returning O(n) data,
# it doesn't make a difference in space complexity.
