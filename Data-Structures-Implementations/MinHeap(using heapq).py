from heapq import heappop, heappush


class MinHeap(object):
    def __init__(self):
        self.items = []

    def insert(self, val):
        heappush(self.items, val)

    def extract_min(self):
        heappop(self.items)

    def get_min(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


h = MinHeap()
h.insert(20)
print h
h.insert(30)
print h
h.insert(10)
print h
h.insert(15)
print h
h.insert(18)
print h
h.insert(25)
print h
h.extract_min()
print h
