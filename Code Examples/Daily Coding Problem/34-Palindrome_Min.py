'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible 
anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the 
lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it 
(which is the smallest amount to make a palindrome). There are seven other palindromes that can be made 
from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

```python
def palindrome_min(string):
  return helper(string, {})

def helper(string, cache):
  # cache hit
  if string in cache:
    return cache[string]
  
  # base case
  if len(string) <= 1:
    return string
  
  # if first and last are the same we don't need to insert anything
  if string[0] == string[-1]:
    return string[0] + helper(string[1:-1], cache) + string[-1]
  
  # for the string [1..n] find which one of [2..n] or [1..n-1] is the shorter palindrome
  # and return it together with the appropriate letter padded at both sides
  # if they are the same length return the one that its padding is lexicography earlier
  n1 = helper(string[1:], cache)
  cache[string[1:]] = n1
  n2 = helper(string[:-1], cache)
  cache[string[:-1]] = n2
  if len(n1) < len(n2):
    return string[0] + n1 + string[0]
  if len(n2) < len(n1):
    return string[-1] + n2 + string[-1]
  # This part if for returning the lexicographically earliest one
  if len(n1) == len(n2):
    return string[0] + n1 + string[0] if string[0] < string[-1] else string[-1] + n2 + string[-1]

print(palindrome_min('race'))
```
