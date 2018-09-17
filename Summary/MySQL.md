


Create table
````MySQL
CREATE TABLE table(
col1 int AUTO_INCREMENT,
col2 varchar(30),           #max string length=30
col3 varchar(10) NOT NULL,
PRIMARY KEY(col1)
)
````
Delete table
````MySQL
DROP TABLE table
````
Rename table
````MySQL
RENAME TABLE table_old TO table_new
````
Insert row
````MySQL
INSERT INTO table VALUES('col1a','col2a'),('col1b','col2b') #inserted two rows
INSERT INTO table(col1_name,col2_name) VALUES('col1','col2')
````
Insert rows from another table (same column names)
````MySQL
INSERT INTO table(col1_name,col2_name) SELECT sol1_name,col2_name FROM table2 WHERE ...
````
Delete rows
````MySQL
DELETE FROM table WHERE col_name=100 (e.x. id=100, deletes the rows with id=100)
````
Add column
````MySQL
ALTER TABLE table ADD col varchar(10)
````
Delete column
````MySQL
ALTER TABLE table DROP COLUMN col
````
 **VIEW** is like a reference to a portion or entire part of one or more table. It dynamically represents those info.  
````MySQL
CREATE VIEW view AS SELECT id FROM table 1 ORDER BY col2 DESC LIMIT 10
````

Keywords: (<a href="https://dev.mysql.com/doc/refman/5.7/en/sql-syntax-data-manipulation.html">This</a> gives a comprehensive description)<br>
<samp>SELECT	<br>					
FROM<br>
WHERE
````MySQL
SELECT col3, col4, col5 FROM table WHERE (col1=1 OR col1=2) AND col3='Alex';
````
LIMIT<br>					
IN<br>
NOT IN<br>
ORDER BY <br>
ASC<br>
DESC<br>
AS #name the defined column as, it can rename the current columns or tables as well<br>
CONCAT
````MySQL
SELECT CONCAT(city, ', ', state) AS address FROM customers
````
UPPER #uppercase<br>
COUNT()<br>
GROUP BY<br>
HAVING #similar to WHERE but used for GROUP By<br>
UNION #similar to OR but between queries (the SELECT part need to be the same)<br>
LIKE #E.x: SELECT city FROM customers WHERE city LIKE 'h%d'; \\starts with h and ends with d. <br>
_ represents a single character, % represents 0 or more characters<br>
REGEXP  #E.x: . | [123] [^123] [1-7]
FULLTEXT #E.x: ALTER TABLE table ADD FULLTEXT(col1) \\enables text search functionality for the column "col1" of the table "table": \\this is similar to LIKE but easier to work with
</samp>
</body>
</html> 

select * from [dbo].[Sales] where ProvState='BC'
select AccountID, AccountKey, PCodeZip from [dbo].[Accounts] where ProvState='BC'
select ProductID, Description, VolPerUnit from [dbo].[Products] where IsActive=1 and ProvState='BC'

drop table  #vahidtable
select top 50000
 s.*, 
 p.[Description], 
 p.VolPerUnit,
 a.AccountKey, 
 a.PCodeZip
into #vahidtable
from
 [magSales2k].[dbo].[Sales] s
  INNER JOIN [magSales2k].[dbo].[Products] p ON s.ProvState = p.ProvState AND
                                                s.ProductID = p.ProductID
  INNER JOIN [magSales2k].[dbo].[Accounts] a ON s.ProvState = a.ProvState AND
                                                s.AccountID = a.AccountID
where
 s.ProvState = 'BC' AND
 p.ISActive = 1

select SaleDate, count(Units)  from #vahidtable group by SaleDate order by saleDate desc


