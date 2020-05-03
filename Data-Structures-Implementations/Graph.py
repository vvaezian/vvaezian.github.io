from Queue import Queue


class Node(object):
    def __init__(self, key, neighbours):
        self.key = key
        self.neighbors = neighbours
        self.visited = False
        self.parent = None  # Is needed for finding the shortest path using BFS

def dfs(n):
  print(n.key) 
  n.visited = True
  for node in n.neighbors:
    if not node.visited:
      dfs(node)

def bfs(n):
  q = Queue()
  q.enq(n)
  n.visited = True

  while not q.isEmpty():
    node = q.deq()
    print(node.val)
    for neighbor in node.neighbors:
      if not neighbor.visited:
        q.enq(neighbor)
        neighbor.visited = True

        
def unidirectional_search(s, t):
  
  def extract_path(node):
    path = []
    while node:
      path.append(node.val)
      node = node.parent
    return path[::-1]
  
  q = Queue()
  q.enqueue(s)

  while not q.isEmpty():
    n = q.dequeue()
    n.visited = True

    if n is t:
      return extract_path(n)
    
    for node in n.neighbors:
      if not node.visited:
        q.enqueue(node)
        node.parent = n
    
  return False


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n0.neighbors = [n1, n4, n5]
n1.neighbors = [n3, n4]
n2.neighbors = [n1]
n3.neighbors = [n2, n4]
dfs(n0)
bfs(n0)
print(unidirectional_search(n0, n2))

######## Bidirectional Search ############
class Node:
  def __init__(self, val, neighbors=[]):
    self.val = val
    self.neighbors = neighbors
    self.visited_right = False  # whether the node was reached by the BFS that started from source
    self.visited_left = False  # whether the node was reached by the BFS that started from destination
    self.parent_right = None  # used for retrieving the final path from start to the meeting point
    self.parent_left = None  # used for retrieving the final path from the meeting point to destination


def bidirectional_search(s, t):
  
  def extract_path(node):
    """return the path when both BFS's have met"""
    node_copy = node
    path = []
    
    while node:
      path.append(node.val)
      node = node.parent_right
    
    path.reverse()
    del path[-1]  # because the meeting node appears twice
    
    while node_copy:
      path.append(node_copy.val)
      node_copy = node_copy.parent_left
    return path
  
  q = Queue()
  q.enqueue(s)
  q.enqueue(t)
  s.visited_right = True
  t.visited_left = True
  
  while not q.isEmpty():
    n = q.dequeue()

    if n.visited_left and n.visited_right:  # if the node visited by both BFS's
      return extract_path(n)
    
    for node in n.neighbors:
      if n.visited_left == True and not node.visited_left:
        node.parent_left = n
        node.visited_left = True
        q.enqueue(node)
      if n.visited_right == True and not node.visited_right: 
        node.parent_right = n
        node.visited_right = True
        q.enqueue(node)
    
  return False

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n0.neighbors = [n1, n5]
n1.neighbors = [n0, n2, n6]
n2.neighbors = [n1]
n3.neighbors = [n4, n6]
n4.neighbors = [n3]
n5.neighbors = [n0, n6]
n6.neighbors = [n1, n3, n5, n7]
n7.neighbors = [n6]
print(bidirectional_search(n0, n4))
