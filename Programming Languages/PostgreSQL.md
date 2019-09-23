* Postgres commands are case-insensitive, to force case sensetivity we need to wrap the name in double-quotes.  


### Basic Functions
````SQL
-- lists databases  
\l 
-- lists tables
\dt   
-- connect to a database 
\c DBNAME

-- get table size without index
SELECT pg_size_pretty (pg_relation_size('table_name'));

-- get table size with index
SELECT pg_size_pretty (pg_total_relation_size('table_name'));

-- get query plan and costs and see whether index is being used
EXPLAIN SELECT ...

-- Date trunc
select avg(temp), avg(rh) from adcon_all
where date_trunc('day', thedate) = '2010-01-01'
````

### Copy from CSV
```SQL
\copy tbl_name from '~/myFile.csv' delimiter E'\t' csv;
```
- Including `csv` in the command causes empty strings to be imported as NULL. E.g. `,,` or `\t\t` depending on the delimiter.
