
@ECHO OFF

SETLOCAL

CALL container-config

IF "%APP_PROJECT%"=="" SET APP_PROJECT=%CONTAINER_GROUP%

CALL docker compose ^
--project-name %APP_PROJECT% ^
--file docker-compose-gpu.yml ^
build

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL