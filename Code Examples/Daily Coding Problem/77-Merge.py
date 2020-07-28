'''
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''


def merge(array):
  if len(array) < 2:
    return array
  
  array.sort()
  output = [ array[0] ]
  
  for interval in array[1:]:
    start, end = interval
    last = output[-1]
    if start < last[1]:
      if last[1] < end:
        last[1] = end
      continue

    output.append(interval)

  return output
