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
# Analysis: 
