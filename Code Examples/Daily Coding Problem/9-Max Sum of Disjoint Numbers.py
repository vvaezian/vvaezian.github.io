# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# E.g. [2, 4, 6, 2, 5] should return 13.


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

# O(n) time, O(n) space

# O(n) time, O(1) space
