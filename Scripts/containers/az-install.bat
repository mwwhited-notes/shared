@REM CALL az login 

SET APP_RESOURCE_GROUP=Personal.MWhitted
SET APP_ENVIRONMENT=open-webui-demo

ECHO APP_RESOURCE_GROUP=%APP_RESOURCE_GROUP%
ECHO APP_ENVIRONMENT=%APP_ENVIRONMENT%

@REM CALL az configure --defaults group=%APP_RESOURCE_GROUP%

CALL az containerapp env create --resource-group %APP_RESOURCE_GROUP% --name %APP_ENVIRONMENT%
CALL az containerapp compose create --resource-group %APP_RESOURCE_GROUP% --environment %APP_ENVIRONMENT% --compose-file-path .\docker-compose.yaml
CALL az containerapp compose create --resource-group %APP_RESOURCE_GROUP% --environment %APP_ENVIRONMENT% --compose-file-path .\docker-compose.apache-tika.yaml
CALL az containerapp compose create --resource-group %APP_RESOURCE_GROUP% --environment %APP_ENVIRONMENT% --compose-file-path .\docker-compose.searxng.yaml
