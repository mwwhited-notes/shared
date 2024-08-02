# Behavioral Patterns

## Blackboard

The blackboard pattern allows discrete state management across multiple knowledge source providers.  Each knowledge provider owns its own validate and data lookup.  Shared state is stored in the Blackboard and access in managed through the control. 

[Example](../Examples/BehaviorBlackboard/)

### Class Diagram

```plantuml
@startuml

interface IControl {
    + Add(IKnowledgeSource)
    + Post(string key, object? value)
    + Snapshot() IDictionary<string, object>
    - OnChange(IBlackboard, IEventData)
}

interface IBlackboard {
  + State Dictionary<string, object>
  + OnChanged EventHandler<(IBlackboard, IEventData)>
  + Set(object source, string key, object? value)
}

interface IEventData {
    + Key string
    + Value object?
}

interface IKnowledgeSource {
    + Handler(IBlackboard, IEventData)
}

class KnowledgeSource1 implements IKnowledgeSource {
}

class KnowledgeSource2 implements IKnowledgeSource {
}

class KnowledgeSourceN implements IKnowledgeSource {
}

class Control implements IControl {
}
class Blackboard implements IBlackboard {
}

KnowledgeSource1 --> IBlackboard : read/write
KnowledgeSource2 --> IBlackboard : read/write
KnowledgeSourceN --> IBlackboard : read/write
Blackboard --> IControl  : onChange
Control --> IBlackboard : read/write
Control --> IBlackboard : get state
Control --> IKnowledgeSource : call

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Controller
participant Blackboard
participant KnowledgeSource1
participant KnowledgeSource2

activate Controller
Controller -> Blackboard: Initialize()
activate Blackboard
  Controller -> KnowledgeSource1: Request Data/Action()
    activate KnowledgeSource1
    return Provide Data/Action()
  Controller -> KnowledgeSource2: Request Data/Action()
    activate KnowledgeSource2
    return Provide Data/Action()
Controller -> Blackboard: Retrieve Combined Data/Action()
Controller -> Blackboard: Finalize()

@enduml
```

## Chain of Responsibility

Chain of Responsibility provides a means to decouple the requester from the actual handler. If the called operation is not able to complete the request it is passed on to the next handler in the chain until the chain ends or the request is handled.

### Class Diagram

```plantuml
@startuml
abstract class Handler {
  + SetNext(handler: Handler)
  + HandleRequest(request: string)
}

class ConcreteHandler1 {
  + HandleRequest(request: string)
}

class ConcreteHandler2 {
  + HandleRequest(request: string)
}

class ConcreteHandler3 {
  + HandleRequest(request: string)
}

Handler <|-- ConcreteHandler1
Handler <|-- ConcreteHandler2
Handler <|-- ConcreteHandler3
Handler --> Handler : nextHandler

@enduml
```

###  Sequence Diagram

```plantuml
@startuml
participant Client
participant Handler1
participant Handler2
participant Handler3

Client -> Handler1: HandleRequest(request)
activate Handler1
alt Handler1 can handle
    Handler1 -> Handler1: Process request
else Handler1 can't handle
    Handler1 -> Handler2: HandleRequest(request)
    activate Handler2
    alt Handler2 can handle
        Handler2 -> Handler2: Process request
    else Handler2 can't handle
        Handler2 -> Handler3: HandleRequest(request)
        activate Handler3
        alt Handler3 can handle
            Handler3 -> Handler3: Process request
        else Handler3 can't handle
            Handler3 -> Handler3: Request not handled
        end
    end
end
@enduml
```

## Command

The command pattern allows for defining a common means to execute operations.  This allows for decoupling the caller from the handler.

## Class Diagram

