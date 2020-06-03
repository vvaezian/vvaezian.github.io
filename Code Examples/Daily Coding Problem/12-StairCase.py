'''
There exists a staircase with N steps, and you could climb any number from a set of positive integers X
Given N and X, write a function that returns the number of unique ways you can climb the staircase.
'''

def stairs_with_steps(n, steps):
  # Since we want to look back at most max(steps) steps, 
  # we add this many zeros more so we don't run out of index.
  m = [0] * (max(steps) + n)  # the cache

  for i in range(max(steps), n + max(steps)):
    for s in steps:
      m[i] += m[i - s]
    if i - max(steps) + 1 in steps:
      m[i] += 1
  
  return m[-1]
