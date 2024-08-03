# Service Patterns

## Circuit Breaker

Circuit Breakers are a design pattern used in software development to improve the stability and resilience of a system by preventing repeated attempts to execute an operation that is likely to fail. They help to manage failures and prevent cascading failures in distributed systems.

### Class Diagram

```plantuml
@startuml
class CircuitBreaker {
    - state: String
    - failureThreshold: int
    - recoveryTimeout: int
    + callService(): Response
    + recordFailure(): void
    + reset(): void
}

class Service {
    - serviceID: String
    + execute(): Response
}

class Response {
    - status: String
    - data: Object
}

class FailureHandler {
    + handleFailure(response: Response): void
}

class Metrics {
    - failureCount: int
    - successCount: int
    + updateMetrics(response: Response): void
}

CircuitBreaker --> Service : calls
CircuitBreaker --> FailureHandler : uses
CircuitBreaker --> Metrics : tracks

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Circuit Breaker" as CircuitBreaker
participant "Service" as Service
participant "Failure Handler" as FailureHandler
participant "Metrics" as Metrics
participant "Response" as Response

User -> CircuitBreaker : callService()
    activate CircuitBreaker
    CircuitBreaker -> Service : execute()
        activate Service
        return response

    alt response is a failure
        CircuitBreaker -> FailureHandler : handleFailure(response)
            activate FailureHandler
            return void

        CircuitBreaker -> Metrics : updateMetrics(response)
            activate Metrics
            return void
    end

    return response

@enduml
```

## Service Discovery

Service Discovery is a design pattern used in microservices architecture to enable automatic detection of devices and services on a network. It simplifies the process of locating services and ensures that applications can communicate efficiently and reliably.

### Class Diagram

```plantuml
@startuml
class ServiceRegistry {
    - services: Map<String, Service>
    + registerService(service: Service): void
    + deregisterService(serviceID: String): void
    + getService(serviceID: String): Service
}

class Service {
    - serviceID: String
    - serviceAddress: String
    - servicePort: int
}

class Client {
    - clientID: String
    + discoverService(serviceID: String): Service
}

class LoadBalancer {
    + balanceLoad(services: List<Service>): Service
}

ServiceRegistry --> Service : manages
Client --> ServiceRegistry : queries
LoadBalancer --> ServiceRegistry : fetches services

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Client" as Client
participant "Service Registry" as ServiceRegistry
participant "Service" as Service
participant "Load Balancer" as LoadBalancer

User -> Client : discoverService(serviceID)
    activate Client
    Client -> ServiceRegistry : getService(serviceID)
        activate ServiceRegistry
        return Service

    Client -> LoadBalancer : balanceLoad(services)
        activate LoadBalancer
        return selectedService

    return selectedService

@enduml
```

## Bulk Head

The Bulkhead pattern is a design pattern used in software development to improve system resilience by isolating components or services from one another. This approach prevents failures in one part of a system from cascading and affecting other parts, much like bulkheads in a ship that keep water from flooding the entire vessel.

### Class Diagram

```plantuml
@startuml
class Bulkhead {
    - name: String
    - capacity: int
    - currentLoad: int
    + executeTask(task: Task): Response
    + isAvailable(): boolean
}

class Task {
    - taskID: String
    - taskData: Object
    + run(): Response
}

class Response {
    - status: String
    - data: Object
}

class Resource {
    - resourceID: String
    + allocate(): void
    + release(): void
}

Bulkhead --> Task : manages
Bulkhead --> Resource : allocates resources
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Bulkhead" as Bulkhead
participant "Task" as Task
participant "Resource" as Resource

User -\ Bulkhead : executeTask(task)
    activate Bulkhead
    Bulkhead -> Task : run()
        activate Task
        return response

    Bulkhead -> Resource : allocate()
        activate Resource
        return void

    Bulkhead -\ User : response

    Bulkhead -> Resource : release()
        activate Resource
        return void

@enduml
```

## Stranger Fig

The Strangler Fig pattern is a design pattern used in software development to facilitate the gradual replacement of an existing system with a new one. This approach allows for incremental changes, minimizing risk and ensuring continuous operation during the migration process, much like how a strangler fig tree grows around and eventually replaces its host tree.

### Class Diagram

