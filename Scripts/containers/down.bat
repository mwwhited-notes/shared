@ECHO OFF

SETLOCAL

CALL container-config %*

SET EXTRA_ARGS=
IF /I "%1" EQU "ALL" (
    SET EXTRA_ARGS=--volumes 
)

CALL docker compose --project-name %APP_PROJECT% down %EXTRA_ARGS%

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL