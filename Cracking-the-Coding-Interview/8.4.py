# Power Set: Write a method to return all subsets of a set.

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
