# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8]

# Method 1: O(n) time, O(n) space
# (This doesn't work for streaming data)
# Analysis: If we devide the list in k chunks and calculate max in each chunk separately forward and backward,
# then max(array[i], array[i + k - 1]) gives the desired result.
# The reason is explained using the following example: To get the max for the window [2  3 | 1  5], 
# we can get the max of [2 3] and max of [1 5], and return the bigger of the two. 
# Max of [ 2 3 ] is calculated in LR and max of [ 1 5 ] is calculated in RL pass. 
#     [5, 6, 2, 3 | 1, 5, 1, 4 ]
# LR:  5  6  6  6 | 1  5  5  5 
# RL:  6  6  2  3 | 5  5  4  4  
#      6  6  5  4   5    

# Method 2: O(n) time, O(k) space
# Analysis: We use a deque to store index of useful element. The index of the current max is kept at the leftmost element of queue.
# In the following explanation we say value of the element is in the deque, while if fact the index of that element is in the deque. 
# We do this to simplify the explanation:
# Let's say {5, 3, 2} are already in the deque. 
# If the next element we read from the array is bigger than 5 (remeber, the leftmost elemet of deque holds the max), say 7: We delete the deque and create a new one with only 7 in it
# If the next element is less than 2, say 1: We add it to the right ({5, 3, 2, 1})
# If the next element is bigger than 2 but less than 5, say 4: We remove element from right that are smaller than the element and then add the elemet from right ({5, 4}).
# Also we keep elements of the current window only.

from collections import deque

def max_subarray(array, k):
  deq = deque()

  for index, item in enumerate(array):

    if len(deq) == 0:
      deq.append(index)

    elif index - deq[0] >= k:  # the max element is out of the window
      deq.popleft()

    elif item > array[deq[0]]:  # found a new max
      deq = deque()
      deq.append(index)

    elif item < array[deq[-1]]:  # the array item is smaller than all the deque elements
      deq.append(index)

    elif item > array[deq[-1]] and item < array[deq[0]]:
      while item > array[deq[-1]]:
        deq.pop()
      deq.append(index)

    if index >= k - 1:  # start printing when the first window is filled
      print(array[deq[0]])
