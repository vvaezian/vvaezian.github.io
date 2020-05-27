# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import defaultdict

def is_valid(string, k, dictionary):
  return len([i for i in dictionary if dictionary[i] > 0]) <= k

def lsd(string, k):
  
  # initializing
  substring = string[:k]
  window_dict = defaultdict(int)
  best_start = cur_start = 0
  best_end = cur_end = k - 1
  biggest_size = cur_size = k
  for char in substring:
    window_dict[char] += 1
  
  # sliding the window
  for char in string[k:]:
    if window_dict[char] > 0:
      window_dict[char] += 1
      cur_size += 1
      cur_end += 1
      if cur_size > biggest_size:
        biggest_size = cur_size
        best_start, best_end = cur_start, cur_end
    else:
      window_dict[char] += 1
      window_dict[string[cur_start]] -= 1
      cur_end += 1
      cur_start += 1
      while not is_valid(string[cur_start:cur_end + 1], k, window_dict):
        window_dict[string[cur_start]] -= 1
        cur_start += 1
        cur_size -= 1

  return best_start, best_end
