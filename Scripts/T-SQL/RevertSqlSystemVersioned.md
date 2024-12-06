# Revert System Versioned tables

```sql
ALTER TABLE dbo.your_table
	DROP CONSTRAINT DF_SysStart , DF_SysEnd 
ALTER TABLE dbo.your_table
	DROP PERIOD FOR SYSTEM_TIME
ALTER TABLE dbo.your_table
	DROP COLUMN [SysStartTime], [SysEndTime]
```