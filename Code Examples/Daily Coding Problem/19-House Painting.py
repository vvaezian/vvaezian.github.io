# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
# return the minimum cost which achieves this goal.

# for each house we either choose the current first best cost, or the current second best cost. 
# E.g. in the below setting the optimal solution is to use the color with the second-best cost:
# a = [
#      [2, 3, 6, 1],
#      [4, 6, 8, 2],
#      [3, 4, 3, 5],
#      [2, 4, 5, 3]
#     ]
# We recursively try both approaches, then choosing the better one

# without memoization
def min_cost(array):

  def _min_cost(array, last_color_index=None):
    if len(array) == 0:
      return 0
    
    first_best_cost, second_best_cost = float('inf'), float('inf')
    first_best_cost_index, second_best_cost_index = None, None
    for index, item in enumerate(array[0]):
      if index != last_color_index:
        if item < first_best_cost:
          first_best_cost, second_best_cost = item, first_best_cost
          first_best_cost_index, second_best_cost_index = index, first_best_cost_index
        elif item < second_best_cost:
          second_best_cost = item
          second_best_cost_index = index
    
    return min( first_best_cost + _min_cost(array[1:], first_best_cost_index)
              , second_best_cost + _min_cost(array[1:], second_best_cost_index)
              ) 

  return _min_cost(array)

# with memoization
