
Create table
````SQL
CREATE TABLE table(
col1 int AUTO_INCREMENT,
col2 varchar(30),           #max string length=30
col3 varchar(10) NOT NULL,
PRIMARY KEY(col1)
)
````
Delete table
````SQL
DROP TABLE table
````
Rename table
````SQL
RENAME TABLE table_old TO table_new
````
Insert row
````SQL
INSERT INTO table VALUES('col1a','col2a'),('col1b','col2b') #inserted two rows
INSERT INTO table(col1_name,col2_name) VALUES('col1','col2')
````
Insert rows from another table (same column names)
````SQL
INSERT INTO table(col1_name,col2_name) SELECT sol1_name,col2_name FROM table2 WHERE ...
````
Delete rows
````SQL
DELETE FROM table WHERE col_name=100 (e.x. id=100, deletes the rows with id=100)
````
Add column
````SQL
ALTER TABLE table ADD col varchar(10)
````
Delete column
````SQL
ALTER TABLE table DROP COLUMN col
````
 **VIEW** is like a reference to a portion or entire part of one or more table. It dynamically represents those info.  
````SQL
CREATE VIEW view AS SELECT id FROM table 1 ORDER BY col2 DESC LIMIT 10
````

`Keywords` (<a href="https://dev.mysql.com/doc/refman/5.7/en/sql-syntax-data-manipulation.html">This</a> gives a comprehensive description)  
`SELECT`			
`FROM`  
`WHERE`  
````SQL
SELECT col3, col4, col5 FROM table WHERE (col1=1 OR col1=2) AND col3='Alex';
````
`LIMIT`  					
`IN`  
`NOT IN`  
`ORDER BY`  
`ASC`  
`DESC`  
`AS` name the defined column as, it can rename the current columns or tables as well  
`CONCAT`
````MySQL
SELECT CONCAT(city, ', ', state) AS address FROM customers
````
`UPPER` uppercase  
`COUNT()`  
`GROUP BY`  
`HAVING` similar to WHERE but used for GROUP By  
`UNION` similar to OR but between queries (the SELECT part need to be the same)  
`LIKE`
 ````SQL
 SELECT city FROM customers WHERE city LIKE 'h%d'; \\starts with h and ends with d. <br>
 ````
`_` represents a single character, `%` represents 0 or more characters  
`REGEXP`  E.x: . | [123] [^123] [1-7]  
`FULLTEXT` Enables text search functionality for the column "col1" of the table "table".
This is similar to `LIKE` but easier to work with.
````SQL
ALTER TABLE table ADD FULLTEXT(col1)
````

## SQL Server
```SQL
show databases;
use myDB;
show tables;
````

#### Finding All Columns
````SQL
/* searching all columns of a database */
--SELECT c.name AS ColName, t.name AS TableName
--FROM sys.columns c
--    JOIN sys.tables t ON c.object_id = t.object_id
--WHERE c.name LIKE '%chemical%';


/* searching all columns of all databases */
--Declare/Set required variables
DECLARE @vchDynamicDatabaseName AS VARCHAR(MAX),
        @vchDynamicQuery As VARCHAR(MAX),
        @DatabasesCursor CURSOR

SET @DatabasesCursor = Cursor FOR

--Select * useful databases on the server
SELECT name 
FROM sys.databases 
WHERE database_id > 4 
ORDER by name


--Open the Cursor based on the previous select
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
