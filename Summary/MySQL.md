
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
------------
**SQL Server**
```SQL
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
drop table #cursorTable1
select * into #cursorTable1 from VANSQL12t
left join (select SaleDate, sum(units) as 'units' from VANSQL13t  group by SaleDate) Z on Z.SaleDate=VANSQL12t.EndDate  order by VANSQL12t.StartDate 

-- Correct those periods of price change that their EndDate doesn't correspond with a SaleDate
DECLARE @curStartDate DATE, @prevStartDate DATE, @curSaleDate DATE, @prevSaleDate DATE, @StoredDate DATE = (select top 1 startDate from #cursorTable1);
DECLARE cursor_res1 CURSOR FOR
  SELECT StartDate, SaleDate FROM #cursorTable1;

OPEN cursor_res1
FETCH NEXT FROM cursor_res1 into @curStartDate, @curSaleDate
WHILE @@FETCH_STATUS = 0
BEGIN 
  IF @curSaleDate is NULL and @prevSaleDate is not null
	SET @StoredDate = @CurStartDate;
  IF @curSaleDate is not NULL and @prevSaleDate is null
    UPDATE #cursorTable1 SET StartDate = @StoredDate WHERE CURRENT OF cursor_res1; 
  SET @prevStartDate = @curStartDate
  SET @prevSaleDate = @curSaleDate
  FETCH NEXT FROM cursor_res1 into @curStartDate, @curSaleDate
END

CLOSE cursor_res1;
DEALLOCATE cursor_res1;

DELETE FROM #cursorTable1 WHERE SaleDate is Null
ALTER TABLE #cursorTable1 DROP Column SaleDate, units

-- Sum the units sold for periods of price change 
drop table #cursorTable2
select * into #cursorTable2 from (select SaleDate, sum(units) as 'units' from VANSQL13t  group by SaleDate) Z
left join #cursorTable1 on Z.SaleDate=#cursorTable1.EndDate where SaleDate > '2013-07-27' order by Z.SaleDate

DECLARE @CurrUnits INT, @currCSPC INT, @prevCSPC INT, @sum INT = 0;
DECLARE cursor_res CURSOR FOR
  SELECT units, CSPC FROM #cursorTable2;

OPEN cursor_res
FETCH NEXT FROM cursor_res into @CurrUnits, @currCSPC
WHILE @@FETCH_STATUS = 0
BEGIN 
  IF @currCSPC is NULL 
	SET @sum = @sum + @CurrUnits;
  ELSE
	IF @prevCSPC is null
      BEGIN
	    UPDATE #cursorTable2 SET units = @sum + @CurrUnits WHERE CURRENT OF cursor_res; 
	    SET @sum = 0;
	  END 
  SET @prevCSPC = @currCSPC
  FETCH NEXT FROM cursor_res into @CurrUnits, @currCSPC
END
 
CLOSE cursor_res;
DEALLOCATE cursor_res;

-- Get UnitPerCase
declare @unitPerCase int = (select top 1 UnitsPerCase FROM vansql13.[magSales2k].[dbo].[Products] where cspc = '0257816')

select StartDate, EndDate, Discount, MarginDollars, SaleDate, Units, (units / @unitPerCase) as Cases, (units/ @unitPerCase) * (MarginDollars - Discount) as profitTotal,
DATEDIFF(day, StartDate, EndDate) as 'dateDif', units / DATEDIFF(day, StartDate, EndDate) as 'AvgUnits/Day', ((units/ @unitPerCase) * MarginDollars)/DATEDIFF(day, StartDate, EndDate) as 'AVGProfit/Day' 
from #cursorTable2 where CSPC is not null order by SaleDate desc
````
