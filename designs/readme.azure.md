# C-Sharpening

## Summary

This is an area to learn more about C# and programming in general

## Design

### System Component Model

```plantuml

!include <azure/AzureCommon.puml>
!include <azure/Compute/all.puml>
!include <azure/Analytics/all.puml>
!include <azure/Storage/all.puml>
!include <azure/Databases/all.puml>

[Sensor Gateway] as aggregator
[Sensor 1] as sensor1
[Sensor 2] as sensor2

AzureQueueStorage(events, "Event Bus", "Instance 1")
AzureAppService(apiServices, "API Gateway", "Instance 1")
AzureFunction(handler1, "Event Handler 1", "Instance 1")
AzureFunction(handler2, "Event Handler 2", "Instance 1")
AzureFunction(handler3, "Event Handler 3", "Instance 1")
AzureSqlDatabase(db, "Data Store", "Instance 1")
AzureStorage(UI, "Front End", "Instance 1")

sensor1 --> aggregator : serial
sensor2 --> aggregator : serial

aggregator --> apiServices : http
apiServices --> events : enqueue
apiServices <--> db : sql

events --> handler1 : msg
handler1 --> apiServices

events --> handler2 : msg
handler2 --> events : msg

events --> handler3 : msg

UI -> apiServices : command(msg)
UI <-> apiServices : query

```