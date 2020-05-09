def bi_search(x, array):

  def _bi_search(lo, hi):
    if lo > hi:
      return False
            
    mid = (lo + hi) // 2
    if  array[mid] == x:
      return mid
    elif x < array[mid]:
      return _bi_search(lo, mid - 1)
    else:
      return _bi_search(lo + 1, hi)

  if len(array) == 0:
    return False
  return _bi_search(0, len(array) - 1)

