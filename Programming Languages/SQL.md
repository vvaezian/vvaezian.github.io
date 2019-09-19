### Locks
#### Lock Modes
- The basic lock modes are S (shared), U (update) and X (exclusive). 
- Shared locks allow other processes requesting shared lock to access the data (we say S is compatible with S). Typical example of S is a `SELECT` statement (a *read* request). 
- The U mode is acquired when inspecting a row that might be later updated or deleted (hence the lock may be upgraded to X). Acquiring U locks do not block reads, but blocks other queries from also inspecting the row for a potential update/delete. Without a U mode two queries attempting to update the same row would deadlock as they would both attempt to escalate the S mode to X mode. And having the update queries acquire directly X mode on all rows, even those that turn out not to qualify for the update, would result in unnecessary blocking of reads.
- Two other important locks are SCH-S (schema stability lock) and SCH-M (schema modification lock, e.g. dropping a column). Any query requests SCH-S lock. SCH-M is the most restrictive lock. It basically blocks everything.
#### Lock Levels
- Locks can be row-level, table-level, page-level (8K data) and Hobt-level (partition-level lock, stands for Heap or B-Tree, disabled by default)
- If a small portion of table is being affected, it results in row-level lock, but if the porion be big enough the lock will be table-level instead of a high number of row-level locks.
#### Remarks
- Given the above facts, a SELECT statement will block an UPDATE stement (unless the SELECT statement acquire its S lock as row-level and the UPDATE statement acquire its X lock as row-level and these rows don't overlap). 
- SELECT statements acquire S lock by default. To run a SELECT statement without S lock use either `NOLOCK` (same as `READUNCOMMITTED`) or `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED`. A SELECT statement with NOLOCK results in *dirtyreading*, i.e. it doesn't care whether data is committed or not. While `NOBLOCK` is applied on one table, `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` gets applied to a transaction:
```SQL
SELECT * from myTbl WITH (NOLUCK)
```
```SQL
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; -- turn it on

SELECT ... 
UPDATE ...
SELECT ...

SET TRANSACTION ISOLATION LEVEL READ COMMITTED; -- turn it off
```
* Note that even with NOLOCK or TRANSACTION ISOLATION LEVEL, the query still requests SCH-S lock, so it will block any query that requests SCH-M lock.

### Basic functions
````SQL
-- Create table
CREATE TABLE table(
col1 int AUTO_INCREMENT,
col2 varchar(30),           #max string length=30
col3 varchar(10) NOT NULL,
PRIMARY KEY(col1)
)
-- Delete table
DROP TABLE table

-- Rename table
RENAME TABLE table_old TO table_new

-- Insert row
INSERT INTO table VALUES('col1a','col2a'),('col1b','col2b') #inserted two rows
INSERT INTO table(col1_name,col2_name) VALUES('col1','col2')

-- Insert rows from another table (same column names)
INSERT INTO table(col1_name,col2_name) SELECT sol1_name,col2_name FROM table2 WHERE ...

-- Delete rows
DELETE FROM table WHERE col_name=100 (e.x. id=100, deletes the rows with id=100)

-- Add column
ALTER TABLE table ADD col varchar(10)

-- Delete column
ALTER TABLE table DROP COLUMN col

-- Create View
CREATE VIEW view AS SELECT id FROM table 1 ORDER BY col2 DESC LIMIT 10
 ````
`_` represents a single character, `%` represents 0 or more characters  
`REGEXP`  E.x: . | [123] [^123] [1-7]  


## Command-Line
```SQL
show databases;
use myDB;
show tables;
````

#### Finding Columns
````SQL
/* searching all columns of a database */
select * from INFORMATION_SCHEMA.COLUMNS
where COLUMN_NAME like '%type%'
order by TABLE_NAME

/* Searching all columns of all databases */
-- Declare/Set required variables
DECLARE @vchDynamicDatabaseName AS VARCHAR(MAX),
        @vchDynamicQuery As VARCHAR(MAX),
        @DatabasesCursor CURSOR

SET @DatabasesCursor = Cursor FOR

-- Select useful databases on the server
SELECT name 
FROM sys.databases 
WHERE database_id > 4 
ORDER by name

-- Open the Cursor based on the previous select
OPEN @DatabasesCursor
FETCH NEXT FROM @DatabasesCursor INTO @vchDynamicDatabaseName
WHILE @@FETCH_STATUS = 0
   BEGIN

   --Insert the select statement into @DynamicQuery 
   --This query will select the Database name, all tables/views and their columns (in a comma delimited field)
   SET @vchDynamicQuery =
   ('SELECT ''' + @vchDynamicDatabaseName + ''' AS ''Database_Name'',
          B.table_name AS ''Table Name'',
         STUFF((SELECT '', '' + A.column_name
               FROM ' + @vchDynamicDatabaseName + '.INFORMATION_SCHEMA.COLUMNS A
               WHERE A.Table_name = B.Table_Name
               FOR XML PATH(''''),TYPE).value(''(./text())[1]'',''NVARCHAR(MAX)'')
               , 1, 2, '''') AS ''Columns''
   FROM ' + @vchDynamicDatabaseName + '.INFORMATION_SCHEMA.COLUMNS B
   WHERE B.TABLE_NAME LIKE ''%%''
         AND B.COLUMN_NAME LIKE ''%chemical%''
   GROUP BY B.Table_Name
   Order BY 1 ASC')

   --Print @vchDynamicQuery
   EXEC(@vchDynamicQuery)

   FETCH NEXT FROM @DatabasesCursor INTO @vchDynamicDatabaseName
END
CLOSE @DatabasesCursor
DEALLOCATE @DatabasesCursor
GO
````
## PostgreSQL
`\l` lists databases  
`\dt` lists tables  
`\c DBNAME` connect to a database 
````SQL
-- table size without index
SELECT pg_size_pretty (pg_relation_size('table_name'));

-- table size with index
SELECT pg_size_pretty (pg_total_relation_size('table_name'));

-- Get query plan and costs and see whether index is being used
EXPLAIN SELECT ...

-- Date trunc
select avg(temp), avg(rh) from adcon_all
where date_trunc('day', thedate) = '2010-01-01'
````
````SQL
SELECT 
    TIMESTAMP '2000-01-01 00:00:00' + DATE_PART('day', theDate - TIMESTAMP '2000-01-01 00:00:00') * INTERVAL '1 day' 
    ,AVG(temp)
    ,AVG(rh)
from adcon_all
GROUP BY TIMESTAMP '2000-01-01 00:00:00' + DATE_PART('day', theDate - TIMESTAMP '2000-01-01 00:00:00') * INTERVAL '1 day' 
ORDER BY TIMESTAMP '2000-01-01 00:00:00' + DATE_PART('day', theDate - TIMESTAMP '2000-01-01 00:00:00') * INTERVAL '1 day' 
LIMIT 10
````
````SQL
SELECT CASE WHEN (SELECT the_interval FROM adcon_all WHERE {{t_interval}}) = 'Yearly' 
                THEN SUBSTRING((TIMESTAMP '2000-01-01 00:00:00' + ((DATE_PART('year', theDate) - DATE_PART('year', TIMESTAMP '2000-01-01 00:00:00')) || ' year')::INTERVAL)::TEXT, 1, 4)
            WHEN (SELECT the_interval FROM adcon_all WHERE {{t_interval}}) = 'Monthly' 
                THEN SUBSTRING((TIMESTAMP '2000-01-01 00:00:00' + ((DATE_PART('year', theDate) - DATE_PART('year', TIMESTAMP '2000-01-01 00:00:00')) * 12 
                                                                    + (DATE_PART('month', theDate) - DATE_PART('month', TIMESTAMP '2000-01-01 00:00:00')) || ' month')::INTERVAL)::TEXT, 1, 7)
            WHEN (SELECT the_interval FROM adcon_all WHERE {{t_interval}}) = 'Daily' 
                THEN SUBSTRING((TIMESTAMP '2000-01-01 00:00:00' + (DATE_PART('day', theDate - TIMESTAMP '2000-01-01 00:00:00') || ' day')::INTERVAL)::TEXT, 1, 10)
            WHEN (SELECT the_interval FROM adcon_all WHERE {{t_interval}}) = 'Hourly' 
                THEN SUBSTRING((TIMESTAMP '2000-01-01 00:00:00' + (DATE_PART('day', theDate - TIMESTAMP '2000-01-01 00:00:00') * 24 
                                                                    + DATE_PART('hour', theDate - TIMESTAMP '2000-01-01 00:00:00') || ' hour')::INTERVAL)::TEXT, 1, 13)
      END AS "Date"
    , AVG(temp) AS "Avg Temperature"
    , AVG(rh) AS "Avg RH"
FROM adcon_all
GROUP BY "Date"
ORDER BY "Date"
````
