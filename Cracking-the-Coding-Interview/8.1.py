# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs.

def step(n):
  m = [1, 2, 4] # initial values for 1, 2 and 3 steps
  for i in range(3, n):
    m.append(m[i-1] + m[i-2] + m[i-3])
  return m[-1]