```plantuml
@startuml
class StranglerFig {
    - oldSystem: System
    - newSystem: System
    - routingLogic: String
    + routeRequest(request: Request): Response
    + migrateFeature(feature: Feature): void
}

class System {
    - systemID: String
    - endpoints: List<Endpoint>
    + handleRequest(request: Request): Response
}

class Request {
    - requestID: String
    - data: Object
}

class Response {
    - status: String
    - data: Object
}

class Feature {
    - featureID: String
    - functionality: String
}

StranglerFig --> System : manages
StranglerFig --> Feature : migrates
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Strangler Fig" as StranglerFig
participant "Old System" as OldSystem
participant "New System" as NewSystem
participant "Request" as Request
participant "Response" as Response

User -> StranglerFig : routeRequest(request)
    activate StranglerFig
    alt request handled by old system
        StranglerFig -> OldSystem : handleRequest(request)
            activate OldSystem
            return response
    else request handled by new system
        StranglerFig -> NewSystem : handleRequest(request)
            activate NewSystem
            return response
    end

    return response

@enduml
```

## Database per Service

The Database per Service pattern is a design pattern used in microservices architecture where each microservice has its own dedicated database. This approach ensures data encapsulation, reduces the risk of tight coupling between services, and allows each service to choose the most appropriate database technology for its requirements.

### Class Diagram

```plantuml
@startuml
class Service {
    - serviceID: String
    - database: Database
    + performAction(action: Action): Response
}

class Database {
    - dbName: String
    - dbType: String
    + query(query: String): ResultSet
    + update(data: Object): void
}

class Action {
    - actionID: String
    - payload: Object
}

class Response {
    - status: String
    - data: Object
}

Service --> Database : uses
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Service A" as ServiceA
participant "Database A" as DatabaseA

participant "Service B" as ServiceB
participant "Database B" as DatabaseB

User -> ServiceA : performAction(action)
    activate ServiceA
    ServiceA -> DatabaseA : query(query)
        activate DatabaseA
        return resultSet
    return response
    
User -> ServiceB : performAction(action)
    activate ServiceB
    ServiceB -> DatabaseB : query(query)
        activate DatabaseB
        return resultSet

    return response

@enduml
```

## Message Broker

A Message Broker is a design pattern used in distributed systems to facilitate communication between services by allowing them to send messages to each other without being directly connected. It decouples the sender and receiver, enabling asynchronous communication, load balancing, and improved scalability.

### Class Diagram

```plantuml
@startuml
class MessageBroker {
    - queues: Map<String, Queue>
    + sendMessage(queueName: String, message: Message): void
    + receiveMessage(queueName: String): Message
}

class Queue {
    - queueName: String
    - messages: List<Message>
    + enqueue(message: Message): void
    + dequeue(): Message
}

class Message {
    - messageID: String
    - content: String
    - timestamp: Date
}

class Producer {
    - producerID: String
    + publish(message: Message): void
}

class Consumer {
    - consumerID: String
    + consume(): Message
}

MessageBroker --> Queue : manages
Producer --> MessageBroker : sends
Consumer --> MessageBroker : receives

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Producer" as Producer
participant "Consumer" as Consumer

participant "Message Broker" as MessageBroker
participant "Queue" as Queue

alt Publisher
User -\ Producer : publish(message)
    activate Producer
    Producer -> MessageBroker : sendMessage(queueName, message)
        activate MessageBroker
        MessageBroker -> Queue : enqueue(message)
            activate Queue
            return message-id
        return message-id
    deactivate Producer
end 

alt Reader
User -> Consumer : consume()
    activate Consumer
    Consumer -> MessageBroker : receiveMessage(queueName)
        activate MessageBroker
        MessageBroker -> Queue : dequeue()
            activate Queue
            return message
        return message
    return message
end

@enduml
```

## Health Check

Health Checks are a design pattern used in software systems to monitor the status and performance of services. They provide a way to determine whether a service is operational, allowing for proactive management of service availability, load balancing, and automated recovery.

### Class Diagram

```plantuml
@startuml
class HealthCheck {
    - serviceID: String
    - status: String
    - responseTime: int
    + performCheck(): HealthStatus
}

class HealthStatus {
    - status: String
    - message: String
    - timestamp: Date
}

class Service {
    - serviceID: String
    + getHealthStatus(): HealthStatus
}

class HealthMonitor {
    + checkService(service: Service): HealthStatus
}

HealthCheck --> Service : monitors
HealthMonitor --> HealthCheck : initiates

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Health Monitor" as HealthMonitor
participant "Health Check" as HealthCheck

User -> HealthMonitor : checkService(service)
    activate HealthMonitor
    HealthMonitor -> HealthCheck : performCheck()
        activate HealthCheck
        return healthStatus

    return healthStatus

@enduml
```