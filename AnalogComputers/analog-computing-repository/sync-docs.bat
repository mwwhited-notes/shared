@echo off
SET TARGET_FOLDER=C:\Users\mwwhi\OneDrive\Analog Computers\

SET FOLDER1=.\09-datasheets\pdfs
SET FOLDER2=.\10-application-notes\pdfs
SET FOLDER3=.\11-aerospace-simulation\pdfs
SET FOLDER4=.\12-analog-computer-docs

ROBOCOPY "%FOLDER1%" "%TARGET_FOLDER%datasheets" *.pdf /MIR
ROBOCOPY "%FOLDER2%" "%TARGET_FOLDER%application-notes" *.pdf /MIR
ROBOCOPY "%FOLDER3%" "%TARGET_FOLDER%aerospace-simulation" *.pdf /MIR
ROBOCOPY "%FOLDER4%" "%TARGET_FOLDER%analog-computer-docs" *.pdf /MIR /S
