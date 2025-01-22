
@ECHO OFF

SETLOCAL

CALL container-config %*

ECHO Starting %APP_PROJECT% as %APP_MODE%

CALL docker compose --project-name %APP_PROJECT% --file docker-compose-%APP_MODE%.yml up --detach

GOTO :EOF

:ERROR
ECHO Error Code: %LAST_ERROR%
EXIT /B %LAST_ERROR%

:EOF
ENDLOCAL