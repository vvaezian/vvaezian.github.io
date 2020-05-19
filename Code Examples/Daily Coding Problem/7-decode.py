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
