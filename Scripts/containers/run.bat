@ECHO OFF
SETLOCAL
CALL container-config.bat

CALL pull && ^
CALL build && ^
CALL up && ^
CALL pull-models

ENDLOCAL