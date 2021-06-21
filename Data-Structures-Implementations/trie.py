class TrieNode:
  def __init__(self):
    #Dict: Key = letter, Item = TrieNode
    self.children = {}
    self.end = False
    
    
class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, name, name_id):
    node = self.root
    for char in name:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.end = True
    
  def search(self, name):
    node = self.root
    for char in name:
      if char in node.children:
        node = node.children[char]
      else:
        return None
    return node.end
