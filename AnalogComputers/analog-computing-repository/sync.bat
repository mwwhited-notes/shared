SET TARGET_FOLDER=C:\Users\mwwhi\OneDrive\Analog Computers\

SET FOLDER1=.\analog-computing-repository\09-datasheets\pdfs\*.pdf
SET FOLDER2=.\analog-computing-repository\10-application-notes\pdfs\*.pdf
SET FOLDER3=.\analog-computing-repository\11-aerospace-simulation\pdfs\*.pdf

ROBOCOPY "%FOLDER1%" "%TARGET_FOLDER%datasheets" /MIR
ROBOCOPY "%FOLDER2%" "%TARGET_FOLDER%application-notes" /MIR
ROBOCOPY "%FOLDER3%" "%TARGET_FOLDER%aerospace-simulation" /MIR