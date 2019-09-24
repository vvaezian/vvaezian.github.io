## Indexing ([source](https://use-the-index-luke.com/))
The primary purpose of an index is to provide an ordered representation of the indexed data.  
Since it is not efficient to store the data sequentially (because an insert statement would need to move the following entries to make room for the new one), we need to establish a logical order that is independent of physical order in memory.  
The logical order is established via a doubly linked list. It is used to connect B-tree leaf nodes. Index is represented as a B-tree. Each leaf node is stored in a database block (or page; the database's smallest storage unit).  
So the index order is maintained on two different levels: the index entries within each leaf node (because B-tree is ordered), and the leaf nodes among each other using a doubly linked list (because linked_lists are ordered).  
The table data is stored in a heap structure and is not sorted at all. 

![index-table-connection](https://use-the-index-luke.com/static/fig01_01_index_leaf_nodes.en.MMHwYDFb.png))

So I think there are three levels here: 
1. Physical storage that has the bits in the storage.
2. The heap that holds the records and has pointers to phisycal storage
3. The linked list at the B-tree's leaf node which has connections with the heap.

![index B-tree](https://use-the-index-luke.com/static/fig01_02_tree_structure.en.BdEzalqw.png)
