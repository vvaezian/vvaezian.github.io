# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

class Node:
  def __init__(self, key):
    self.key = key
    self.neighbours = set()
    self.dependencyCount = 0


class Graph:
  def __init__(self):
    self.nodes = {}

  def getNodes(self):
    return self.nodes.values()
  
  def addNodeByKey(self, key):
    if key not in self.nodes:
      self.nodes[key] = Node(key)
  
  def addEdge(self, key1, key2):
    self.addNodeByKey(key1)
    self.addNodeByKey(key2)
    self.nodes[key1].neighbours.add(self.nodes[key2])
    self.nodes[key2].dependencyCount += 1
  

def buildOrder(projectList, dependencyList):
  g = Graph()
  for edge in dependencyList:
    g.addEdge(edge[0], edge[1])
  for nodeKey in projectList:
    g.addNodeByKey(nodeKey)
  nodes = g.getNodes()
  buildOrderList = []

  # add those with no dependencies
  for node in nodes:
    if node.dependencyCount == 0:
      buildOrderList.append(node)
  
  # 'delete' the dependecies on nodes without dependency and add the new nodes without dependency in the updated graph 
  # to the buildOrderList. Repeat until no more change.
  index = 0
  while index < len(buildOrderList):  # this is false when new node with dependency 0 is not found, so buildOrderList has not grown
    for node in buildOrderList[index:]: # 'delete' dependecy on nodes without dependency
      for neighbour in node.neighbours:
        neighbour.dependencyCount -= 1
    index = len(buildOrderList)
    for node in nodes:  # add new nodes with dependency zero
      if node not in buildOrderList and node.dependencyCount == 0:
        buildOrderList.append(node)

  if len(buildOrderList) != len(projectList): # if not all nodes has been 'deleted'
    return "There is a loop!"
  return [node.key for node in buildOrderList]

print(buildOrder(['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]))
