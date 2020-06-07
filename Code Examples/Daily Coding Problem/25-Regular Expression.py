'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
'''


################################################
### Method 1: Recursive (non-efficient) solution
################################################

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


########################################
### Method 2: DP O(mn time), O(mn) space
########################################
# This video is helpful for the explanation: https://www.youtube.com/watch?v=l3hda49XcDE
# Although it doesn't cover how to initialize the first row if the pattern starts with x*.
# in these cases we need to set the value of the cell corresponding to * to True if in the
# two cell prior we have True.

def reg(string, pattern):
  
  # Initializing the matrix
  m = [ [False] * (len(pattern) + 1) for _ in range(len(string) + 1) ]
  m[0][0] = True
  # the following is explained above
  for index, char in enumerate(pattern):
    if char == '*':
      m[0][index + 1] = m[0][index - 2 + 1]

  for s_idx, s_char in enumerate(string):
    m_s_idx = s_idx + 1
    for p_idx, p_char in enumerate(pattern):
      m_p_idx = p_idx + 1
      if p_char != '*':
        m[m_s_idx][m_p_idx] = m[m_s_idx - 1][m_p_idx - 1] if p_char == s_char or p_char == '.' else False
      else:
        if m[m_s_idx][m_p_idx - 2] == True:
          m[m_s_idx][m_p_idx] = True
        else:
          if pattern[p_idx - 1] == string[s_idx] or pattern[p_idx - 1] == '.':
            m[m_s_idx][m_p_idx] = m[m_s_idx - 1][m_p_idx]
  
  return m[-1][-1]


#######################################
### Method 3: DP O(mn) time, O(n) space
#######################################
# We don't need the whole matrix for the calculations.
# We keep two rows only
def reg(string, pattern):
  
  m = [ [False] * (len(pattern) + 1) for i in range(min(2, len(string) + 1)) ]
  m[0][0] = True
  for index, char in enumerate(pattern):
    if char == '*':
      m[0][index + 1] = m[0][index - 2 + 1]

  for s_idx, s_char in enumerate(string):
    for p_idx, p_char in enumerate(pattern):
      m_p_idx = p_idx + 1
      if p_char != '*':
        m[1][m_p_idx] = m[0][m_p_idx - 1] if p_char == s_char or p_char == '.' else False
      else:
        if m[1][m_p_idx - 2] == True:
          m[1][m_p_idx] = True
        else:
          if pattern[p_idx - 1] == string[s_idx] or pattern[p_idx - 1] == '.':
            m[1][m_p_idx] = m[0][m_p_idx]

    if s_idx != len(string) - 1: # We don't want to swap the rows at the end, becuase it messes up the return value
      m[0], m[1] = m[1], [False] * (len(pattern) + 1)
  
return m[-1][-1]


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
