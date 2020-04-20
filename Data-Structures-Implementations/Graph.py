from Queue import Queue


class Node(object):
    def __init__(self, key, neighbours):
        self.key = key
        self.neighbors = neighbours
        self.visited = False
        self.parent = None  # Is needed for finding the shortest path using BFS

def dfs(root):
  if root is None:
    return
  else:
    if not root.visited:
      print(root.val)
      root.visited = True
      for node in root.neighbors:
        dfs(node)

def bfs(root):
  q = Queue()
  q.enqueue(root)

  while not q.isEmpty():
    n = q.dequeue()
    print(n.val) 
    n.visited = True
    for node in n.neighbors:
      if not node.visited:
        q.enqueue(node)

        
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
