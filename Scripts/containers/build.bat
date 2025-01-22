
@ECHO OFF

SETLOCAL

CALL container-config %*

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