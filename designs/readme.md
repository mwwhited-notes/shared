# C-Sharpening

## Summary

This is an area to learn more about C# and programming in general

## Design

### System Component Model

```plantuml

[Sensor Gateway] as aggregator
[Sensor 1] as sensor1
[Sensor 2] as sensor2
[Event Bus] as events
[API Gateway] as apiServices
[Event Handler 1] as handler1
[Event Handler 2] as handler2
[Event Handler 3] as handler3
[Front End] as UI
[Data Store] as db


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