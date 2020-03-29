# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

# iterative approach

def findPath(maze):
  """ maze is a 2-dimentional array consisting of 1's and 0's where 0's represent "off limit" cells."""
  path = [[0]*len(maze[0]) for _ in range(len(maze))] # holding a path to each cell 
                                                      # ('D' means 'Down', 'R' mean 'Right', 'None' if no path, '' for start cell)
  path[0][0] = ''

  # setting first column cells
  for r_index in range(1, len(maze)):
    path[r_index][0] = path[r_index - 1][0] + 'D' if maze[r_index - 1][0] != 0 and path[r_index - 1][0] is not None else None

  # setting first row cells
  for c_index in range(1, len(maze[0])):
    path[0][c_index] = path[0][c_index - 1] + 'R' if maze[0][c_index - 1] != 0 and path[0][c_index - 1] is not None else None

  # setting other cells
  for r_index in range(1, len(maze)):
    for c_index in range(1, len(maze[0])):
      if maze[r_index - 1][c_index] != 0 and path[r_index - 1][c_index] is not None:
        path[r_index][c_index] =  path[r_index - 1][c_index] + 'D'
      elif maze[r_index][c_index - 1] != 0 and path[r_index][c_index - 1] is not None:
        path[r_index][c_index] =  path[r_index][c_index - 1] + 'R'
      else:
        path[r_index][c_index] = None
  return path[-1][-1]

print(findPath([[1,0,1],[1,1,1],[1,1,1]]))  # DRRD
