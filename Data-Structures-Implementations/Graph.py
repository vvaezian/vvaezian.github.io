from Queue import Queue


class Node(object):
    def __init__(self, key, neighbours):
        self.key = key
        self.neighbors = neighbours
        self.visited = False
        self.parent = None  # Is needed for finding the shortest path using BFS


class Graph(object):
    """"nodes and edges are given as an adjacency list.
        Adjacency list itself is given as a tuple of node key and
         a list of its neighbors"""
    def __init__(self, nodes):
        self.nodes = [Node(item[0], item[1]) for item in nodes]
        self.flag = False   # auxiliary variable used in _dfs2 method

    def __str__(self):
        for item in self.nodes:
            print str(item.key) \
                + ' : '         \
                + ''.join(str(i) + ', ' for i in item.neighbors)[:-2]
        return ''

    def get_node(self, key):
        for node in self.nodes:
            if node.key == key:
                return node
        print 'not found!'
        return None

    def dfs(self, key):
        """Explores the graph rooted at 'key' using Depth-First Search"""
        node = self.get_node(key)
        if not node.visited:
            print node.key
            node.visited = True
            for i in node.neighbors:
                self.dfs(i)
        # Reverting the visited status of all nodes not 'not visited'
        for node in self.nodes:
            node.visited = False

    def dfs2(self, start, end):
        """Finds a path between start and end or the reverse direction if one exists
            using Depth-First Search"""

        def _dfs2(_start, _end, _tmp_path):
            global path
            if self.flag:  # if the destination is reached, stop recursion
                return
            s = self.get_node(_start)
            if not s.visited:
                s.visited = True
                tmp_path_copy = _tmp_path[:]
                tmp_path_copy.append(s.key)
                for node in s.neighbors:
                    if node == _end:    # if the destination node is reached
                        self.flag = True
                        tmp_path_copy.append(node.key)
                        path = tmp_path_copy
                        return
                    _dfs2(node, end, tmp_path_copy)

            # Reverting back the visited status of all nodes to 'not visited'
            for node in self.nodes:
                node.visited = False

            if self.flag:
                return path

        tmp_path = []
        a = _dfs2(start, end, tmp_path)
        b = _dfs2(end, start, tmp_path)
        if a:
            print 'There is a path between {} and {}: {}'.format(start, end, a)
        if b:
            print 'There is a path between {} and {}: {}'.format(end, start, b)
        if not a and not b:
            print 'There is no path between {} and {}'.format(start, end)

    def bfs(self, key):
        """Explores the graph rooted at 'key' using Breadth-First Search"""
        node = self.get_node(key)
        q = Queue()
        q.enqueue(node)
        node.visited = True
        while not q.isEmpty():
            n = q.dequeue()
            print n.key
            for node in n.neighbors:
                if not node.visited:
                    q.enqueue(node)
                    node.visited = True
        # Reverting the visited status of all nodes not 'not visited'
        for node in self.nodes:
            node.visited = False

    def bfs2(self, start, end):
        """Finds a path between start and end or the reverse direction if one exists
            using Breadth-First Search"""

        def _bfs2(_start, _end):
            q = Queue()
            s = self.get_node(_start)
            q.enqueue(s)
            while not q.isEmpty():
                node = q.dequeue()
                if node.key == _end:
                    _path = []
                    while True:
                        _path.append(node.key)
                        if not node.parent:  # reached the root node
                            _path.reverse()
                            break
                        node = node.parent
                    return _path
                for i in node.neighbors:
                    n = self.get_node(i)
                    if not n.visited:
                        n.visited = True
                        n.parent = node
                        q.enqueue(n)

            # Reverting back the visited status of all nodes to 'not visited'
            for node in self.nodes:
                node.visited = False

            return False

        a = _bfs2(start, end)
        b = _bfs2(end, start)
        if a:
            print 'There is a path between {} and {}: {}'.format(start, end, a)
        if b:
            print 'There is a path between {} and {}: {}'.format(end, start, b)
        if not a and not b:
            print 'There is no path between {} and {}'.format(start, end)


g = Graph([('a', ['b', 'c']),
           ('b', ['c', 'd']),
           ('c', ['e', 'f']),
           ('d', []),
           ('e', []),
           ('f', []),
           ('g', [])])
print g
g.bfs2('a', 'e')
