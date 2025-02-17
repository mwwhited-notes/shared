@ECHO OFF

SETLOCAL

SET PROJECT_EXTENSION=
IF NOT "%1"=="" SET PROJECT_EXTENSION=-%1

CALL container-config.bat

CALL :pull-models %CONTAINER_OLLAMA_MODELS%

:EOF
ENDLOCAL
EXIT /B

:pull-models
IF NOT "%1"=="" (
    CALL :pull-model %1 
    SHIFT 
    GOTO :pull-models
)
EXIT /B

:pull-model
ECHO -- Pull Model "%1"
CALL docker exec -it --user root %CONTAINER_OLLAMA_NAME% ollama pull %1
EXIT /B
