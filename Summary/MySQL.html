<!DOCTYPE html>
<html>

<head>
  <title>MySQL</title>
  <link rel="shortcut icon" href="/vvaezian.github.io/Pic/terminal.ico">
  <link rel="stylesheet" href="/vvaezian.github.io/styles.css"/>
  <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>
  <script src="https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js?lang=css"></script>
  <link href='http://fonts.googleapis.com/css?family=Hind' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Lora' rel='stylesheet' type='text/css'>
</head>

<body>


Create table<br>
<samp>CREATE TABLE table( <br>
col1 int AUTO_INCREMENT, <br>
col2 varchar(30), #max string length=30 <br>
col3 varchar(10) NOT NULL,<br>
PRIMARY KEY(col1) <br>
)</samp><br>

Delete table
<br><samp>DROP TABLE table</samp><br>

Rename table
<br><samp>RENAME TABLE table_old TO table_new</samp><br>

Insert row
<br><samp>INSERT INTO table VALUES('col1a','col2a'),('col1b','col2b') #inserted two rows<br>
INSERT INTO table(col1_name,col2_name) VALUES('col1','col2')</samp><br>

Insert rows from another table (same comuln names)<br>
<samp>INSERT INTO table(col1_name,col2_name) SELECT sol1_name,col2_name FROM table2 WHERE ...</samp><br>

Delete rows
<br><samp>DELETE FROM table WHERE col_name=100 (e.x. id=100, deletes the rows with id=100)</samp><br>


Add column
<br><samp>ALTER TABLE table ADD col varchar(10)</samp><br>


Delete column
<br><samp>ALTER TABLE table DROP COLUMN col</samp><br>

 "VIEW" is like a reference to a portion or entire part of one or more table. It dynamically represents those info.<br>
<samp>CREATE VIEW view AS SELECT id FROM table 1 ORDER BY col2 DESC LIMIT 10</samp><br><br>

Keywords: (<a href="https://dev.mysql.com/doc/refman/5.7/en/sql-syntax-data-manipulation.html">This</a> gives a comprehensive description)<br>
<samp>SELECT	<br>					
FROM<br>
WHERE 		#E.x: SELECT col3, col4, col5 FROM table WHERE (col1=1 OR col1=2) AND col3='Alex';<br>
LIMIT<br>					
IN<br>
NOT IN<br>
ORDER BY <br>
ASC<br>
DESC<br>
AS #name the defined column as, it can rename the current columns or tables as well<br>
CONCAT #E.X: SELECT CONCAT(city, ', ', state) AS address FROM customers
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


