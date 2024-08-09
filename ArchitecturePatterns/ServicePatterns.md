# Service Patterns

## Active Service

An Active Server is an application component that actively processes incoming requests, managing session state and returning responses while orchestrating interactions between services and resources.

### Class Diagram

```plantuml
@startuml
class ActiveServer {
    + handleRequest(request: Request)
    + sendResponse(response: Response)
}

class Request {
    - requestData
    + getData()
}

class Response {
    - responseData
    + setData(data: String)
}

class Session {
    - sessionId
    - userData
    + getUserData()
    + setUserData(data: String)
}

ActiveServer --> Request
ActiveServer --> Response
ActiveServer --> Session
@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Request
control ActiveServer
participant Session
participant Response

Request -> ActiveServer: handleRequest(request)
  activate ActiveServer
  ActiveServer -> Session: getUserData()
    activate Session
    return userData
  ActiveServer -\ Response: setData(responseData)
  return sendResponse(response)
@enduml
```

## Enterprise Service Bus (ESB)

An Enterprise Service Bus or ESB provides routing, transformation, mediation and much more.  The primary intention of an ESB is to separate the service dependencies between application within a particular enterprise.

### Component Diagram

```plantuml
@startuml
title Service Pattern - Enterprise Service Bus (ESB)

frame "Client 1"
frame "Client 2"

cloud "API Gateway"

queue "Enterprise Service Bus" As ESB

node "Service A"
node "Service B"
node "Service C"

database "Data Store A"
database "Data Store B"
database "Data Store C"

folder "Notification Service"
folder "Logging Service"

[Client 1] --> ESB
[Client 2] --> ESB
[API Gateway] --> ESB

ESB <--> [Service A]
ESB <--> [Service B]
ESB <--> [Service C]

ESB --> [Notification Service]
ESB --> [Logging Service]

[Service A] --> [Data Store A]
[Service B] --> [Data Store B]
[Service C] --> [Data Store C]

@enduml
```

## Frontend for Backend

`Frontend for Backend` providers a means to desegregate backend services from frontend applications.  Features such as versioning, translation, authentication and more may be controlled independently per frontend application allowing for easier maintenance and deployments.

### Component Diagram

```plantuml
@startuml
title Service Pattern - Frontend for Backend

frame "Frontend A"
cloud "FeB A"

frame "Frontend B"
cloud "FeB B"


component "Service Registry"

package "A" {
  node "Service A"
  database "Data Store A"
}
package "B" {
  node "Service B"
  database "Data Store B"
}
package "C" {
  node "Service C"
  database "Data Store C"
}

[Frontend A] --> [FeB A]
[FeB A] ---> [Service Registry]

[Frontend B] --> [FeB B]
[FeB B] ---> [Service Registry]

[FeB A] --> [Service A]
[Service A] --> [Data Store A]

[FeB A] --> [Service B]
[FeB B] --> [Service B]
[Service B] --> [Data Store B]

[FeB B] --> [Service C]
[Service C] --> [Data Store C]

[Service A] ...> [Service Registry]
[Service B] ...> [Service Registry]
[Service C] ...> [Service Registry]

[Service A] ---> [Authentication Service]
[Service B] ---> [Authentication Service]
[Service C] ---> [Authentication Service]

@enduml
```

## Microservices

```plantuml
@startuml

title: Service Pattern - Microservices

() User

cloud "Front End" {
    [App Service 1] AS API_A1
    [App Service 2] AS API_A2
}

frame Service1 {
    [System Service 1] AS API_S1
    database Data1
}

frame Service2 {
    [System Service 2] AS API_S2
    database Data2
}

User --> API_A1
User --> API_A2
API_A2 --> API_S1
API_A1 --> API_S2
API_S1 -> API_S2

API_S1 -- Data1
API_S2 -- Data2

@enduml
```

## N-Tier, Layered

```plantuml
@startuml

title: Service Pattern - N-Tier

()User
[Presentation]
[Business]
database "Data Access" as DataAccess

User <-> Presentation
Presentation <--> Business
Business <--> DataAccess

@enduml
```

## Serverless

```plantuml
@startuml

title: Service Pattern - Serverless

() User

cloud "Front End" {
    cloud Func1
    cloud Func2
    cloud Func3
}
frame Services {
    cloud Func4

    database Data1
    queue Queue1
    database Data2
    Node Service    
}

User --> Func1
User --> Func2
User --> Func3

Func1 --> Data1
Func1 --> Queue1
Func2 --> Queue1
Func2 --> Data2
Func3 --> Service
Service -> Data2
Queue1 -> Func4
Func4 -> Data1

@enduml
```

## Service Host

A Service Host is an application component that manages the lifecycle and communication of multiple independent services, providing a centralized interface for client interactions.

### Class Diagram

```plantuml
@startuml
class ServiceHost {
    - services: List
    + start()
    + stop()
    + addService()
    + removeService()
}

class Service {
    - serviceName
    + execute()
}

class ServiceA {
    + execute()
}

class ServiceB {
    + execute()
}

ServiceHost --> Service
Service <|-- ServiceA
Service <|-- ServiceB
@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant ServiceHost
participant ServiceA
participant ServiceB

ServiceHost -> ServiceA: start()
activate ServiceA
  ServiceA -> ServiceA: execute()
return response

ServiceHost -> ServiceB: execute()
activate ServiceB
  ServiceB -> ServiceB: execute()
return  response
@enduml
```


## Sidecar

A Sidecar is an application component that is an external process in the same container or a secondary process in a related container to manage some cross cutting concern.  

```plantuml
@startuml

title: Service Pattern - Sidecar

package "Container" {
    [Sidecar Proxy] <<component>>
    [Primary Application] <<component>>
    [Sidecar Service] <<component>>
}

[Client] --> [Sidecar Proxy] : gRPC/HTTP Call
[Sidecar Proxy] --> [Primary Application] : gRPC/Named Pipes Communication
[Primary Application] --> [Sidecar Service] : gRPC/Named Pipes Communication

note left of [Client]
  External client making a request
  to the primary application
end note

note right of [Sidecar Proxy]
  Handles cross-cutting concerns
  (e.g., service discovery, translation)
end note

note right of [Primary Application]
  Handles core business logic and requests
end note

note right of [Sidecar Service]
  Handles cross-cutting concerns
  (e.g., logging, monitoring)
end note

@enduml
```
