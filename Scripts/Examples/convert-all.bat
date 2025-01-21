@ECHO OFF

SETLOCAL

FOR %%f in (*.pdf) DO CALL :convert "%%f"
FOR %%f in (*.zip) DO CALL :unzip "%%f"

ENDLOCAL

EXIT /B

:convert
SET fileName=%~1
SET outfileName=%~n1.zip

IF EXIST "%outfileName%" (    
    ECHO Exists: %outfileName%
) ELSE (
    ECHO Convert: %fileName% -^> %outfileName%
    REM CALL curl -X "POST" "http://127.0.0.1:8081/api/v1/misc/extract-images" -H "accept: */*" -H "Content-Type: multipart/form-data" -F "fileInput=@%fileName%;type=application/pdf" -F "format=png" -F "allowDuplicates=true" --output "%outfileName%"
    CALL curl -X "POST" "http://127.0.0.1:8081/api/v1/convert/pdf/img" -H "accept: */*" -H "Content-Type: multipart/form-data" -F "fileInput=@%fileName%;type=application/pdf" -F "imageFormat=png" -F "singleOrMultiple=multiple" -F "pageNumbers=all" -F "colorType=greyscale" -F "dpi=300" --output "%outfileName%"
)
EXIT /B

:unzip
SET fileName=%~1
REM SET outfileName=%~n1
SET outfileName=Pages

    ECHO Unzip: %fileName% -^> %outfileName%
    CALL 7z e "%fileName%" -o"%outfileName%" -y

EXIT /B

