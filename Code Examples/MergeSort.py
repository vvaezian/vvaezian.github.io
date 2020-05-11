def merge(sorted_arr1, sorted_arr2):
  a_idx, b_idx = 0, 0
  out = []
  while a_idx < len(sorted_arr1) and b_idx < len(sorted_arr2):
    a_val, b_val = sorted_arr1[a_idx], sorted_arr2[b_idx]
    if a_val < b_val:
      out.append(a_val)
      a_idx += 1
    else:
      out.append(b_val)
      b_idx += 1
  # add the left-overs
  for i in sorted_arr1[a_idx:]:
    out.append(i)
  for i in sorted_arr2[b_idx:]:
    out.append(i)
  return out

def mergesort(array):
  if len(array) <= 1:
    return array
  else:
    mid = len(array) // 2
    return merge(mergesort(array[:mid]), mergesort(array[mid:]))
