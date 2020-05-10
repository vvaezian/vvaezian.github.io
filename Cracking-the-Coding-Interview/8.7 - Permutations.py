# Permutations without Dups: Write a method to compute all permutations of a string of unique characters.


def insertChar(char, array):
  out = []
  for string in array:
    for i in range(len(string) + 1):
      out.append(string[:i] + char + string[i:])
  return out
    

def perm(string):
  if len(string) == 1:
    return string
  return insertChar(string[0], perm(string[1:]))
