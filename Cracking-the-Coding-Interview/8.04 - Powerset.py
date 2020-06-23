# Power Set: Write a method to return all subsets of a set.


### Recursive
def powerset(array):

  def _powerset(array, out):
    if len(array) == 0:
      return [[]]
    for item in [ i + [array[-1]] for i in _powerset(array[:-1], out) ]:
      out.append(item)
    return out
  
  return _powerset(array, [[]])


### Iterative
def powerset(array):
    import copy
    output = [[]]
    for i in array:
        tmp = copy.deepcopy(output)
        for j in tmp:
            j.append(i)
            output.append(j)
    return output

print(powerset(['a', 'b', 'c']))
