# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

def loopDetect(head):
  aDict = {}
  cur = head
  aDict[cur] = 1
  while cur.nxt:
    if cur.nxt in aDict:
      return cur.nxt
    cur = cur.nxt
    aDict[cur] = 1
  print("There is no loop")


a = Node(7)
b = Node(1)
c = Node(4)
a.nxt = b
b.nxt = c
c.nxt = b
loopDetect(a)
