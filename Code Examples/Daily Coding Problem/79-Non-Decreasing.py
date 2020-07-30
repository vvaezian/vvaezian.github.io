'''
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
'''

# O(n) time, O(1) space

def checkPossibility(nums):
  if len(nums) <= 2:
    return True
      
  def is_non_decreasing(array):
    '''checks if the array is non-decreasing'''
    prev = array[0]
    for i in array[1:]:
        if i < prev:
            return False
        prev = i
    return True

  prev = nums[0]
  count = 0 
  for index, item in enumerate(nums[:-1]):
    if index == 0:
      continue
    if item < prev:
      count += 1
      if count >= 2: # if two times we see decrease in numbers, then the answer is definitely False
        return False
      # we test to see if by removing the problematic numbers the remaining members of array are non-decreasing
      # the problematic numbers are the two numbers that characterize the decrease in value
      if not is_non_decreasing(nums[:index] + nums[index + 1:]) and not is_non_decreasing(nums[:index - 1] + nums[index:]):
        return False
    prev = item

  return True
