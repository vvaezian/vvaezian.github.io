# Since heapq methods work for MinHeap, here for MaxHeap we use them for negated values.
# At the end we negate again to get the desired output.

# If values are not numbers (int, float) we need to redefine __lt__ (see https://stackoverflow.com/a/40455775/2445273).

from heapq import heappop, heappush


class MaxHeap(object):
    def __init__(self):
        self.items = []

    def insert(self, val):
        heappush(self.items, -val)

    def extract_min(self):
        heappop(self.items)

    def get_min(self):
        return -self.items[0]

    def __str__(self):
        return str([-x for x in self.items])


h = MaxHeap()
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
