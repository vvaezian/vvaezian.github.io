## Indexing
The primary purpose of an index is to provide an ordered representation of the indexed data.  
Since it is not efficient to store the data sequentially (because an insert statement would need to move the following entries to make room for the new one), we need to establish a logical order that is independent of physical order in memory.  
The logical order is established via a doubly linked list. It is used to connect B-tree leaf nodes. Index is represented as a B-tree. Each leaf node is stored in a database block (or page; the database's smallest storage unit).  
So the index order is maintained on two different levels: the index entries within each leaf node (because B-tree is ordered), and the leaf nodes among each other using a doubly linked list (because linked_lists are ordered).  
