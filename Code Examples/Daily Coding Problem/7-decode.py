# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# recursive O(n) runtime, O(n) space
def decode(string:str) -> int:

  def _decode(string:str, n:int, cache:dict) -> int:
    if n == 0 or n == 1: 
      cache[n] = 1
      return 1
    count = 0
    if 1 <= int(string[n-1]) <= 9:  # if the last character is valid
      # count = cache.get(n-1, _decode(string, n - 1, cache)) first evaluates the _decode
      # because .get like any other func first evaluates its args. So the cache becomes irrelevant
      count = cache.get(n-1) or _decode(string, n - 1, cache)
    if 10 <= int(string[n - 2: n]) <= 26:  # if the last two characters are valid
      count += cache.get(n-2) or _decode(string, n - 2, cache) 
    
    cache[n] = count
    return count
    
  return _decode(string, len(string), {})

# iterative O(n) runtime, O(n) space
def decode(string:str) -> int:
  m = [1] * (len(string) + 1)  # m[i] is for the solution for the first i characters of string
  if int(string[0]) == 0:
    return 0
  for i in range(2, len(string) + 1):
    count = 0
    if int(string[i-1]) > 0:
      count = m[i - 1]
    if 10 <= int(string[i - 2:i]) <= 26:
      count += m[i - 2]
    m[i] = count
  return m[-1]

# iterative O(n) runtime, O(1) space
