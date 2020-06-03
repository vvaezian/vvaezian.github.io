'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
'''

# Solution using stack
# AAdd words in a greedy fashion, if not all characters of the string are used, backtrack and continue
def extract_sentence(dictionary, string):
  min_len, max_len = min([ len(i) for i in dictionary ]), max([ len(i) for i in dictionary ])
  cur_sentence = []
  start_idx = 0
  def _extract_sentence(cur_sentence=cur_sentence, start_idx=start_idx, excluded_item=None):
    length = min_len
    while start_idx < len(string) and min_len <= length <= max_len:
      substring = string[start_idx:start_idx + length]
      if substring != excluded_item and substring in dictionary:
        cur_sentence.append( (start_idx, string[start_idx:start_idx + length]) )
        start_idx += length
        length = min_len
      else:
        length += 1
    if cur_sentence[-1][1][-1] == string[-1]:
      return [ i[1] for i in cur_sentence ]
    start_idx, excluded_item = cur_sentence.pop()
    return _extract_sentence(cur_sentence, start_idx, excluded_item)

  return _extract_sentence(cur_sentence, start_idx)