```plantuml
@startuml
interface ICommand {
    +Execute()
}

class ConcreteCommand1 {
    +Execute()
}

class ConcreteCommand2 {
    +Execute()
}

class Invoker {
    +SetCommand(command: ICommand)
    +ExecuteCommand()
}

class Receiver {
    +Action1()
    +Action2()
}

ICommand <|.. ConcreteCommand1
ICommand <|.. ConcreteCommand2
Invoker --> ICommand
ConcreteCommand1 --> Receiver
ConcreteCommand2 --> Receiver

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Caller
participant Command
participant CommandHandler1
participant CommandHandler2

Caller -> Command: Create Command
activate Command
Command -> CommandHandler1: Execute()
activate CommandHandler1
CommandHandler1 -> CommandHandler1: Process Command
deactivate CommandHandler1
Command -> CommandHandler2: Execute()
activate CommandHandler2
CommandHandler2 -> CommandHandler2: Process Command
deactivate CommandHandler2
deactivate Command

@enduml
```

## Interpreter 

Interpreters are used to declare a graph based representation of a syntax expression such as the abstract syntax tree (AST) behind a expression parser.

### Class Diagram

```plantuml
@startuml
interface IExpression {
    +Interpret(context: string): int
}

class TerminalExpression implements IExpression {
    +Interpret(context: string): int
}

class NonterminalExpression implements IExpression {
    +Interpret(context: string): int
}

class Context {
    +input: string
    +output: int
}

Context --> IExpression : uses

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Client
participant Context
participant Interpreter
participant TerminalExpression
participant NonTerminalExpression

Client -> Interpreter: Interpret(expression)
activate Interpreter
Interpreter -> Context: Set Context
activate Context

alt If expression is terminal
    Interpreter -> TerminalExpression: Interpret()
    activate TerminalExpression
    TerminalExpression -> Context: Process Terminal Expression
    deactivate TerminalExpression
else If expression is non-terminal
    Interpreter -> NonTerminalExpression: Interpret()
    activate NonTerminalExpression
    NonTerminalExpression -> Context: Process Non-Terminal Expression
    deactivate NonTerminalExpression
end

deactivate Context
deactivate Interpreter

@enduml
```

## Iterator or Cursor

Iterators are used to access the elements of a set of objects sequentially.

### Class Diagram

```plantuml
@startuml
interface IIterator {
    +HasNext() : bool
    +Next() : Object
}

interface IAggregate {
    +CreateIterator() : IIterator
}

class ConcreteIterator implements IIterator {
    - collection : ConcreteAggregate
    - current : int
    +HasNext() : bool
    +Next() : Object
}

class ConcreteAggregate implements IAggregate {
    +CreateIterator() : IIterator
    - items : List<Object>
    +Count : int
    +GetItem(index: int) : Object
}

ConcreteAggregate --> ConcreteIterator
ConcreteAggregate --> Object

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Client
participant Collection
participant Iterator

Client -> Collection: Create Iterator()
activate Collection
Collection -> Iterator: Get Iterator()
deactivate Collection
activate Iterator

Client -> Iterator: Next()
alt Has Next
    Iterator -> Iterator: Move Next()
    Iterator -> Client: Return Current Item
else No More Items
    Iterator -> Client: Return Null or Exception
end

Client -> Iterator: HasNext()
alt Has Next
    Iterator -> Client: Return True
else No More Items
    Iterator -> Client: Return False
end

Client -> Iterator: Next()
alt Has Next
    Iterator -> Iterator: Move Next()
    Iterator -> Client: Return Current Item
else No More Items
    Iterator -> Client: Return Null or Exception
end

Client -> Iterator: Release Iterator()
deactivate Iterator

@enduml
```

## Mediator

Mediator is used as a meant ot separate object interactions.  

```plantuml
@startuml
interface IMediator {
    +Notify(sender: Component, event: string): void
}

abstract class Component {
    protected mediator: IMediator
    +SetMediator(mediator: IMediator): void
}

class ConcreteMediator implements IMediator {
    -component1: ConcreteComponent1
    -component2: ConcreteComponent2
    +ConcreteMediator(component1: ConcreteComponent1, component2: ConcreteComponent2)
    +Notify(sender: Component, event: string): void
}

class ConcreteComponent1 extends Component {
    +DoA(): void
    +DoB(): void
}

class ConcreteComponent2 extends Component {
    +DoC(): void
    +DoD(): void
}

ConcreteMediator --> ConcreteComponent1
ConcreteMediator --> ConcreteComponent2

@enduml
```

