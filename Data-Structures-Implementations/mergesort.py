# Mergesort
# runtime: O(nlog(n)), space: O(n)

import time
s = time.time()


def mergesort(array):
    if len(array) == 1:
        return array
    mid = len(array) / 2
    return merge(mergesort(array[:mid]), mergesort(array[mid:]))


def merge(list1, list2):
    output = []
    n, m = 0, 0
    while True:
        if list1[m] < list2[n]:
            output.append(list1[m])
            m += 1
        else:
            output.append(list2[n])
            n += 1
        if not list1[m:]:
            for i in list2[n:]:
                output.append(i)
            break
        elif not list2[n:]:
            for i in list1[m:]:
                output.append(i)
            break
    return output


mergesort(range(1000, 0, -1))
print time.time() - s
