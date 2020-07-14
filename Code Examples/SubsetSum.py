'''
Given an array and an integer k, return whether there is a subset of the array that sums to k.
'''

def subset_sum(array, k):
  array.sort()
  if k > array[-1]:
    return False
  
  # DP
  m = [ [0] * (len(array) + 1) for _ in range(k + 1) ]
  m[0] = [1] * (len(array) + 1)

  for row in range(1, k + 1):
    for col in range(1, len(array) + 1):
      if m[row][col - 1] == 1 or (row - array[col - 1] >= 0 and m[row - array[col - 1]][col - 1] == 1):
        m[row][col] = 1
  
  return True if m[-1][-1] else False

print(subset_sum([2, 5, 7, 12], 9))
