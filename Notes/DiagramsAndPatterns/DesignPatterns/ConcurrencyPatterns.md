# Concurrency Patterns

## Actor Model

The Actor Model is a concurrency design pattern used in software development that treats "actors" as the fundamental units of computation. Each actor encapsulates its state and behavior, communicates with other actors through asynchronous message passing, and operates independently. This pattern simplifies the development of concurrent and distributed systems, enabling better scalability and fault tolerance.

### Class Diagram

```plantuml
@startuml
class Actor {
    - actorID: String
    - state: Object
    + receiveMessage(message: Message): void
    + sendMessage(target: Actor, message: Message): void
}

class Message {
    - messageID: String
    - content: Object
}

class Supervisor {
    - supervisorID: String
    + supervise(actor: Actor): void
    + handleFailure(actor: Actor): void
}

class System {
    - actors: List<Actor>
    + addActor(actor: Actor): void
    + removeActor(actor: Actor): void
}

Actor --> Message : processes
Supervisor --> Actor : supervises
System --> Actor : manages

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Actor" as Actor
participant "Message" as Message
participant "Supervisor" as Supervisor

User -> Actor : sendMessage(message)
    activate Actor
    Actor -> Message : process(content)
        activate Message
        return void

    Actor -> Supervisor : reportStatus()
        activate Supervisor
        return void

    return acknowledgment

@enduml
```

## Async/Await

Async/Await is a programming pattern that simplifies asynchronous programming by allowing developers to write asynchronous code in a synchronous style. It provides a way to work with promises more easily, improving code readability and maintainability while handling asynchronous operations without blocking the main execution thread.

This patterns is also known as Awaitable Futures and Promises.

### Class Diagram

```plantuml
@startuml
class AsyncOperation {
    - operationID: String
    + execute(): Promise<Result>
}

class Result {
    - status: String
    - data: Object
}

class Promise {
    + then(callback: Function): Promise
    + catch(callback: Function): Promise
}

class User {
    + performAsyncOperation(): void
}

AsyncOperation --> Promise : returns
User --> AsyncOperation : calls

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "AsyncOperation" as AsyncOperation
participant "Promise" as Promise
participant "Result" as Result

User -> AsyncOperation : execute()
    activate AsyncOperation
    AsyncOperation -> Promise : create()
        activate Promise
        Promise -> AsyncOperation : resolve(data)
        return promise

    User -> Promise : then(callback)
        activate Promise
        return Result

    User -\ Result : display(data)

@enduml
```

## Fork/Join

The Fork/Join pattern is a design pattern used in parallel programming to divide a task into smaller subtasks that can be executed concurrently (forked) and then combined (joined) to produce a final result. This pattern helps to efficiently utilize system resources and improve performance by breaking down complex tasks into manageable parts that can be processed in parallel.

### Class Diagram

```plantuml
@startuml
class ForkJoinTask {
    - taskID: String
    + compute(): Result
    + fork(): void
    + join(): Result
}

class Result {
    - data: Object
}

class SubTask {
    - taskID: String
    + compute(): Result
}

ForkJoinTask --> SubTask : divides into
ForkJoinTask --> Result : produces

@enduml
```

### Activity Diagram

```plantuml
@startuml
start
:Compute Main Task;
    :Fork Subtasks;
    fork
        :Compute Subtask 1;
        :Return Result 1;
    fork again
        :Compute Subtask 2;
        :Return Result 2;
    end fork
    :Join Results;
:Return Final Result;
stop
@enduml
```

## Pipelining

Pipelining is a design pattern used in software development to process data in stages, where each stage performs a specific transformation or operation on the data. This approach allows for concurrent processing of multiple data items, improving throughput and resource utilization by minimizing idle time between processing steps.

### Class Diagram

