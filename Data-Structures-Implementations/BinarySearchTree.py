# To delete a node from a BST:
# If the node to be deleted is leaf: Simply remove from the tree. 
# If the node to be deleted has only one child: Copy the child to the node and delete the child 
# IF the node to be deleted has two children: 
#   - Find inorder successor of the node (this is a leaf node). 
#   - Update the the ins and outs of the to be deleted node to use this new node. 
#

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):  # Binary Search Tree
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left:    # i.e. if node.left is not 'None'
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def create_bst(self, alist):
        self.root = BST._create_bst(alist, 0, len(alist) - 1)

    @staticmethod
    def _create_bst(alist, start, end):
        if end < start:
            return None
        mid = (start + end) / 2
        root = Node(alist[mid])
        root.right = BST._create_bst(alist, mid + 1, end)
        root.left = BST._create_bst(alist, start, mid - 1)
        return root


b = BST()
b.create_bst([1, 2, 3])
