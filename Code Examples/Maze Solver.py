import random
import time
from colorama import Fore


class Node(object):
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.visited = False
        self.parent = None


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class Graph(object):
    """"nodes are given as an adjacency list"""
    def __init__(self, adj_list):
        self.nodes = [Node(index, item) for index, item in enumerate(adj_list)]

    def bfs(self, start, end):
        q = Queue()
        s = self.nodes[start]
        s.visited = True
        q.enqueue(s)
        while not q.is_empty():
            node = q.dequeue()
            if node.name == end:
                path = []
                while True:
                    path.append(node.name)
                    if not node.parent:  # reached root node
                        path.reverse()
                        break
                    node = node.parent
                return path
            for i in node.neighbors:
                n = self.nodes[i]
                if not n.visited:
                    n.visited = True
                    n.parent = node
                    q.enqueue(n)
        return


def rename_func(a_maze):
    a_dict = {}
    counter = 0
    for r in range(len(a_maze)):
        for c in range(len(a_maze[0])):
            a_dict[(r, c)] = counter
            counter += 1
    return a_dict


def create_adj_list(a_maze):
    "a_maze is a two-dimensional list with elements 1 and 0"""
    adj_list = []
    for r in range(len(a_maze)):
        for c in range(len(a_maze[0])):
            tmp = []
            if r - 1 >= 0 and a_maze[r - 1][c]:
                tmp.append(myDict[(r - 1, c)])
            if r + 1 < len(a_maze) and a_maze[r + 1][c]:
                tmp.append(myDict[(r + 1, c)])
            if c - 1 >= 0 and a_maze[r][c - 1]:
                tmp.append(myDict[(r, c - 1)])
            if c + 1 < len(a_maze[0]) and a_maze[r][c + 1]:
                tmp.append(myDict[(r, c + 1)])
            adj_list.append(tmp)
    return adj_list


def generate_maze(r, c):
    a_maze = [[1] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if random.uniform(0.3, 1) < 0.5:
                a_maze[i][j] = 0
    a_maze[0][0] = 1
    a_maze[r - 1][c - 1] = 1
    return a_maze


def find_path(a_maze):
    adj_list = create_adj_list(a_maze)
    g = Graph(adj_list)
    path = g.bfs(myDict[(0, 0)], myDict[(row - 1, col - 1)])
    if not path:
        print 'There is no path'
    else:
        for i in range(row):
            for j in range(col):
                if myDict[(i, j)] in path:
                    print Fore.GREEN + str(a_maze[i][j]) + Fore.RESET,
                else:
                    print str(a_maze[i][j]),
            print


row = 10
col = 80
maze = generate_maze(row, col)
myDict = rename_func(maze)  # turning coordinations to numbers.
#                             E.x. (0,0) -> 0, (0, 1) -> 1, ...

starting_time = time.time()
find_path(maze)
print time.time() - starting_time
