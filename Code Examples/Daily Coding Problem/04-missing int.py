'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def missing_int(array):
  
  for item in array:
    if type(item) == int and item > 0 and item <= len(array):
      array[item - 1] = (array[item - 1], True)
      continue
    if type(item) == tuple and item[0] > 0 and item[0] <= len(array):
      array[item[0] - 1] = (array[item[0] - 1], True)
  
  for index, item in enumerate(array):
    if type(item) == int:
      return index + 1   
  
  return len(array) + 1
