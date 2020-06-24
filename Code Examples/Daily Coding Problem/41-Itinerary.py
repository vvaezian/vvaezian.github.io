'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, 
compute the person's itinerary. If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. 
All flights must be used in the itinerary.
'''

### Analysis: We use a dictionary to map sources to destinations. We also include a flag with the destination indicating 
# whether it has been visited. For example for ('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A') initially we have
# { 'A':[['B', 0], ['C', 0]],
#   'B':[['C', 0]],
#   'C':[['A', 0]]
# }
# We then recursively add points to the path, looking in the dict values for the next point.
# The program runs in O(n) time and O(k) space where k is the maximum number of duplicate destinations (practically O(1))

from collections import defaultdict

def itinerary(flight_list, start):
  hash_table = defaultdict(list)
  # key is source, value is a list of pairs [a, b] where a is the destination 
  # and be is either 0 or 1 indicating whether a has been visited
  for pair in flight_list:
    hash_table[pair[0]].append([pair[1], 0])
  # sort the values to make sure we return solution in lexicographic order
  for value_list in hash_table.values():
    if len(value_list) > 1:
      value_list.sort()

  path = helper(start, hash_table)
  return path if len(path) == len(flight_list) + 1 else None


def helper(cur_point, hash_table):

  # finding the next point in lexicographic order
  next_point = None
  for item in hash_table[cur_point]:
    point, visited = item
    if visited == 0:
      item[1] = 1
      next_point = point
      break

  if not next_point:
    return [cur_point]

  return [cur_point] + helper(next_point, hash_table)


print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
