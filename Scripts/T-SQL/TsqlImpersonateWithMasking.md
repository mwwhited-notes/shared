# TSQL Impersonation with Dynamic Datamasking

## Summary

It is possible to use impersonation to change between a masked and unmasked data within the same connection.

```sql

/*
CREATE USER [unmasked] WITHOUT LOGIN WITH DEFAULT_SCHEMA=[dbo]
CREATE USER [masked] WITHOUT LOGIN WITH DEFAULT_SCHEMA=[dbo]

GRANT UNMASK TO unmasked
GRANT IMPERSONATE ON USER::unmasked TO masked;
GRANT IMPERSONATE ON USER::masked TO unmasked;

EXEC sp_addrolemember N'db_datareader', N'masked'
EXEC sp_addrolemember N'db_datawriter', N'masked'

EXEC sp_addrolemember N'db_datareader', N'unmasked'
EXEC sp_addrolemember N'db_datawriter', N'unmasked'

ALTER TABLE [Core].[Persons]  
	ALTER COLUMN [LastName] 
		ADD MASKED WITH (FUNCTION = 'partial(2,"XXX",0)');  
*/

--current scope

SELECT TOP 5 [Persons].[LastName], USER, ORIGINAL_LOGIN()
FROM [Core].[Persons];

--impersonate as masked
EXECUTE AS USER = 'masked';

SELECT TOP 5 [Persons].[LastName], USER, ORIGINAL_LOGIN()
FROM [Core].[Persons];

REVERT ;


--impersonate as unmasked
EXECUTE AS USER = 'unmasked'; -- WITH NO REVERT;

SELECT TOP 5 [Persons].[LastName], USER, ORIGINAL_LOGIN()
FROM [Core].[Persons];

REVERT ;

WHILE (SYSTEM_USER != ORIGINAL_LOGIN() )
BEGIN
	REVERT;
END

```