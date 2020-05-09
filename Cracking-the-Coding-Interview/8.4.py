# Power Set: Write a method to return all subsets of a set.


### Recursive
def subset(array):

  def _subset(array, out):
    if len(array) == 0:
      return [[]]
    for item in [ i + [array[-1]] for i in _subset(array[:-1], out) ]:
      out.append(item)
    return out
  
  return _subset(array, [[]])


### Iterative
def subsets(list1):
    import copy
    output = [[]]
    for i in list1:
        tmp = copy.deepcopy(output)
        for j in tmp:
            j.append(i)
            output.append(j)
    return output

print(subsets(['a', 'b', 'c']))
