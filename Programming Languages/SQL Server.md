
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
- SELECT statements acquire S lock by default. To run a SELECT statement without S lock use either `NOLOCK` (same as `READUNCOMMITTED`) or `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED`. A SELECT statement with NOLOCK results in *dirtyreading*, i.e. it doesn't care whether data is committed or not. While `NOLOCK` is applied on one table, `TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` gets applied to a transaction:
````SQL
SELECT * from myTbl WITH (NOLOCK)
````
````SQL
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; -- turn it on

SELECT ... 
UPDATE ...
SELECT ...

SET TRANSACTION ISOLATION LEVEL READ COMMITTED; -- turn it off
````
- Note that even with NOLOCK or TRANSACTION ISOLATION LEVEL, the query still requests SCH-S lock, so it will block any query that requests SCH-M lock.  
- We can see all locks by running `sp_lock [SPID]`

### DB disk usage
```sql
SELECT DbSize_GB = (SELECT CONVERT(DECIMAL(18,2), SUM(CAST(df.size as float))*8/(1024.0 * 1024))
                    FROM sys.database_files AS df 
                    WHERE df.type in ( 0, 2, 4 ) )
      , SpaceUsed_GB = CONVERT(DECIMAL(18,2), SUM(a.total_pages)*8/(1024.0 * 1024))
      , LogSize_GB = (SELECT CONVERT(DECIMAL(18,2), SUM(CAST(df.size as float))*8/(1024.0 * 1024))
                      FROM sys.database_files AS df 
                      WHERE df.type in (1, 3))
FROM sys.partitions p 
     JOIN sys.allocation_units a 
     ON p.partition_id = a.container_id;
```

### Bulk Copy
```powershell
bcp [database_name].[dbo].[table_name] in "C:\path\to\file" -S server_name -U user_name -P password -c -t ','
```
- Installation `sudo yum install mssql-tools`
- The table need to be present. So if we want to empty if beforehand use `truncate` statement: `truncate table my_table`
- We can use -T (Trusted Connection) for windows Authentication instead of providing user/pass
- If `^M$` at the end it should work fine without -r option. For `$` as line ending use `-r "0x0a"`.
- `-F` option indicated which line to start. So to exclude header use `-F 2` .
- Speed test: ~6 MB/s from local. ~3 MB/s from EC2
- To run from Python
```python
subprocess.call('bcp {t} in {f} -S {s} -U {u} -P {p} -c -t "{sep}" '.format(t='db_name.dbo.table_name', 
                                                                            f='out.csv', 
                                                                            s='server_name', 
                                                                            u='user_name', 
                                                                            p="pass", 
                                                                            sep='\t'), 
                 shell=True)
```
### Add Primary Key
```SQL
-- First need to make the columns non-null if not already
ALTER TABLE tbl_name
alter column col1 varchar(10) not null

ALTER TABLE tbl_name
alter column col2 varchar(10) not null

ALTER TABLE tbl_name
ADD PRIMARY KEY(col1, col2)
```

### Finding Columns
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