```plantuml
@startuml
class Pipeline {
    - stages: List<Stage>
    + addStage(stage: Stage): void
    + execute(input: Input): Output
}

class Stage {
    - stageID: String
    - processingLogic: String
    + process(data: Input): Output
}

class Input {
    - content: Object
}

class Output {
    - results: Object
}

Pipeline --> Stage : contains
Stage --> Input : processes
Stage --> Output : produces

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Pipeline" as Pipeline
participant "Stage 1" as Stage1
participant "Stage 2" as Stage2
participant "Stage 3" as Stage3

User -> Pipeline : execute(input)
    activate Pipeline
    Pipeline -> Stage1 : process(data)
        activate Stage1
        return intermediateOutput

    Pipeline -> Stage2 : process(intermediateOutput)
        activate Stage2
        return intermediateOutput2

    Pipeline -> Stage3 : process(intermediateOutput2)
        activate Stage3
        return finalOutput

    return finalOutput

@enduml
```

## Producer/Consumer

The Producer/Consumer pattern is a design pattern used in concurrent programming to manage the flow of data between two or more processes (producers and consumers) that operate asynchronously. Producers generate data and place it in a shared buffer, while consumers retrieve and process the data from the buffer. This pattern helps to decouple the production and consumption of data, allowing for more flexible and scalable applications.

### Class Diagram

```plantuml
@startuml
class Producer {
    - producerID: String
    + produce(data: Object): void
}

class Consumer {
    - consumerID: String
    + consume(): Object
}

class Buffer {
    - items: List<Object>
    - capacity: int
    + add(item: Object): void
    + remove(): Object
    + isFull(): boolean
    + isEmpty(): boolean
}

Producer --> Buffer : produces
Consumer --> Buffer : consumes

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Producer" as Producer
participant "Consumer" as Consumer
participant "Buffer" as Buffer

User -> Producer : produce(data)
    activate Producer
    Producer -> Buffer : add(item)
        activate Buffer
        return
    return

User -> Consumer : consume()
    activate Consumer
    Consumer -> Buffer : remove()
        activate Buffer
        return item
    return item

@enduml
```

## Read/Write Lock

Read/Write Locks are a concurrency control pattern used to manage access to shared resources in a multithreaded environment. This pattern allows multiple readers to access the resource simultaneously while ensuring that only one writer can modify the resource at a time. This improves performance in scenarios where reads are more frequent than writes.

### Class Diagram

```plantuml
@startuml
class ReadWriteLock {
    - readCount: int
    - writeCount: int
    - readLock: Lock
    - writeLock: Lock
    + acquireReadLock(): void
    + releaseReadLock(): void
    + acquireWriteLock(): void
    + releaseWriteLock(): void
}

class Lock {
    - lockID: String
    + acquire(): void
    + release(): void
}

class Resource {
    - data: Object
    + read(): Object
    + write(data: Object): void
}

ReadWriteLock --> Lock : uses
ReadWriteLock --> Resource : manages

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User
control Service

participant "ReadWriteLock" as ReadWriteLock
participant "Lock" as Lock
participant "Resource" as Resource

par Accessor 1
User -> Service
    activate Service
    Service -> ReadWriteLock : acquireWriteLock()
        activate ReadWriteLock
        ReadWriteLock -> Lock : acquire()
            activate Lock
            return
        return

    Service -> Resource : write(data)
        activate Resource
        return

    Service -> ReadWriteLock : releaseWriteLock()
        activate ReadWriteLock
        ReadWriteLock -> Lock : release()
            activate Lock
            return
        return
    return
end

par Accessor 2
User -> Service
    activate Service
    Service -> ReadWriteLock : acquireWriteLock()
        activate ReadWriteLock
        ReadWriteLock -> Lock : acquire()
            activate Lock
            return
        return

    Service -> Resource : write(data)
        activate Resource
        return

    Service -> ReadWriteLock : releaseWriteLock()
        activate ReadWriteLock
        ReadWriteLock -> Lock : release()
            activate Lock
            return
        return
    return
end

@enduml
```
