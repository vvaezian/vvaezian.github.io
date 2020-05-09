# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.

def hanoi(stacks):

  def move(i, j):
    item = stacks[i].pop()
    stacks[j].append(item)

  def _hanoi(i, j, n):
    '''move the top n disks from tower i to tower j'''
    if n == 1:
      move(i, j)  
    else:
      other_stack_num = 3 - i - j
      _hanoi(i, other_stack_num, n - 1)
      move(i, j)
      _hanoi(other_stack_num, j, n - 1)
    return stacks
    
  return _hanoi(0, 2, len(stacks[0]))

a, b, c = ['XXL', 'XL', 'L', 'M', 'S', 'XS', 'XXS'], [], []
stacks = [a, b, c]

print(hanoi(stacks))

# Let d(n) be the number of moves required for n disks. Then we have d(n) = 2 * d(n-1) + 1, d(1) = 1. This results in d(n) = 2^n - 1
