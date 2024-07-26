# Behavioral Patterns

## Blackboard

The blackboard pattern allows discrete state management across multiple knowledge source providers.  Each knowledge provider owns its own validate and data lookup.  Shared state is stored in the Blackboard and access in managed through the control. 

```plantuml

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
```

## Chain of Responsibility

Chain of Responsibility provides a means to decouple the requester from the actual handler. If the called operation is not able to complete the request it is passed on to the next handler in the chain until the chain ends or the request is handled.

```plantuml
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
```

## Command

The command pattern allows for defining a common means to execute operations.  This allows for decoupling the caller from the handler.

```plantuml
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
```