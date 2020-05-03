- A **tree** is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph.
- A **binary tree** is a tree in which each node has up to two children.
- A **complete binary tree** is a binary tree in which every level of the tree is fully filled, except for perhaps the
last level. To the extent that the last level is filled, it is filled left to right.
- A **full binary tree** is a binary tree in which every node has either zero or two children.
- A **perfect binary tree** is one that is both full and complete. All leaf nodes will be at the same level, and this
level has the maximum number of nodes.
- A **binary search tree** is a binary tree in which every node fits a specific ordering property: all left
descendents <= n < all right descendents.
- A **min-heap** is a complete binary tree where each node is smaller than its children.
- A **trie** (sometimes called a **prefix tree**) is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word.  
The * nodes (sometimes called "null nodes") are often used to indicate complete words. The actual implementation of these * nodes might be a special type of child (such as a `TerminatingTrieNode`, which inherits from TrieNode). Or, we could use just a boolean flag `terminates` within the "parent" node.  
Very commonly, a trie is used to store the entire (English) language for quick prefix lookups. While a hash
table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid
words. A trie can do this very quickly.