## Memento

Memento is a mean to capture/replay state for an applications.  Examples use cases may include undo/redo functionality or change a change log.

### Class Diagram

```plantuml
@startuml
class Originator {
    - state: String
    + SetState(state: String): void
    + GetState(): String
    + SaveState(): Memento
    + RestoreState(memento: Memento): void
}

class Memento {
    - state: String
    + Memento(state: String)
    + GetState(): String
}

class Caretaker {
    - memento: Memento
    + GetMemento(): Memento
    + SetMemento(memento: Memento): void
}

Originator --> Memento
Caretaker --> Memento

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Originator
participant Memento
participant Caretaker

Originator -> Originator: SetState(state)
activate Originator
Originator -> Caretaker: SaveState()
activate Caretaker
Caretaker -> Originator: CreateMemento()
activate Memento
Originator -> Memento: GetState()
deactivate Memento
deactivate Caretaker

Originator -> Originator: SetState(newState)

Caretaker -> Originator: RestoreState()
activate Caretaker
Caretaker -> Originator: GetMemento()
activate Memento
Originator -> Memento: RestoreState()
deactivate Memento
deactivate Caretaker

@enduml
```

## Observer, Dependents or Publisher/Subscriber

Observers are used to track changes and notify dependents.

### Class Diagram

```plantuml
@startuml
interface IObserver {
    + Update(subject: Subject): void
}

interface ISubject {
    + Attach(observer: IObserver): void
    + Detach(observer: IObserver): void
    + Notify(): void
}

class ConcreteSubject implements ISubject {
    - state: int
    - observers: List<IObserver>
    + GetState(): int
    + SetState(state: int): void
    + Attach(observer: IObserver): void
    + Detach(observer: IObserver): void
    + Notify(): void
}

class ConcreteObserver implements IObserver {
    - subject: ConcreteSubject
    + Update(subject: Subject): void
}

ConcreteSubject --> IObserver : maintains

@enduml
```

### Sequence Diagram

```plantuml
@startuml
participant Publisher as Subject
participant Subscriber1 as Observer1
participant Subscriber2 as Observer2

Subject -> Subject: SetState()
activate Subject
  Subject -> Subject: Notify()
  activate Subject

    alt Notify Observer1
        Subject -> Observer1: Update()
        activate Observer1
        Observer1 -> Observer1: Update State
        return
    end

    alt Notify Observer2
        Subject -> Observer2: Update()
        activate Observer2
        Observer2 -> Observer2: Update State
        return
    end

@enduml
```

## Specification

The Specifications pattern is used as a means to define combinable business logic

[Example](../Examples/BehaviorSpecification/)

### Class Diagram

```plantuml
@startuml
interface Specification {
    +isSatisfiedBy(entity): bool
}

class ConcreteSpecificationA {
    +isSatisfiedBy(entity): bool
}

class ConcreteSpecificationB {
    +isSatisfiedBy(entity): bool
}

class CompositeSpecification {
    +isSatisfiedBy(entity): bool
}

Specification <|-- ConcreteSpecificationA
Specification <|-- ConcreteSpecificationB
Specification <|-- CompositeSpecification

CompositeSpecification --> Specification : specifications
@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor Client
participant "CompositeSpecification" as Composite
participant "ConcreteSpecificationA" as SpecA
participant "ConcreteSpecificationB" as SpecB

Client -> Composite : isSatisfiedBy(Entity)
activate Composite

    Composite -> SpecA : isSatisfiedBy(Entity)
    activate SpecA
        SpecA -> SpecA : Check criteria
    deactivate SpecA

    Composite -> SpecB : isSatisfiedBy(Entity)
    activate SpecB
        SpecB -> SpecB : Check criteria
    deactivate SpecB
    
    return result
@enduml

```

