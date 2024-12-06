
@ECHO OFF

SETLOCAL

CALL container-config

IF "%APP_PROJECT%"=="" SET APP_PROJECT=%CONTAINER_GROUP%

CALL docker compose --project-name %APP_PROJECT% --file docker-compose-cpu.yml up --detach

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL