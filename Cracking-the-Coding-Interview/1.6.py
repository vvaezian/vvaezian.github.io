# 1.6. String Compression: Implement a method to perform string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than
# the original string, your method should return the original string. You can assume the string has only uppercase and
# lowercase letters (a - z).


def compress(myStr):
  if myStr == "":
    return myStr
  
  compressed = myStr[0] + '1'
  prevChar = myStr[0]
  for char in myStr[1:]:
    if char == prevChar:
      compressed = compressed[:-1] + str(int(compressed[-1]) + 1)
    else:
      compressed += char + '1'
      prevChar = char
  return compressed if len(compressed) < len(myStr) else myStr
