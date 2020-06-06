'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
'''

def reg(string, pattern):
  
  # base case
  if len(pattern) == 0:
    return len(string) == 0
  if len(string) == 0:
    return pattern == '' or ( '*' in pattern and len(pattern) % 2 == 0 and  set([ item for index, item in enumerate(pattern) if index % 2 == 1 ]) == {'*'} )
  if len(pattern) == 1:
    return len(string) == 1 and (string[0] == pattern[0] or pattern[0] == '.')

  if pattern[1] != '*':
    if pattern[0] != '.':
      return string[0] == pattern[0] and reg(string[1:], pattern[1:])
    else:
      return reg(string[1:], pattern[1:])
  
  # pattern[1] == '*'
  for str_idx in range(len(string)):
    if string[str_idx] != pattern[0] and pattern[0] != '.':
      break
    if reg(string[str_idx + 1:], pattern[2:]):
      return True
  
  # for the case where zero count of a in a* is used for matching
  return reg(string, pattern[2:])

assert reg("a", "ab*a") is False
assert reg("","c*c*") is True
assert reg('aa','a*') is True
assert reg("a","ab*") is True
assert reg("aab","c*a*b") is True
assert reg('ade','.*de') is True
assert reg("aabcd", "a*bcd") is True
assert reg("ssippi", "p*.") is False
assert reg("sissippi","s*is*p*.") is False
assert reg("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c") is False
