
@ECHO OFF

SETLOCAL

CALL container-config %*

CALL docker compose --project-name %APP_PROJECT% --file docker-compose-cpu.yml stop

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL