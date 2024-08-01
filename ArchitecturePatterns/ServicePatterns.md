# Service Patterns

## N-Tier

```plantuml
title: Service Pattern - N-Tier

()User
[Presentation]
[Business]
database "Data Access" as DataAccess

User <-> Presentation
Presentation <--> Business
Business <--> DataAccess
```

## Microservices

```plantuml
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
```

## Serverless

```plantuml
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
```

## Sidecar

A Sidecar is an application component that is an external process in the same container or a secondary process in a related container to manage some cross cutting concern.  

```plantuml
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

```
