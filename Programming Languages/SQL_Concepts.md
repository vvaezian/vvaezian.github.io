## Window Functions ([source](https://www.postgresql.org/docs/current/tutorial-window.html))
A window function performs a calculation across a set of table rows that are somehow related to the current row. This is similar to GROUP BY but now the result is not squished as done with Group By. 
```SQL
-- add a column containing avg(salary) where avg is applied to those rows that have the same depname as the current row
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;

-- add a column containing sum(salary), which is the same for all rows
SELECT salary, sum(salary) OVER () FROM empsalary;

-- add a column containing sum(salary) up until that row (and those with the same value as the current row)
SELECT salary, sum(salary) OVER (ORDER BY salary) FROM empsalary;

-- add a column containg the rank of the row with respect to highest salary, where comparision is done with rows that have the same depname
SELECT depname, empno, salary,
       rank() OVER (PARTITION BY depname ORDER BY salary DESC)
FROM empsalary;

-- several functions on the same window
SELECT sum(salary) OVER w, avg(salary) OVER w
FROM empsalary
WINDOW w AS (PARTITION BY depname ORDER BY salary DESC);
```

## Locks
### Lock Modes (SQL Server)
- The basic lock modes are S (shared), U (update) and X (exclusive). 
- Shared locks allow other processes requesting shared lock to access the data (we say S is compatible with S). Typical example of S is a `SELECT` statement (a *read* request). 
- The U mode is acquired when inspecting a row that might be later updated or deleted (hence the lock may be upgraded to X). Acquiring U locks do not block reads, but blocks other queries from also inspecting the row for a potential update/delete. Without a U mode two queries attempting to update the same row would deadlock as they would both attempt to escalate the S mode to X mode. And having the update queries acquire directly X mode on all rows, even those that turn out not to qualify for the update, would result in unnecessary blocking of reads.
- Two other important locks are SCH-S (schema stability lock) and SCH-M (schema modification lock, e.g. dropping a column). Any query requests SCH-S lock. SCH-M is the most restrictive lock. It basically blocks everything.
### Lock Levels
- Locks can be row-level, table-level, page-level (8K data) and Hobt-level (partition-level lock, stands for Heap or B-Tree, disabled by default)
- If a small portion of table is being affected, it results in row-level lock, but if the porion be big enough the lock will be table-level instead of a high number of row-level locks.
### Remarks
- Given the above facts, a SELECT statement will block an UPDATE stement (unless the SELECT statement acquire its S lock as row-level and the UPDATE statement acquire its X lock as row-level and these rows don't overlap). 
- SELECT statements acquire S lock by default. To run a SELECT statement without S lock use either `NOLOCK` (same as `READUNCOMMITTED`) or `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED`. A SELECT statement with NOLOCK results in *dirtyreading*, i.e. it doesn't care whether data is committed or not. While `NOLOCK` is applied on one table, `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` gets applied to a transaction:

```SQL
SELECT * from myTbl WITH (NOLOCK)
```

```SQL
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; -- turn it on

SELECT ... 
UPDATE ...
SELECT ...

SET TRANSACTION ISOLATION LEVEL READ COMMITTED; -- turn it off
```

- Note that even with NOLOCK or TRANSACTION ISOLATION LEVEL, the query still requests SCH-S lock, so it will block any query that requests SCH-M lock.  
- We can see all locks by running `sp_lock [SPID]`

## Indexing ([source](https://use-the-index-luke.com/))
- The primary purpose of an index is to provide an ordered representation of the indexed data. This reduces the read time, but increase the write time, as the order need to be preserved.   
- Do not index the low-cardinality columns.
- Since it is not efficient to store the data sequentially (because an insert statement would need to move the following entries to make room for the new one), we need to establish a logical order that is independent of physical order in memory.  
The logical order is established via a doubly linked list. It is used to connect B-tree leaf nodes. Index is represented as a B-tree. Each leaf node is stored in a database block (or page; the database's smallest storage unit).  
So the index order is maintained on two different levels: the index entries within each leaf node (because B-tree is ordered), and the leaf nodes among each other using a doubly linked list (because linked_lists are ordered).  
The table data is stored in a heap structure and is not sorted at all. 

<img src="https://use-the-index-luke.com/static/fig01_01_index_leaf_nodes.en.MMHwYDFb.png" width="600">

So I think there are three levels here: 
1. Physical storage that has the bits in memory addresses.
2. The heap that holds the records and has pointers to phisycal storage (data in this stage is called "data rows")
3. The linked list at the B-tree's leaf node which has connections with the heap.

<img src="https://use-the-index-luke.com/static/fig01_02_tree_structure.en.BdEzalqw.png" width="600">

### B-tree Traversal
In the general case, 
1. The database software starts traversing the B-tree to find the first matching entry at the leaf node level. 
2. It then follows the doubly linked list until it has found all matching entries.
3. Finally it fetches each of those matching entries from the table. (the last two steps can be interleaved)

<img src="https://use-the-index-luke.com/static/fig01_03_tree_traversal.en.niC7Q5jq.png" width="400">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/Pic/index1.png" width="600">

Estimates of read operations for each step: (assuming 100 index entries per page/block)

1. The B-tree: `log100([rows in table])`, often less than 5
2. The doubly linked list: `[rows read from index] / 100`
3. The table: `[rows read from table]`

Worst case scenario: all rows of interest are in different blocks, i.e. the worst possible clustering factor.

### Multi-Column (AKA composite) index
This is when index is defined on multiple columns. 
```SQL
CREATE INDEX idx_1
ON tbl ( col1, col2 )
```
Note that the order of columns is important. The index is used for queries on `col1, col2` or on `col1` only.  
It is like the phone book. It is sorted by lastName, FirstName, PhoneNumber. We cannot search by firstName at first.

### index-only scans
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

### Clustered vs Nonclustered ([source](https://www.c-sharpcorner.com/blogs/differences-between-clustered-index-and-nonclustered-index1))
- In SQL Server there is a distinction between Clustered and Nonclustered  indexes.
- Clustered indexes are not a separate entity like it is with other index types. A clustered index *is* the table. When you define a clustered index on a table, the database engine sorts all the rows in the table, in ascending or descending order, based on the columns identified in the index definition (the key columns).
- The leaf node of a Clustered Index contains data pages of the table on which it is created (it kind of replaces the table, as it has all the columns' data in its leaf nodes).
- The leaf nodes of a Nonclustered index consists of index pages which contains Clustering Key (if Clustered index is present on the table) or row ID (RID) (if there is no Clustered index) as pointer to the data. It also contains included columns, if any.
- Clustered Index enforces a logical order on the rows. Rows are ordered based on Clustering Key.
- Nonclustered indexes are slower than Clustered ones for reads but faster for write and update.
- In the following example ([source](https://stackoverflow.com/a/41070976/2445273)) we want to retrieve Lname data (the last one is `covering` AKA `index-only`):
<img src="https://i.stack.imgur.com/TnLMf.png" width="600">
<img src="https://i.stack.imgur.com/ojZjo.png" width="600">
<img src="https://i.stack.imgur.com/rSDOI.png" width="600">
- Indexes are automatically created when `PRIMARY KEY` and `UNIQUE` constraints are defined on table columns. For `PRIMARY KEY` a clustered index is created (unless there is already a clustered index. In this case primary key constraint is enforced by a non-clustered index). 

### `include` statement
*PostgreSQL since release 11 supports include statement.*  
 
The include clause allows us to make a distinction between columns we would like to have in the entire index (key columns) and columns we only need in the leaf nodes (include columns).  
That means it allows us to remove columns from the non-leaf nodes if we don’t need them there.  
For example if the following query is run frequently and we want to define an index for it, having a multi-column index on both OrderID and OrderDate is not the most efficient approach. We just need an index on OrderID where *includes*  OrderDate: ([source](https://www.red-gate.com/simple-talk/sql/performance/14-sql-server-indexing-questions-you-were-too-shy-to-ask/))
```SQL
SELECT OrderID, OrderDate
FROM Sales
WHERE OrderID = 12345;
```
<img src="/Pic/index2.png" width="600">

```SQL
CREATE INDEX idx_2
ON tbl ( col1 )
INCLUDE ( col2 )
```
This results in shallower B-tree, smaller index size, and most importantly can make the index an *index-only scan*.  
Note that the order of the leaf node entries does not take the include columns into account. The index is solely ordered by its key columns.  

- In SQL Server, *include* statement are only available for non-clustered indexes, because clustered indexes alread have all the data in their leaf nodes.

### PostgreSQL
In Postgres all indexes are non-clustered. Although there is a command `CLUSTER` which has similar effects:
```SQL
CLUSTER VERBOSE table_name USING index
```
It creates a temp table where the columns are ordered based on the index. It also creates all indexes that were on the original table to the new table. At the end it drops the original table.
- The difference with SQL Server's clustered index is that the order is not maintained after the table is edited. In this case we need to recluster. (there may also be a difference in a way the data is stored. Here clustered table is stored as a heap, because it is a redular table. Need to look into how SQL Server's Clustered indexes are stored.)
- In subsequest clusterings, we don't need to mention the index, because there can be only one cluster on a table.
- The command `CLUSTER` (without any argument) will recluster all previously defined clusters in the current database.