## State

### Class Diagram

```plantuml
@startuml
class Context {
    -state: State
    +setState(state: State)
    +request()
}

interface State {
    +handle(context: Context)
}

class ConcreteStateA implements State {
    +handle(context: Context)
}

class ConcreteStateB implements State {
    +handle(context: Context)
}

Context --> State
@enduml
```

### Sequence Diagram

```plantuml
@startuml

actor Client
participant Context
participant ConcreteStateA
participant ConcreteStateB

Client -> Context: request()
activate Context
    Context -> ConcreteStateA: handle()
    activate ConcreteStateA
    return stateA
    Context -> Context : setState(stateA)

    Context -> ConcreteStateB: handle()
    activate ConcreteStateB
    return stateB
    Context -> Context : setState(stateB)
@enduml
```

## Strategy

The Strategy patterns allows for changing algorithm independently from the client.

### Class Diagram

```plantuml
@startuml

interface Strategy {
    +execute(data): void
}

class ConcreteStrategyA {
    +execute(data): void
}

class ConcreteStrategyB {
    +execute(data): void
}

class Context {
    -strategy: Strategy
    +setStrategy(strategy: Strategy): void
    +executeStrategy(data): void
}

Strategy <|-- ConcreteStrategyA
Strategy <|-- ConcreteStrategyB
Context --> Strategy : strategy

@enduml
```

### Sequence Diagram

```plantuml
@startuml

actor Client
participant "Context" as Context
participant "ConcreteStrategyA" as StrategyA
participant "ConcreteStrategyB" as StrategyB

Client -> Context : setStrategy(StrategyA)
activate Context
deactivate Context

Client -> Context : executeStrategy(data)
activate Context
    Context -> StrategyA : execute(data)
    activate StrategyA
        StrategyA -> StrategyA : Perform algorithm
    deactivate StrategyA
    Context -> Client : return result
deactivate Context

Client -> Context : setStrategy(StrategyB)
activate Context
deactivate Context

Client -> Context : executeStrategy(data)
activate Context
    Context -> StrategyB : execute(data)
    activate StrategyB
        StrategyB -> StrategyB : Perform algorithm
    deactivate StrategyB
    Context -> Client : return result
deactivate Context

@enduml
```

## Template Method

Template Methods provide a means to use object hierarchy to abstract your application specific implementation from a shared definition.

### Class Diagram

```plantuml
@startuml
abstract class AbstractClass {
    +templateMethod(): void
    #primitiveOperation1(): void
    #primitiveOperation2(): void
}

class ConcreteClassA {
    +primitiveOperation1(): void
    +primitiveOperation2(): void
}

class ConcreteClassB {
    +primitiveOperation1(): void
    +primitiveOperation2(): void
}

AbstractClass <|-- ConcreteClassA
AbstractClass <|-- ConcreteClassB
@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor Client
participant "ConcreteClassA" as ClassA
participant "ConcreteClassB" as ClassB
participant "AbstractClass" as AbstractClass

Client -> ClassA : templateMethod()
activate ClassA
    ClassA -> AbstractClass : templateMethod()
    activate AbstractClass
        AbstractClass -> ClassA : primitiveOperation1()
        activate ClassA
            ClassA -> ClassA : Execute specific logic
        deactivate ClassA
        AbstractClass -> ClassA : primitiveOperation2()
        activate ClassA
            ClassA -> ClassA : Execute specific logic
        deactivate ClassA
    deactivate AbstractClass
deactivate ClassA

Client -> ClassB : templateMethod()
activate ClassB
    ClassB -> AbstractClass : templateMethod()
    activate AbstractClass
        AbstractClass -> ClassB : primitiveOperation1()
        activate ClassB
            ClassB -> ClassB : Execute specific logic
        deactivate ClassB
        AbstractClass -> ClassB : primitiveOperation2()
        activate ClassB
            ClassB -> ClassB : Execute specific logic
        deactivate ClassB
    deactivate AbstractClass
deactivate ClassB
@enduml
```