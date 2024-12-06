
SET SONARQUBE_KEY=XXX
SET SONARQUBE_TOKEN=YYY

dotnet tool restore

echo "Git fetch"
git fetch --prune
FOR /F "tokens=* USEBACKQ" %%g IN (`dotnet gitversion /output json /showvariable FullSemVer`) DO (SET BUILD_VERSION=%%g)
if "%BUILD_VERSION%"=="" GOTO error
ECHO Building Version=  "%BUILD_VERSION%"

dotnet sonarscanner begin ^
/k:"%SONARQUBE_KEY%" ^
/d:sonar.host.url="http://localhost:9000" ^
/d:sonar.token="%SONARQUBE_TOKEN%" ^
/d:sonar.cs.vscoveragexml.reportsPaths=.\TestResults\coverage.xml ^
/v:"%BUILD_VERSION%"

RMDIR /S .\TestResults
CALL build.bat
dotnet coverage collect "dotnet test" -f xml -o ".\TestResults\coverage.xml"

dotnet sonarscanner end ^
/d:sonar.token="%SONARQUBE_TOKEN%"