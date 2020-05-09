# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs.

# O(n) time, O(n) space
def step(n):
  m = [1, 2, 4] # initial values for 1, 2 and 3 steps
  if n < 4:
    return m[n -1]
  
  for i in range(3, n):
    m.append(m[i-1] + m[i-2] + m[i-3])
  return m[-1]

# O(n) time, O(1) space
def step2(n):
  if n < 4:
    return [1, 2, 4][n - 1]
  
  a, b, c = 1, 2, 4
  for _ in range(3, n):
    d = a + b + c
    a, b, c = b, c, d
  return d

#######################
###### Recursive ######
#######################

# O(n) time, O(n) space
def stairs(n, mem=None):
  '''we regard n as the number of steps left to climb
  '''
  # make a list of zeros to act as a cache
  if mem is None:
    mem = [0]*n
  # if the value is in the cache return it
  if mem[n-1] != 0:
    return mem[n-1]
  # base cases
  if n == 1 or n == 2:
    mem[n-1] = n
    return n
  if n == 3:
    mem[n-1] = 4
    return 4
  # recursive step
  mem[n-1] = stairs(n - 1, mem) + stairs(n - 2, mem) + stairs(n - 3, mem)
  return mem[n-1]
