# Enumerate Contents of an MS SQL Database

## Summary 

### As Dataset

This will create a dataset listing all all schemas, objects and columns within the current database

```sql
SELECT 
    [databases].[database_id]
    ,[schemas].[schema_id]
    ,CASE [objects].[parent_object_id]
        WHEN 0 THEN [objects].[object_id]
        ELSE [objects].[parent_object_id]
        END [object_id]
    ,CASE [objects].[parent_object_id]
        WHEN 0 THEN [columns].[column_id]
        ELSE [objects].[object_id]
        END [column_id]
    ,[databases].[name] AS [Database Name]
    ,[schemas].[name] AS [Schema Name]
    ,CASE [objects].[parent_object_id]
        WHEN 0 THEN [objects].[name]
        ELSE [Parent].[name]
        END [Object Name]
    ,CASE [objects].[parent_object_id]
        WHEN 0 THEN [columns].[name] 
        ELSE [objects].[name]
        END [Item Name]
    ,[objects].[type]
    ,REPLACE([objects].[type_desc], '_', ' ') AS [Object Type]
    ,[types].[name] AS [Column Type]
    ,[types].[max_length]
    ,[types].[precision]
    ,[types].[scale]
    ,[types].[collation_name]
FROM [sys].[objects]
CROSS JOIN [sys].[databases]
INNER JOIN [sys].[schemas]
    ON [objects].[schema_id] = [schemas].[schema_id]
LEFT OUTER JOIN [sys].[objects] AS [Parent]
    ON [objects].[parent_object_id] = [Parent].[object_id]
LEFT OUTER JOIN [sys].[columns]
    ON [objects].[object_id] = [columns].[object_id]
LEFT OUTER JOIN [sys].[types]
    ON [types].[user_type_id] = [columns].[user_type_id]
WHERE 
    [databases].[database_id] = DB_ID()
    AND [objects].[is_ms_shipped] = 0
ORDER BY 
    [databases].[database_id]
    ,[schemas].[schema_id]
    ,CASE [objects].[parent_object_id]
        WHEN 0 THEN [objects].[object_id]
        ELSE [objects].[parent_object_id]
        END
    ,[objects].[type]
    ,[objects].[object_id]
    ,[columns].[column_id]
```

### As XML

