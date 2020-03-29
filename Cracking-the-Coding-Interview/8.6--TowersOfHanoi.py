# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.

class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

def other_tower(tower1, tower2):
    """given two towers (= stacks), returns the other tower"""
    return [i for i in stacks if i not in [tower1, tower2]][0]

def move(i, j):  # moves the top disk in tower i, to tower j
    tmp = i.pop()
    j.push(tmp)

def hanoi(n, i, j):  # moves the n top disks from tower i to tower j
    if n == 1:
        move(i, j)
    else:
        other = other_tower(i, j)
        hanoi(n - 1, i, other)
        move(i, j)
        hanoi(n - 1, other, j)

s1 = Stack()
s2 = Stack()
s3 = Stack()
stacks = [s1, s2, s3]
s1.push('XL')
s1.push('L')
s1.push('M')
s1.push('S')
s1.push('XS')
hanoi(s1.size(), s1, s3)

# Let d(n) be the number of moves required for n disks. Then we have d(n) = 2 * d(n-1) + 1, d(1) = 1. This results in d(n) = 2^n - 1
