# Structural Patterns

## Adapter

Adapters are used to convert from one implementation to another.

```plantuml
@startuml

title: Structural Pattern - Adapter

interface Target {
    + request(): void
}

class Adapter implements Target {
    - adaptee: Adaptee
    + Adapter(adaptee: Adaptee)
    + request(): void 
}

class Adaptee {
    + specificRequest(): void
}

class Client {
    + clientRequest(target: Target): void 
}

Adapter --> Adaptee
Client --> Target

@enduml
```

## Bridge

Bridge pattern is used to decouple abstractions from implementations 

```plantuml
@startuml

title: Structural Pattern - Bridge

interface Implementor {
    + operationImpl(): void
}

class ConcreteImplementorA implements Implementor {
    + operationImpl(): void
}

class ConcreteImplementorB implements Implementor {
    + operationImpl(): void
}

abstract class BridgeAbstraction {
    - implementor: Implementor
    + BridgeAbstraction(implementor: Implementor)
    + operation(): void 
}

class RefinedAbstraction extends BridgeAbstraction {
    + RefinedAbstraction(implementor: Implementor): super(implementor)
    + operation(): void 
}

BridgeAbstraction o-- Implementor

@enduml
```

## Composite

Composite classes may be used to simplify multiple types into a single component.  This provides a means to represent complex hierarchies in a simplified fashion.

```plantuml
@startuml

title: Structural Pattern - Composite

interface Graphic {
    + draw() : void
}

class Circle implements Graphic {
    + draw() : void
}

class Square implements Graphic {
    + draw() : void
}

class CompositeGraphic implements Graphic {
    + add(graphic: Graphic) : void
    + remove(graphic: Graphic) : void
    + draw() : void
    - graphics : List<Graphic>
}

CompositeGraphic --> "1..*" Graphic : contains

@enduml
```

## Decorator / Wrapper

Decorators provide a means to add functionality to a object dynamically without sub-classing.

```plantuml
@startuml

title: Structural Pattern - Decorator

interface Component {
    + operation() : void
}

class Leaf implements Component {
    + operation() : void
}

class Composite implements Component {
    + add(component: Component) : void
    + remove(component: Component) : void
    + operation() : void
    - children : List<Component>
}

Composite --> "1..*" Component : contains

@enduml
```

## Facade

Facades may be used to isolated sub-systems of functionality into a simplified abstraction.  This provide a means to manage access to a collection of functionality in from a single point.

```plantuml
@startuml

title: Structural Pattern - Facade

class SubsystemA {
    + operationA1() : void
    + operationA2() : void
}

class SubsystemB {
    + operationB1() : void
    + operationB2() : void
}

class SubsystemC {
    + operationC1() : void
    + operationC2() : void
}

class Facade {
    - subsystemA : SubsystemA
    - subsystemB : SubsystemB
    - subsystemC : SubsystemC
    + operation() : void
}

Facade --> SubsystemA : uses
Facade --> SubsystemB : uses
Facade --> SubsystemC : uses

@enduml
```

## Flyweight

Flyweight provides a means to reduce resources by allowing child classed to reference the same implementation instead of creating their own.

```plantuml
@startuml

title: Structural Pattern - Flyweight

interface Flyweight {
    + operation(extrinsicState: String) : void
}

class ConcreteFlyweight implements Flyweight {
    - intrinsicState : String
    + operation(extrinsicState: String) : void
}

class FlyweightFactory {
    - flyweights : Map<String, Flyweight>
    + getFlyweight(key: String) : Flyweight
    + createFlyweight(key: String, intrinsicState: String) : Flyweight
}

FlyweightFactory --> Flyweight : manages

@enduml
```

## Marker/Tagging Interfaces

Marker interfaces are a means to provide additional metadata to your type definitions.   

```plantuml
@startuml

title: Structural Pattern - Marker Interface

interface MarkerInterface1
interface MarkerInterface2

class MyClass1
class MyClass2

MyClass1 ..|> MarkerInterface1
MyClass2 ..|> MarkerInterface2
MyClass2 ..|> MarkerInterface1

@enduml
```

## Proxy

Proxies are similar to an adapter but typically provide an additional layer such as logging or access control. 

```plantuml
@startuml

title: Structural Pattern - Proxy

interface Subject {
    +Request()
}

class RealSubject {
    +Request()
}

class Proxy {
    -RealSubject realSubject
    +Request()
}

Subject <|-- RealSubject
Subject <|-- Proxy
Proxy --> RealSubject

@enduml
```