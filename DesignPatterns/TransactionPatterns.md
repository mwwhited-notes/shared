# Transaction Patterns

## Saga

The Saga Design Pattern allows for transaction compensation on failure.

### Saga - Orchestration

```plantuml
@startuml
actor User
participant "Orchestrator" as Orchestrator
participant "Service A" as A
participant "Service B" as B
participant "Service C" as C

User -> Orchestrator: Start transaction
activate Orchestrator

Orchestrator -> A: Execute action A
activate A
A -> Orchestrator: Result A
deactivate A

Orchestrator -> B: Execute action B
activate B
B -> Orchestrator: Result B
deactivate B

Orchestrator -> C: Execute action C
activate C
C -> Orchestrator: Result C
deactivate C

Orchestrator -> User: Transaction completed
deactivate Orchestrator

note right of Orchestrator: If any service fails,\ntrigger optional compensation

alt Failure in Service B
    Orchestrator -> C: Compensate action C
    activate C
    C -> Orchestrator: Compensation C completed
    deactivate C

    Orchestrator -> B: Compensate action B
    activate B
    B -> Orchestrator: Compensation B completed
    deactivate B

    Orchestrator -> A: Compensate action A
    activate A
    A -> Orchestrator: Compensation A completed
    deactivate A

    Orchestrator -> User: Transaction compensated
else All services succeed
end

@enduml
```

### Saga - Choreography

```plantuml
@startuml

actor User
participant "Service A" as A
participant "Service B" as B
participant "Service C" as C

User -> A: Start transaction
activate A
A -> A: Process
A -> B: Notify action A completed
deactivate A

activate B
B -> B: Process
B -> C: Notify action B completed
deactivate B

activate C
C -> C: Process
C -> User: Transaction completed
deactivate C

note right of C: If any service fails,\nnotify previous services for compensation

alt Failure in Service B
    C -> B: Compensate action B
    activate B
    B -> B: Compensation
    B -> A: Notify compensation B completed
    deactivate B

    A -> A: Compensation
    deactivate A

    C -> User: Transaction compensated
else All services succeed
end

@enduml
```


## Two-Phase Commit (2PC)

Two-Phase Commit allows for commit/rollback coordination.

```plantuml
@startuml

actor Coordinator
participant "Participant A" as A
participant "Participant B" as B
participant "Participant C" as C

Coordinator -> A: Prepare
activate A
return Vote (Yes/No)

Coordinator -> B: Prepare
activate B
return Vote (Yes/No)

Coordinator -> C: Prepare
activate C
return Vote (Yes/No)

alt All votes are Yes
    Coordinator -> A: Commit
    activate A
    A -> Coordinator: Acknowledge commit
    deactivate A

    Coordinator -> B: Commit
    activate B
    B -> Coordinator: Acknowledge commit
    deactivate B

    Coordinator -> C: Commit
    activate C
    C -> Coordinator: Acknowledge commit
    deactivate C

    Coordinator -> Coordinator: Transaction completed successfully
else Any vote is No
    Coordinator -> A: Rollback
    activate A
    A -> Coordinator: Acknowledge rollback
    deactivate A

    Coordinator -> B: Rollback
    activate B
    B -> Coordinator: Acknowledge rollback
    deactivate B

    Coordinator -> C: Rollback
    activate C
    C -> Coordinator: Acknowledge rollback
    deactivate C

    Coordinator -> Coordinator: Transaction rolled back
end

@enduml
```

## Three-Phase Commit (3PC)

```plantuml
@startuml

actor Coordinator
participant "Participant A" as A
participant "Participant B" as B
participant "Participant C" as C

Coordinator -> A: Prepare
activate A
return Vote (Yes/No)

Coordinator -> B: Prepare
activate B
return Vote (Yes/No)

Coordinator -> C: Prepare
activate C
return Vote (Yes/No)

alt All votes are Yes
    Coordinator -> A: Pre-commit
    activate A
    return Acknowledge pre-commit

    Coordinator -> B: Pre-commit
    activate B
    return Acknowledge pre-commit

    Coordinator -> C: Pre-commit
    activate C
    return Acknowledge pre-commit

    Coordinator -> A: Commit
    activate A
    return Acknowledge commit

    Coordinator -> B: Commit
    activate B
    return Acknowledge commit

    Coordinator -> C: Commit
    activate C
    return Acknowledge commit

    Coordinator -> Coordinator: Transaction completed successfully
else Any vote is No
    Coordinator -> A: Rollback
    activate A
    return Acknowledge rollback

    Coordinator -> B: Rollback
    activate B
    return Acknowledge rollback

    Coordinator -> C: Rollback
    activate C
    return Acknowledge rollback

    Coordinator -> Coordinator: Transaction rolled back
end

@enduml
```

## Event Sourcing

With Event Sourcing data is stored as a collection of events.  This allows for reconstruction and compensation from any point. 

```plantuml
@startuml

actor User
participant "Command Handler" as CH
participant "Event Store" as ES
participant "Event Processor" as EP
participant "Read Model" as RM

User -> CH: Send command (e.g., Create Order)
activate CH
CH -> ES: Store event (e.g., OrderCreated)
deactivate CH

ES -> EP: Notify event (OrderCreated)
activate EP
EP -> RM: Update read model
deactivate EP

User -> RM: Query current state (e.g., Get Order)

@enduml
```

## Outbox

Outbox provides a means to store the outbound data in a temporary database before publishing final data as an event.


```plantuml
@startuml
actor User
participant "Service" as S
participant "Database" as DB
participant "Outbox Table" as OT
participant "Message Broker" as MB

User -> S: Send command (e.g., Create Order)
activate S

S -> DB: Update state (e.g., Insert Order)
S -> OT: Write event (OrderCreated)
deactivate S

note right of DB: Both the update and\noutbox entry occur\nin the same transaction.

OT -> MB: Publish event (OrderCreated)
activate MB
MB -> User: Notify event received
deactivate MB

@enduml

```