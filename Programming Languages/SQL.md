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

### B-tree Traversal
In the general case, 
1. the database software starts traversing the B-tree to find the first matching entry at the leaf node level. 
2. It then follows the doubly linked list until it has found all matching entries.
3. Finally it fetches each of those matching entries from the table. (the last two steps can be interleaved)

![index B-tree](https://use-the-index-luke.com/static/fig01_03_tree_traversal.en.niC7Q5jq.png) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![traverse](/Pic/index1.png)

Estimates of read operations for each step: (assuming 100 index entries per page/block)

1. The B-tree: `log100([rows in table])`, often less than 5
2. The doubly linked list: `[rows read from index] / 100`
3. The table: `[rows read from table]`

Worst case scenario: all rows of interest are in different blocks, i.e. the worst possible clustering factor.

### index-only scans

```SQL
SELECT SUM(col2)
FROM tbl
WHERE col1 = ?
```

### `include` statement
*PostgreSQL since release 11 supports include statement.*  
  
The include clause allows us to make a distinction between columns we would like to have in the entire index (key columns) and columns we only need in the leaf nodes (include columns).  
That means it allows us to remove columns from the non-leaf nodes if we don’t need them there.  
This results in shallower B-tree smaller index size. But the most important effect is that it can make the index an *index-only scan* (aka *covering index*), meaning that the quert doesn't need to access the table as all the data is in the index.  
![include](/Pic/index2.png)

```SQL
CREATE INDEX idx
ON tbl ( col1 )
INCLUDE ( col2 )
```
Note that the order of the leaf node entries does not take the include columns into account. The index is solely ordered by its key columns.
