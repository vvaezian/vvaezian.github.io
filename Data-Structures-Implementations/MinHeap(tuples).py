# MinHeap of tuples


class MinHeap(object):
    def __init__(self):
        self.items = []

    def insert(self, val):
        self.items.append(val)
        self.heapify_up()

    def extract_min(self):
        self.items[0] = self.items[-1]
        self.items.pop()
        self.heapify_down()

    def get_min(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

    # The rest is for defining heapify

    @staticmethod
    def get_parent(index):
        if index == 0:
            print("Root has no parent")
            return None
        return (index - 1) // 2

    def has_left_child(self, index):
        return 2 * index + 1 < len(self.items)

    def has_right_child(self, index):
        return 2 * index + 2 < len(self.items)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def heapify_up(self):
        cur_index = len(self.items) - 1
        while cur_index > 0:
            par = self.get_parent(cur_index)
            if self.items[par][0] > self.items[cur_index][0]:
                self.swap(par, cur_index)
            cur_index -= 1

    def heapify_down(self):
        cur_index = 0
        while 2 * cur_index + 1 < len(self.items):
            left_child = 2 * cur_index + 1
            if self.has_right_child(cur_index):
                right_child = 2 * cur_index + 2
                child = left_child if self.items[left_child][0] < \
                    self.items[right_child][0] else right_child
            else:
                child = left_child
            if self.items[child][0] < self.items[cur_index][0]:
                self.swap(child, cur_index)
            cur_index += 1


h = MinHeap()
h.insert((20, 'a'))
print(h)
h.insert((30, 'b'))
print(h)
h.insert((10, 'c'))
print(h)
h.insert((15, 'd'))
print(h)
h.insert((18, 'e'))
print(h)
h.insert((25, 'f'))
print(h)
h.extract_min()
print(h)
