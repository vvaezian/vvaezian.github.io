'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
'''

# O(n) time, O(1) space

def largest_product(array):
  maxA, maxA_idx = max([ (item, index) for index, item in enumerate(array) ])
  maxB, maxB_idx = max([ (item, index) for index, item in enumerate(array) if index != maxA_idx ])
  maxC, maxC_idx = max([ (item, index) for index, item in enumerate(array) if index not in [maxA_idx, maxB_idx] ])
  minA, minA_idx = min([ (item, index) for index, item in enumerate(array) ])
  minB, minB_idx = min([ (item, index) for index, item in enumerate(array) if index != minA_idx ])
  
  return max(maxA * maxB * maxC, maxA * minA * minB)
