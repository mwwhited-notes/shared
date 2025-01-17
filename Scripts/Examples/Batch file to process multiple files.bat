
SETLOCAL

FOR %%f in (*.pdf) DO ^
CALL :get-images "%%f"

ENDLOCAL

EXIT /B

:get-images
SET fileName=%~1
ECHO Input: %fileName%
call curl -X "POST" "http://127.0.0.1:8081/api/v1/misc/extract-images" -H "accept: */*" -H "Content-Type: multipart/form-data" -F "fileInput=@%fileName%;type=application/pdf" -F "format=png" -F "allowDuplicates=true" --output "%fileName%.zip"

EXIT /B