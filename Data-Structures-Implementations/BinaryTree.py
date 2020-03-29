class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def addLeft(self, val):
        """Adds a node with value 'val' to immediate left of the root"""
        if self.root is None:
            self.root = Node(val)
        elif self.root.left is None:
            self.root.left = Node(val)
        else:
            tmp = Node(val)
            tmp.left = self.root.left
            self.root.left = tmp

    def addRight(self, val):
        """Adds a node with value 'val' to immediate right of the root"""
        tmp = Node(val)
        if self.root is None:
            self.root = tmp
        elif self.root.right is None:
            self.root.right = Node(val)
        else:
            tmp.right = self.root.right
            self.root.right = tmp

    def addAtRootL(self, val):
        """creates a node with value 'val' and attaches the tree
         to the left of it"""
        tmp = Node(val)
        if self.root is None:
            self.root = tmp
        else:
            tmp.left = self.root
            self.root = tmp

    def addAtRootR(self, val):
        """Creates a node with value 'val' and attaches the tree
         to the right of it"""
        tmp = Node(val)
        if self.root is None:
            self.root = tmp
        else:
            tmp.right = self.root
            self.root = tmp

    def inorder(self):
        """One of Depth-First Traversal Methods"""
        if self.root:
            self._inOrder(self.root)
        else:
            print 'The tree is empty'

    def _inOrder(self, node):
        if node:
            self._inOrder(node.left)
            print node.value
            self._inOrder(node.right)

    def levelOrder(self):
        """Breadth-First Traversal"""
        from Queue import Queue
        q = Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            node = q.dequeue()
            print node.value
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def levelOrder2(self):
        """Another Breadth-First Traversal without using a Queue"""
        print self.root.value
        l1 = [self.root]  # contains nodes at each level
        while True:
            l2 = []
            output = ''
            for i in l1:
                if i.left:
                    output += str(i.left.value) + ' '
                    l2.append(i.left)
                if i.right:
                    output += str(i.right.value) + ' '
                    l2.append(i.right)
            print output
            if not l2:
                break
            l1 = l2[:]


bt = BinaryTree()
bt.addAtRootL(1)
bt.addRight(2)
bt.addLeft(3)
bt.addAtRootL(4)
bt.addRight(5)
bt.addRight(6)
bt.addAtRootR(7)
bt.addLeft(8)
bt.levelOrder2()
