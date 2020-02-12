```sql
select dateadd(d, datediff(d, 0, current_timestamp), 0)
```

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
- The table need to be present. So if we want to empty it beforehand, we use `truncate` statement: `truncate table my_table`
- We can use -T (Trusted Connection) for windows Authentication instead of providing user/pass
- If `^M$` at the end it should work fine without -r option. If line ending is `$`, use `-r "0x0a"`.
- `-F` option indicates which line to start. So to exclude header use `-F 2` .
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
### List of Jobs
```sql
use msdb
go
SELECT [sJOB].[name] AS [JobName]
    , [sDBP].[name] AS [JobOwner]
    , [sCAT].[name] AS [JobCategory]
		, [sJOB].[description] AS [JobDescription]
		, (SELECT COUNT(step_id) FROM dbo.sysjobsteps WHERE job_id = sJOB.job_id) AS 'Number of Steps'
    , [sJSTP].[step_id] AS [JobStartStepNo]
    , [sJSTP].[step_name] AS [JobStartStepName]
    , [sJOB].[date_created] AS [JobCreatedOn]
    , [sJOB].[date_modified] AS [JobLastModifiedOn]
		, CASE [sJOB].[enabled] WHEN 1 THEN 'Yes' WHEN 0 THEN 'No' END AS [IsEnabled]
    , CASE WHEN [sSCH].[schedule_uid] IS NULL THEN 'No' ELSE 'Yes' END AS [IsScheduled]
    , CASE 
        WHEN [freq_type] = 64 THEN 'Start automatically when SQL Server Agent starts'
        WHEN [freq_type] = 128 THEN 'Start whenever the CPUs become idle'
        WHEN [freq_type] IN (4,8,16,32) THEN 'Recurring'
        WHEN [freq_type] = 1 THEN 'One Time'
      END [ScheduleType]
    , CASE [freq_type]
        WHEN 1 THEN 'One Time'
        WHEN 4 THEN 'Daily'
        WHEN 8 THEN 'Weekly'
        WHEN 16 THEN 'Monthly'
        WHEN 32 THEN 'Monthly - Relative to Frequency Interval'
        WHEN 64 THEN 'Start automatically when SQL Server Agent starts'
        WHEN 128 THEN 'Start whenever the CPUs become idle'
      END [Occurrence]
    , CASE [freq_type]
        WHEN 4 THEN 'Occurs every ' + CAST([freq_interval] AS VARCHAR(3)) + ' day(s)'
        WHEN 8 THEN 'Occurs every ' + CAST([freq_recurrence_factor] AS VARCHAR(3)) 
                    + ' week(s) on '
                    + CASE WHEN [freq_interval] & 1 = 1 THEN 'Sunday' ELSE '' END
                    + CASE WHEN [freq_interval] & 2 = 2 THEN ', Monday' ELSE '' END
                    + CASE WHEN [freq_interval] & 4 = 4 THEN ', Tuesday' ELSE '' END
                    + CASE WHEN [freq_interval] & 8 = 8 THEN ', Wednesday' ELSE '' END
                    + CASE WHEN [freq_interval] & 16 = 16 THEN ', Thursday' ELSE '' END
                    + CASE WHEN [freq_interval] & 32 = 32 THEN ', Friday' ELSE '' END
                    + CASE WHEN [freq_interval] & 64 = 64 THEN ', Saturday' ELSE '' END
        WHEN 16 THEN 'Occurs on Day ' + CAST([freq_interval] AS VARCHAR(3)) + ' of every ' + CAST([freq_recurrence_factor] AS VARCHAR(3)) + ' month(s)'
        WHEN 32 THEN 'Occurs on ' + CASE [freq_relative_interval]
																			WHEN 1 THEN 'First'
																			WHEN 2 THEN 'Second'
																			WHEN 4 THEN 'Third'
																			WHEN 8 THEN 'Fourth'
																			WHEN 16 THEN 'Last'
																		END + ' ' 
																	+ CASE [freq_interval]
																			WHEN 1 THEN 'Sunday'
																			WHEN 2 THEN 'Monday'
																			WHEN 3 THEN 'Tuesday'
																			WHEN 4 THEN 'Wednesday'
																			WHEN 5 THEN 'Thursday'
																			WHEN 6 THEN 'Friday'
																			WHEN 7 THEN 'Saturday'
																			WHEN 8 THEN 'Day'
																			WHEN 9 THEN 'Weekday'
																			WHEN 10 THEN 'Weekend day'
																		END	+ ' of every ' + CAST([freq_recurrence_factor] AS VARCHAR(3)) + ' month(s)'
      END AS [Recurrence]
    , CASE [freq_subday_type]
        WHEN 1 THEN 'Occurs once at ' 
                    + STUFF(
                  STUFF(RIGHT('000000' + CAST([active_start_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
        WHEN 2 THEN 'Occurs every ' 
                    + CAST([freq_subday_interval] AS VARCHAR(3)) + ' Second(s) between ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_start_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
                    + ' & ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_end_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
        WHEN 4 THEN 'Occurs every ' 
                    + CAST([freq_subday_interval] AS VARCHAR(3)) + ' Minute(s) between ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_start_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
                    + ' & ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_end_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
        WHEN 8 THEN 'Occurs every ' 
                    + CAST([freq_subday_interval] AS VARCHAR(3)) + ' Hour(s) between ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_start_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
                    + ' & ' 
                    + STUFF(
                    STUFF(RIGHT('000000' + CAST([active_end_time] AS VARCHAR(6)), 6)
                                , 3, 0, ':')
                            , 6, 0, ':')
      END [Frequency]

    , [sSCH].[name] AS [JobScheduleName]
    --,[sJSTP].database_name
    , Last_Run = CONVERT(DATETIME, RTRIM(run_date) + ' '
        + STUFF(STUFF(REPLACE(STR(RTRIM(h.run_time),6,0),
        ' ','0'),3,0,':'),6,0,':'))
		, case [sJSTP].Last_run_outcome
          When 0 then 'Failed'
          when 1 then 'Succeeded'
          When 2 then 'Retry'
          When 3 then 'Canceled'
          When 5 then 'Unknown'
			End as Last_Run_Status

    , Last_Run_Duration_HHMMSS = STUFF(STUFF(REPLACE(STR([sJSTP].last_run_duration,7,0),
        ' ','0'),4,0,':'),7,0,':')
    , Max_Duration = STUFF(STUFF(REPLACE(STR(l.run_duration,7,0),
        ' ','0'),4,0,':'),7,0,':')
    , Next_Run= CONVERT(DATETIME, RTRIM(NULLIF([sJOBSCH].next_run_date, 0)) + ' '
        + STUFF(STUFF(REPLACE(STR(RTRIM([sJOBSCH].next_run_time),6,0),
        ' ','0'),3,0,':'),6,0,':'))
    , CASE [sJOB].[delete_level]
        WHEN 0 THEN 'Never'
        WHEN 1 THEN 'On Success'
        WHEN 2 THEN 'On Failure'
        WHEN 3 THEN 'On Completion'
      END AS [JobDeletionCriterion]
    , [sSVR].[name] AS [OriginatingServerName]
    , [sJSTP].subsystem
    , [sJSTP].command
		, h.message
into #tt
FROM
    [msdb].[dbo].[sysjobs] AS [sJOB]
    LEFT JOIN [msdb].[sys].[servers] AS [sSVR] ON [sJOB].[originating_server_id] = [sSVR].[server_id]
    LEFT JOIN [msdb].[dbo].[syscategories] AS [sCAT] ON [sJOB].[category_id] = [sCAT].[category_id]
    LEFT JOIN [msdb].[dbo].[sysjobsteps] AS [sJSTP] ON [sJOB].[job_id] = [sJSTP].[job_id] AND [sJOB].[start_step_id] = [sJSTP].[step_id]
    LEFT JOIN [msdb].[sys].[database_principals] AS [sDBP] ON [sJOB].[owner_sid] = [sDBP].[sid]
    LEFT JOIN [msdb].[dbo].[sysjobschedules] AS [sJOBSCH] ON [sJOB].[job_id] = [sJOBSCH].[job_id]
    LEFT JOIN [msdb].[dbo].[sysschedules] AS [sSCH] ON [sJOBSCH].[schedule_id] = [sSCH].[schedule_id]
		left JOIN (SELECT job_id, instance_id = MAX(instance_id),max(run_duration) AS run_duration
							 FROM msdb.dbo.sysjobhistory
							 GROUP BY job_id
							) AS l ON sJOB.job_id = l.job_id
		left JOIN msdb.dbo.sysjobhistory AS h ON h.job_id = l.job_id AND h.instance_id = l.instance_id
ORDER BY [JobName]

select *
#into #tt2
from #tt
where isenabled = 'yes'
and isscheduled = 'yes'
and Recurrence is not null
order by Recurrence

delete FROM #tt2
where Recurrence = 'Occurs every 1 week(s) on Sunday'
```
