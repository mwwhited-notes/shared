# Simple TSQL Table as Queue

## Show unlocked events

```SQL
SELECT
	*
FROM dbo.queue WITH (READPAST)
;
```

## Show all events

```SQL
SELECT
	*
FROM dbo.queue WITH (READUNCOMMITTED)
;
```

## Get, Lock, Process and Unlock Queue

```SQL
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

BEGIN TRAN

-- https://www.mssqltips.com/sqlservertip/1257/processing-data-queues-in-sql-server-with-readpast-and-updlock/ 
DECLARE @workId INT = (
	SELECT TOP 1 [Id] 
	FROM dbo.queue
		WITH (UPDLOCK, READPAST)
);

DROP TABLE IF EXISTS [#processing];

SELECT TOP 1
	*
INTO [#processing]
FROM dbo.queue WITH (ROWLOCK, XLOCK, HOLDLOCK)
WHERE 
	[Id] = @workId; 
;

PRINT @workId;	

UPDATE dbo.queue
SET LastLock = GETDATE(), Status = 'Running'
WHERE 
	[Id] = @workId;

WAITFOR DELAY '00:00:30'; -- Do Work!
	
UPDATE dbo.queue
SET LastRelease = GETDATE(), Status = 'Done'
WHERE 
	[Id] = @workId;

COMMIT
```