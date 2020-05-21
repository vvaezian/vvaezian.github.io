# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# E.g. [2, 4, 6, 2, 5] should return 13.

# Analysis: Let opt(n) be the solution for an array of n numbers. Either the nth element is part of the solution or not. 
# If it isn't, then opt(n) = opt(n-1)
# If it is, then the (n-1)th number cannot be chosen. We have two cases: opt(n) = n + opt(n - 2) or opt(n) = n + opt(n-3)
# E.g. if we have [1, 10, 2, 5, 10] the second case happens

# O(3^n) time, O(1) space
def max_disjoint_sum(array):

  def helper(arr, i):
    if i == 0:
      return arr[0]
    if i == 1:
      return max(arr[0], arr[1])
    if i == 2:
      return max(arr[0] + arr[2], arr[1])
    return max(helper(arr, i-1) # if last_element is not part of the solution
              , max(arr[i] + helper(arr, i-2) 
                  , arr[i] + helper(arr, i-3))
            )

  return helper(array, len(array) - 1)



# O(n) time, O(n) space (memoization) 
# recursive version can use memoization as well, but the iterative approach is simpler
def max_disjoint_sum(arr):
  m = [0] * len(arr)
  m[0] = arr[0]
  m[1] = max(arr[0], arr[1])
  m[2] = max(arr[0] + arr[2], arr[1])
  for i in arr[3:]:
    m[i] = max(m[i-1], max(arr[i] + m[i-2], arr[i] + m[i-3]))
  return m[-1]

# O(n) time, O(1) space (memoization and space-efficient)
# since we are only looking at last three elements of m, we don't need to use the whole  m
def max_disjoint_sum(arr):
  a = arr[0]
  b = max(arr[0], arr[1])
  c = max(arr[0] + arr[2], arr[1])
  for i in arr[3:]:
    new_val = max(c, max(arr[i] + b, arr[i] + a))
    a, b, c = b, c, new_val
  return c
