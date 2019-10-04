# Indexing ([source](https://use-the-index-luke.com/))
The primary purpose of an index is to provide an ordered representation of the indexed data. This reduces the read time, but increase the write time, as the order need to be preserved.   
Since it is not efficient to store the data sequentially (because an insert statement would need to move the following entries to make room for the new one), we need to establish a logical order that is independent of physical order in memory.  
The logical order is established via a doubly linked list. It is used to connect B-tree leaf nodes. Index is represented as a B-tree. Each leaf node is stored in a database block (or page; the database's smallest storage unit).  
So the index order is maintained on two different levels: the index entries within each leaf node (because B-tree is ordered), and the leaf nodes among each other using a doubly linked list (because linked_lists are ordered).  
The table data is stored in a heap structure and is not sorted at all. 

<img src="https://use-the-index-luke.com/static/fig01_01_index_leaf_nodes.en.MMHwYDFb.png" width="600">

So I think there are three levels here: 
1. Physical storage that has the bits in the storage.
2. The heap that holds the records and has pointers to phisycal storage
3. The linked list at the B-tree's leaf node which has connections with the heap.

<img src="https://use-the-index-luke.com/static/fig01_02_tree_structure.en.BdEzalqw.png" width="600">

## B-tree Traversal
In the general case, 
1. the database software starts traversing the B-tree to find the first matching entry at the leaf node level. 
2. It then follows the doubly linked list until it has found all matching entries.
3. Finally it fetches each of those matching entries from the table. (the last two steps can be interleaved)

<img src="https://use-the-index-luke.com/static/fig01_03_tree_traversal.en.niC7Q5jq.png" width="400">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/Pic/index1.png" width="600">

Estimates of read operations for each step: (assuming 100 index entries per page/block)

1. The B-tree: `log100([rows in table])`, often less than 5
2. The doubly linked list: `[rows read from index] / 100`
3. The table: `[rows read from table]`

Worst case scenario: all rows of interest are in different blocks, i.e. the worst possible clustering factor.

## Multi-Column index
This is when index is defined on multiple columns. 
```SQL
CREATE INDEX idx_1
ON tbl ( col1, col2 )
```
Note that the order of columns is important. The index is used for queries on `col1, col2` or on `col1` only.  
It is like the phone book. It is sorted by lastName, FirstName, PhoneNumber. We cannot search by firstName at first.

## index-only scans
index-only scan (aka *covering index*), means that the quert doesn't need to access the table as all the data is in the index.  
Consider the following query
```SQL
SELECT SUM(col2)
FROM tbl
WHERE col1 = ?
```
If we have a multi-column index as follows:
```SQL
CREATE INDEX idx_1
ON tbl ( col1, col2 )
```
Then B-tree index has both the columns and there is no need to access the table.

## `include` statement
*PostgreSQL since release 11 supports include statement.*  
  
The include clause allows us to make a distinction between columns we would like to have in the entire index (key columns) and columns we only need in the leaf nodes (include columns).  
That means it allows us to remove columns from the non-leaf nodes if we don’t need them there.  

<img src="/Pic/index2.png" width="600">

```SQL
CREATE INDEX idx_2
ON tbl ( col1 )
INCLUDE ( col2 )
```
This results in shallower B-tree, smaller index size, and most importantly can make the index an *index-only scan*.  
Note that the order of the leaf node entries does not take the include columns into account. The index is solely ordered by its key columns.

## Clustered vs Nonclustered 
- In SQL Server there is a distinction between Clustered and Nonclustered  indexes (TODO: How Postgres indexing relates to this distinction).
- Nonclustered indexes are slower than Clustered ones for reads but faster for write and update.
- The leaf node of a Clustered Index contains data pages of the table on which it is created.
- The leaf nodes of a Nonclustered index consists of index pages which contain Clustering Key (if Clustered index is present on the table) or row ID (RID) (if there is no Clustered index) to locate Data Row.
- Clustered Index enforces a logical order on the rows. Rows are ordered based on Clustering Key.
- In the following example ([source](https://stackoverflow.com/a/41070976/2445273)) we want to retrieve Lname data (the last one is `covering` AKA `index-only`):
<img src="https://i.stack.imgur.com/TnLMf.png" width="600">
<img src="https://i.stack.imgur.com/ojZjo.png" width="600">
<img src="https://i.stack.imgur.com/rSDOI.png" width="600">