```sql
SELECT 
       [schemas].[name] AS [@name]
       ,[schemas].[schema_id] AS [@id]
       ,(
              SELECT 
                     LOWER([tables].[name]) AS [@name]
                     ,'[' + [schemas].[name] + '].[' + LOWER([tables].[name]) + ']' AS [@full-name]
                     ,[tables].[object_id] AS [@id]
                     ,(
                           SELECT 
                                  [columns].[name] AS [@name]
                                  ,[columns].[column_id] AS [@id]
                                  ,UPPER(CASE
                                         WHEN [types].[name] LIKE '%char' OR [types].[name] LIKE '%binary' THEN [types].[name] + '(' + 
                                                CASE [columns].[max_length] 
                                                       WHEN -1 THEN 'MAX'
                                                       ELSE  CAST([columns].[max_length] AS VARCHAR(10)) 
                                                       END  + ')'
                                         WHEN [types].[name] IN ('decimal', 'numeric') THEN [types].[name] + '(' + 
                                                        CAST([columns].[precision] AS VARCHAR(10)) + ',' +
                                                       CAST([columns].[scale] AS VARCHAR(10)) + ')'
                                         ELSE [types].[name]
                                         END) AS [@type]
                                  ,[columns].[is_nullable] AS [@is-nullable]
 
                           FROM [sys].[columns]
                           INNER JOIN [sys].[types]
                                  ON [types].[system_type_id] = [columns].[system_type_id]
                                         AND [types].[user_type_id] = [columns].[user_type_id]
                           WHERE
                                  [columns].[object_id] = [tables].[object_id]
                           FOR XML PATH('column'), TYPE
                     )
                     ,(
                           SELECT 
                                  [indexes].[name] AS [@name]
                                  ,[indexes].[index_id] AS [@id]
                                  ,[indexes].[is_unique] AS [@is-unique]
                                  ,[indexes].[is_primary_key] AS [@is-primary-key]
                                  ,[indexes].[type_desc] AS [@type]
                                  ,(
                                         SELECT 
                                                [index_columns].[column_id] AS [@ref-id] 
                                                ,[columns].[name] AS [@ref-name] 
                                         FROM [sys].[index_columns]
                                         INNER JOIN [sys].[columns]
                                                ON [columns].[object_id] = [tables].[object_id]
                                                       AND [columns].[column_id] = [index_columns].[column_id]
                                         WHERE
                                                [index_columns].[object_id] = [tables].[object_id]
                                                AND [index_columns].[index_id] = [indexes].[index_id]
                                         FOR XML PATH('column-ref'), TYPE
                                  )
                           FROM [sys].[indexes]
                           WHERE
                                  [indexes].[object_id] = [tables].[object_id]
                                  AND [indexes].[index_id] != 0
                           FOR XML PATH('index'), TYPE
                     )
                     ,(
                           SELECT 
                                  [foreign_keys].[name] AS [@name] 
                                  ,[foreign_keys].[object_id] AS [@id]
                                  ,[foreign_keys].[schema_id] AS [@schema-id]
                                  ,[foreign_keys].[referenced_object_id] AS [@related-id]
                                  ,[referenced_tables].[name] AS [@related-name]
                                  ,[referenced_schemas].[name] AS [@related-schema]
                                  ,(
                                         SELECT 
                                                [foreign_key_columns].[constraint_column_id] AS [@id]
                                                ,[foreign_key_columns].[parent_column_id] AS [@ref-id]
                                                ,[parent_column].[name] AS [@ref-name]
                                                ,[foreign_key_columns].[referenced_column_id] AS [@related-id]
                                                ,[referenced_column].[name] AS [@related-name]
                                         FROM [sys].[foreign_key_columns]
                                         INNER JOIN [sys].[columns] AS [parent_column]
                                                ON [parent_column].[object_id] = [foreign_key_columns].[parent_object_id]
                                                       AND [parent_column].[column_id] = [foreign_key_columns].[parent_column_id]
                                         INNER JOIN [sys].[columns] AS [referenced_column]
                                                ON [referenced_column].[object_id] = [foreign_key_columns].[referenced_object_id]
                                                       AND [referenced_column].[column_id] = [foreign_key_columns].[referenced_column_id]
                                         WHERE
                                                [foreign_key_columns].[constraint_object_id] = [foreign_keys].[object_id]
                                         FOR XML PATH('column-ref'), TYPE
                                  )
                           FROM [sys].[foreign_keys]
                           INNER JOIN [sys].[tables] AS [referenced_tables]
                                  ON [foreign_keys].[referenced_object_id] = [referenced_tables].[object_id]
                           INNER JOIN [sys].[schemas] AS [referenced_schemas]
                                  ON [referenced_tables].[schema_id] = [referenced_schemas].[schema_id]
                           WHERE
                                  [foreign_keys].[parent_object_id] = [tables].[object_id]
                           FOR XML PATH('foreign-key'), TYPE
                     )
              FROM [sys].[tables]
              WHERE 
                     [tables].[schema_id] = [schemas].[schema_id]
                     AND [tables].[name] != 'sysdiagrams'
              FOR XML PATH('table'), TYPE
       )
FROM [sys].[schemas]
WHERE
       [schemas].[schema_id] IN (
              SELECT [tables].[schema_id]
              FROM [sys].[tables]
              WHERE
                     [tables].[name] != 'sysdiagrams'
       )
FOR XML PATH('schema'), ROOT('db')
```

## Yet another version

