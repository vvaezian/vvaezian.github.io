class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.size() == 0

    def push(self, m):
        self.items.append(m)

    def pop(self):
        if self.is_empty():
            print "The list is empty"
        else:
            self.items.pop()

    def peek(self):
        if self.is_empty():
            print "The List is Empty"
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


s = Stack()
s.push(6)
s.push(3)
s.push(4)
s.push(1)
print s
s.pop()
print s
