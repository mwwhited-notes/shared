@ECHO OFF

SETLOCAL

CALL container-config %*

CALL docker compose ^
--project-name %APP_PROJECT% ^
--file docker-compose-%APP_MODE%.yaml ^
build %EXTRA_ARGS%

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL