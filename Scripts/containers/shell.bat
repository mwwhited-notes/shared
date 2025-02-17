@ECHO OFF
SETLOCAL

IF NOT "%1"=="" SET TARGET_MACHINE=%1

CALL container-config

CALL docker exec -it --user root %CONTAINER_GROUP%-%TARGET_MACHINE%-1 bash

ENDLOCAL