```sql
    SELECT 
         schemas.name AS [SchemaName]
        ,objects.name AS [ObjectName]
        ,columns.name AS [ColumnName]
        ,REPLACE(REPLACE(REPLACE(REPLACE(columns.name, ' ', '_'), ')', ''), '(', ''), '.', '') AS [CleanColumnName]

        ,ROW_NUMBER() OVER (
            PARTITION BY
                 schemas.name
                ,objects.name
            ORDER BY
                columns.name
        ) AS [RowOrder]

        ,types.name AS [TypeName]

        -- https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver16
        ,UPPER(
            CASE types.name
                WHEN 'uniqueidentifier' THEN types.name
                WHEN 'bit' THEN types.name
                WHEN 'int' THEN types.name
                WHEN 'bigint' THEN types.name

                WHEN 'nvarchar' THEN 
                    CASE columns.max_length
                        WHEN -1 THEN types.name + '(max)'
                        ELSE types.name + '(' + CAST(columns.max_length / 2 AS NVARCHAR(20)) + ')'
                        END
                WHEN 'varchar' THEN 
                    CASE columns.max_length
                        WHEN -1 THEN types.name + '(max)'
                        ELSE types.name + '(' + CAST(columns.max_length AS NVARCHAR(20)) + ')'
                        END
                
                WHEN 'datetimeoffset' THEN
                    CASE columns.scale
                        WHEN 3 THEN types.name
                        ELSE types.name + '(' + CAST(columns.scale AS NVARCHAR(20)) + ')'
                        END
                WHEN 'datetime' THEN
                    CASE columns.scale
                        WHEN 3 THEN types.name
                        ELSE types.name + '(' + CAST(columns.scale AS NVARCHAR(20)) + ')'
                        END
                WHEN 'datetime2' THEN
                    CASE columns.scale
                        WHEN 3 THEN types.name
                        ELSE types.name + '(' + CAST(columns.scale AS NVARCHAR(20)) + ')'
                        END
                
                WHEN 'decimal' THEN  types.name + '(' + CAST(columns.precision AS NVARCHAR(20)) + ', ' + CAST(columns.scale AS NVARCHAR(20)) + ')'
                WHEN 'numeric' THEN  types.name + '(' + CAST(columns.precision AS NVARCHAR(20)) + ', ' + CAST(columns.scale AS NVARCHAR(20)) + ')'

                END + 

            CASE columns.is_nullable 
                WHEN 1 THEN ' NULL' 
                ELSE ''
                END + 

            CASE columns.is_identity 
                WHEN 1 THEN ' IDENTITY' + (
                    SELECT TOP 1 
                        '(' + CAST(identity_columns.seed_value AS NVARCHAR(20)) + ', ' + CAST(identity_columns.increment_value AS NVARCHAR(20)) + ')' + 
                        ' /* ' + CASE WHEN identity_columns.last_value IS NULL THEN 'Seed' ELSE 'Last' END + ': ' + ISNULL(CAST(identity_columns.last_value AS NVARCHAR(20)), CAST(identity_columns.seed_value AS NVARCHAR(20))) + ' */'
                    FROM sys.identity_columns
                    WHERE 
                            identity_columns.object_id = objects.object_id
                        AND identity_columns.column_id = columns.column_id
                )                
                ELSE ''
                END +

            CASE 
                WHEN columns.collation_name IS NULL THEN ''
                ELSE ' COLLATE ' + columns.collation_name
                END

            ) AS [SQL_TypeDescription]

            -- https://www.jhipster.tech/jdl/entities-fields#with-fields
            ,CASE types.name
                WHEN 'uniqueidentifier' THEN 'UUID'
                WHEN 'bit' THEN 'Boolean'
                WHEN 'int' THEN 'Integer'
                WHEN 'bigint' THEN 'Long'

                WHEN 'nvarchar' THEN CASE columns.max_length WHEN -1 THEN 'TextBlob' ELSE 'String' END
                WHEN 'varchar' THEN CASE columns.max_length WHEN -1 THEN 'TextBlob' ELSE 'String' END
                
                WHEN 'datetimeoffset' THEN 'ZonedDateTime'
                WHEN 'datetime' THEN 'LocalDate'
                WHEN 'datetime2' THEN 'LocalDate'
                
                WHEN 'decimal' THEN 'Double'
                WHEN 'numeric' THEN 'Double'

                END AS [JDL_TypeDescription]
                
            ,CASE types.name
                WHEN 'nvarchar' THEN columns.max_length
                WHEN 'varchar' THEN columns.max_length
                END AS [MaxStringLength]

    FROM sys.schemas AS [schemas]
    INNER JOIN sys.objects AS [objects]
        ON objects.schema_id = schemas.schema_id
            AND objects.type_desc = 'USER_TABLE'
    INNER JOIN sys.columns AS [columns]
        ON columns.object_id = objects.object_id --573
    INNER JOIN sys.types AS [types]
        ON types.system_type_id = columns.system_type_id
            AND types.user_type_id = columns.user_type_id
    --FOR JSON AUTO
```
