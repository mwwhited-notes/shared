DROP FUNCTION IF EXISTS [dbo].[LongestCommonPrefix];
GO
 --=============================================
 --Author:		Matthew Whited
 --Create date: 11/12/2024
 --Description:	This function will compare to strings and return the longest matching prefix
 --=============================================
CREATE FUNCTION [dbo].[LongestCommonPrefix]
(
	 @word1 NVARCHAR(MAX)
	,@word2 NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
WITH SCHEMABINDING
AS
BEGIN
    RETURN (
		SELECT 
			 SUBSTRING(@word1, 1, MAX(LEN(SUBSTRING(@word1, 1, [$Numbers].[Number]))))
		FROM (	
			SELECT
                --if using 2022 or newer you can use ordinal parameter instead of row_number
				ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS [Number] 
			FROM STRING_SPLIT(REPLICATE(',', LEN(@word1)),',') 
		) AS [$Numbers]
		WHERE 
				[$Numbers].[Number] <= LEN(@word1)
			AND SUBSTRING(@word1, 1, [$Numbers].[Number]) = SUBSTRING(@word2, 1, [$Numbers].[Number])
    );
END;
