DECLARE @SchemaName SYSNAME = 'Core_DocumentManagement';

	SELECT 
		--'entity "' + schemas.name + '.' + tables.name + '" as ' + tables.name + ' {' + CHAR(10) +
		'entity ' + tables.name + ' {' + CHAR(10) +
			(SELECT 
				STRING_AGG(
				'  ' + columns.name + ' : ' + UPPER(types.name) + 
					ISNULL(CASE 
						WHEN types.name IN ('varchar', 'nvarchar', 'char', 'nchar')
							THEN '(' + CASE columns.max_length WHEN -1 THEN 'MAX' ELSE CAST(columns.max_length AS NVARCHAR) END + ')'
					END, '') + 
					CHAR(10)
				, '') WITHIN GROUP (ORDER BY columns.column_id)
			FROM sys.columns
			INNER JOIN sys.types
				ON types.system_type_id = columns.system_type_id
				AND types.user_type_id = columns.user_type_id
			WHERE 
				columns.object_id = tables.object_id
			) +
		'}'
	FROM sys.schemas
	INNER JOIN sys.tables
		ON tables.schema_id = schemas.schema_id
	WHERE 
		schemas.name = @SchemaName
	ORDER BY
		 schemas.schema_id
		,tables.object_id
		
;
	SELECT 
		--STRING_AGG(
		ParentTables.name + '::' + ParentColumns.name + ' -- ' + ReferencedTables.name + '::' + ReferencedColumns.name -- + CHAR(10)
		--ParentTables.name + ' -- ' + ReferencedTables.name + CHAR(10)
		--, '') WITHIN GROUP (ORDER BY foreign_key_columns.constraint_column_id)
						 
	FROM sys.foreign_keys
	INNER JOIN sys.foreign_key_columns
		ON foreign_keys.object_id = foreign_key_columns.constraint_object_id

	INNER JOIN sys.columns ParentColumns
		ON ParentColumns.object_id = foreign_key_columns.parent_object_id
			AND ParentColumns.column_id = foreign_key_columns.parent_column_id
	INNER JOIN sys.tables ParentTables
		ON ParentTables.object_id = ParentColumns.object_id
	INNER JOIN sys.schemas ParentSchemas
		ON ParentSchemas.schema_id = ParentTables.schema_id
	
	INNER JOIN sys.columns ReferencedColumns
		ON ReferencedColumns.object_id = foreign_key_columns.referenced_object_id
			AND ReferencedColumns.column_id = foreign_key_columns.referenced_column_id
	INNER JOIN sys.tables ReferencedTables
		ON ReferencedTables.object_id = ReferencedColumns.object_id
	
	WHERE 
		ParentSchemas.name = @SchemaName
	ORDER BY
		 ParentSchemas.schema_id
		,ParentTables.object_id
		,foreign_key_columns.constraint_column_id
		
;