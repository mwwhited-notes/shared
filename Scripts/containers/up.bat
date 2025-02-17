@ECHO OFF

SETLOCAL

CALL container-config %*

IF /I "%1" EQU "clean" (
    SET EXTRA_ARGS=--remove-orphans %EXTRA_ARGS%
    SHIFT
)

IF /I "%1" NEQ "interactive" (
    SET EXTRA_ARGS=--detach %EXTRA_ARGS% 
)

CALL docker compose ^
--project-name %APP_PROJECT% ^
--file docker-compose-%APP_MODE%.yaml ^
up %EXTRA_ARGS%

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL