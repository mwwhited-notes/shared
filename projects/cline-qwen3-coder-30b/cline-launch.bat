@echo off
REM Cline CLI launcher for Windows with Docker + Ollama
REM Usage: cline-launch.bat [optional: model name]
REM
REM Assumes:
REM - Docker Desktop is installed
REM - Ollama is running on host (ollama serve)
REM - cline-local image is built (docker build -t cline-local .)

setlocal enabledelayedexpansion

REM Model selection (default to qwen3-coder)
if "%1"=="" (
    set MODEL=qwen3-coder
) else (
    set MODEL=%1
)

REM Current working directory
set WORKSPACE=%CD%

echo.
echo ====================================
echo Launching Cline with Local Ollama
echo ====================================
echo Workspace: %WORKSPACE%
echo Model: %MODEL%
echo Working directory will be mapped to /workspace in container
echo.
echo Prerequisites:
echo  - Docker Desktop running
echo  - Ollama server running on host (ollama serve)
echo  - Model already pulled (ollama pull %MODEL%)
echo.

REM Check if Docker is available
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker not found. Install Docker Desktop.
    exit /b 1
)

REM Check if cline-local image exists, if not build it
docker image inspect cline-local >nul 2>&1
if errorlevel 1 (
    echo Building cline-local Docker image...
    docker build -t cline-local .
    if errorlevel 1 (
        echo ERROR: Failed to build Docker image
        exit /b 1
    )
)

REM Launch Cline in Docker with workspace mounted
echo Starting Cline CLI...
echo(

docker run -it --rm ^
  -v "%WORKSPACE%":/workspace ^
  -e OLLAMA_API_URL=http://host.docker.internal:11434 ^
  -e OLLAMA_MODEL=%MODEL% ^
  cline-local

echo(
echo Cline session ended.
echo(
