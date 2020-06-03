'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

# One straightforward solution is to put all starts and ends in a list, sort the list, read the list, 
# whenever we see a starting point add to the number of rooms and whenever we see an end point decrase the number of rooms by 1.
# Time O(n), Space O(n)
def min_room(array):
  array = [ (i[0], 's') for i in array ] + [ (i[1], 'e') for i in array ]
  array.sort()

  rooms, max_occupied_rooms = 0, 0
  for item in array:
    if item[1] == 's':
      rooms += 1
      if rooms > max_occupied_rooms:
        max_occupied_rooms = rooms
    else:
      rooms -= 1
  
  return max_occupied_rooms
