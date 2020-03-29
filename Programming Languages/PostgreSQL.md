
### TODO
- [ ] check the multi-valued data types *array*, *jsonb* and *tsvector*.  
E.g Say the table `film` has a column `special_feature` that has *array* data type. To search a text in all array elements of all rows of that column we do:  
`SELECT title FROM film WHERE special_features @> '{"test_text"}';`  
`@>` checks if the left hand side is a superset of the right hand side.  
We need *GIN index* for indexing this column.


### Remarks
- Postgres commands get converted to lower-case and then evaluated. To force case sensetivity we need to wrap the names in double-quotes.  
E.g. the command `select * from myTable` tries to get data from the table `mytable` (which is different from the table `myTable`).


### Basic Functions
````SQL
-- create index
CREATE INDEX index_name ON table_name ( col_name [ASC | DESC] [NULLS {FIRST | LAST }], ...  );

-- cluster a table
CLUSTER VERBOSE table_name USING index
-- in subsequest clusterings, we don't need to mention the index, because there can be only one cluster on a table.
-- the command `CLUSTER` (without any argument) will recluster all previously defined clusters in the current database.

-- get table size without index
SELECT pg_size_pretty (pg_relation_size('table_name'));

-- get table size with index
SELECT pg_size_pretty (pg_total_relation_size('table_name'));

-- Show active connections
select * from pg_stat_activity
order by datname

-- Date trunc
select avg(temp), avg(rh) from adcon_all
where date_trunc('day', thedate) = '2010-01-01'

-- See connections and activities
SELECT * FROM pg_stat_activity
where datname = 'myDBname'
````
### `psql`
```bash
psql --host metabase-internal-database.cztt4nrxp7n3.us-west-2.rds.amazonaws.com --port 5432 --username vvAdmin --password --dbname MetabaseApplicationDB
psql --host metabase-data.cztt4nrxp7n3.us-west-2.rds.amazonaws.com --port 5432 --username vvAdmin --password --dbname ca_account_performance

# lists databases  
\l 
# lists tables
\dt   
# list columns and indexes of a table
\d table_name
# list indexes of a table
\di table_name
# connect to a database 
\c db_name
```
### Indexes

-  Get query plan and costs and see whether index is being used:  
```sql
EXPLAIN SELECT ...
```
- See defined indexes
```sql
SELECT *
FROM pg_indexes
where schemaname = 'public'
```

- Everytime an index is scanned, it is noted by the statistics manager and a cumulative count is available in the system catalog view `pg_stat_user_indexes` as the value `idx_scan`. 
Monitoring this value over a period of time (say, a month) gives a good idea of which indexes are unused and can be removed. ([source](https://pgdash.io/blog/postgres-indexes.html))

```sql
SELECT relname, indexrelname, idx_scan
FROM   pg_catalog.pg_stat_user_indexes
WHERE  schemaname = 'public';
```

### Custom Function
```sql
CREATE FUNCTION update_block(old text, new text) RETURNS void AS $$
BEGIN
    UPDATE adcon_all 
    SET theblock = $2
    WHERE theblock = $1;

END; $$
LANGUAGE PLPGSQL;
```
Call it with `select update_block('SF02 D','Osoyoos 2 D')`.  

#### Multi-Dimentional Array
```SQL
CREATE FUNCTION update_block_name(arr TEXT[]) RETURNS void AS $$
DECLARE
  x varchar[];
BEGIN
  FOREACH x SLICE 1 IN ARRAY arr
  LOOP
    UPDATE adcon_all
    SET theblock = x[2]
    WHERE theblock = x[1];
  END LOOP;
END;
$$ LANGUAGE plpgsql;
```
call it this way
```SQL
DO
$$ declare arr TEXT[] := array[
				 ['SF02 D','Osoyoos 2 D']
				,['SF10 A','Oliver North 10 A']
				,['SF10 AA','Oliver North 10 A']
				,['SF10 C','Oliver North 10 C']
				,['SF10 Q','Oliver North 10 Q']
				,['SF10 T','Oliver North 10 T']
  				];
begin
	perform update_block_name( arr );
end $$; 
```
### Copy from CSV
```SQL
\copy tbl_name from '~/myFile.csv' delimiter E'\t' csv;
```
- Including `csv` in the command causes empty strings to be imported as NULL (empty string is like `,,` or `\t\t` in the file, depending on the delimiter).
- Add `header` if the csv has header row (this will ignore the first row).
- If the file is in utf16 format (e.g. exported from SQL Server), use the following to convert it to utf8:  
`iconv -f UTF-16LE -t UTF-8 file.csv -o file_utf8.csv`

