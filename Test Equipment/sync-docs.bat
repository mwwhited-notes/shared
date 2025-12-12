@echo off
REM ============================================================================
REM sync-docs.bat
REM Syncs test equipment documentation to OneDrive
REM ============================================================================

setlocal EnableDelayedExpansion

REM Configuration
set "SOURCE=%~dp0"
set "DEST=%USERPROFILE%\OneDrive\Documents\TestEquipment"

REM Remove trailing backslash from source if present
if "%SOURCE:~-1%"=="\" set "SOURCE=%SOURCE:~0,-1%"

echo ============================================================================
echo  Test Equipment Documentation Sync
echo ============================================================================
echo.
echo  Source: %SOURCE%
echo  Destination: %DEST%
echo.

REM Check if OneDrive folder exists
if not exist "%USERPROFILE%\OneDrive\Documents" (
    echo ERROR: OneDrive Documents folder not found.
    echo        Please ensure OneDrive is configured and syncing.
    echo        Expected path: %USERPROFILE%\OneDrive\Documents
    pause
    exit /b 1
)

REM Create destination if it doesn't exist
if not exist "%DEST%" (
    echo Creating destination folder...
    mkdir "%DEST%"
    if errorlevel 1 (
        echo ERROR: Failed to create destination folder.
        pause
        exit /b 1
    )
)

echo Starting sync...
echo.

REM Use robocopy for reliable sync
REM Options:
REM   /MIR    - Mirror mode (sync deletions too)
REM   /E      - Copy subdirectories including empty ones
REM   /Z      - Restartable mode (for large files)
REM   /W:3    - Wait 3 seconds between retries
REM   /R:2    - Retry 2 times on failure
REM   /NP     - No progress percentage (cleaner output)
REM   /NDL    - No directory list (less verbose)
REM   /NFL    - No file list (less verbose) - comment out to see files
REM   /XF     - Exclude files
REM   /XD     - Exclude directories

robocopy "%SOURCE%" "%DEST%" /MIR /E /Z /W:3 /R:2 /NP /XF "sync-docs.bat" /XD ".git" "__pycache__" "node_modules"

REM Robocopy exit codes:
REM   0 = No files copied, no errors
REM   1 = Files copied successfully
REM   2 = Extra files/dirs detected (with /MIR, these are deleted)
REM   3 = Files copied + extra files detected
REM   4 = Mismatched files/dirs
REM   8+ = Errors occurred

set "ROBOCOPY_EXIT=%ERRORLEVEL%"

echo.
echo ============================================================================

if %ROBOCOPY_EXIT% LEQ 3 (
    echo  Sync completed successfully.
    echo  Exit code: %ROBOCOPY_EXIT%
) else if %ROBOCOPY_EXIT% EQU 4 (
    echo  Sync completed with mismatches. Check files manually.
    echo  Exit code: %ROBOCOPY_EXIT%
) else (
    echo  ERROR: Sync failed with errors.
    echo  Exit code: %ROBOCOPY_EXIT%
)

echo ============================================================================
echo.

REM Show summary
echo Destination contents:
dir /b "%DEST%"

echo.
pause
exit /b %ROBOCOPY_EXIT%
