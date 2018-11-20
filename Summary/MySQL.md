
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

`Keywords` (<a href="https://dev.mysql.com/doc/refman/5.7/en/sql-syntax-data-manipulation.html">This</a> gives a comprehensive description)  
`SELECT`			
`FROM`  
`WHERE`  
````MySQL
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
 ````MySQL
 SELECT city FROM customers WHERE city LIKE 'h%d'; \\starts with h and ends with d. <br>
 ````
`_` represents a single character, `%` represents 0 or more characters  
`REGEXP`  E.x: . | [123] [^123] [1-7]  
`FULLTEXT` Enables text search functionality for the column "col1" of the table "table".
This is similar to `LIKE` but easier to work with.
````MySQL
ALTER TABLE table ADD FULLTEXT(col1)
````
------------
**SQL Server**
```MySQL
show databases;
use myDB;
show tables;
````

````MySQL
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
````
#### Pricing
````SQL
drop table  #tt
SELECT s.ProductID, s.SaleDate, s.AccountID, s.Units, s.ProvState,
p.Type, p.Description, p.Brand, p.SubBrand, p.Category, p.SubCategory, p.Varietal, p.Manufacturer, p.Origin, p.Country, p.Agent, p.MAG, p.IsActive
into #tt
FROM [magSales2k].[dbo].[Sales] s 
	INNER JOIN [magSales2k].[dbo].[Products] p 
	ON  s.ProductID = p.ProductID 
WHERE p.MAG = 1 and p.IsActive = 1

-- Aggregate
drop table #tt2
select SaleDate, sum(units) as 'units' into #tt2 from #tt where ProductID='0257816' and ProvState='BC' group by SaleDate order by SaleDate desc

-- Add row number
drop table #tt3
select r = ROW_NUMBER() OVER (ORDER BY a.SaleDate Desc), a.SaleDate, a.units
into #tt3 from #tt2 as a order by a.SaleDate desc

-- Calculate the days-difference and add as a column
drop table #tt4
SELECT a.SaleDate, a.units, DATEDIFF(day, b.SaleDate, a.SaleDate) as datedif
into #tt4 FROM #tt3 a 
LEFT JOIN #tt3 b on a.r = b.r - 1

-- Calculate Average Units Sold per day and add as a column
drop table #tt5
select SaleDate, units, datedif, units / datedif as 'average' into #tt5 from #tt4
````
