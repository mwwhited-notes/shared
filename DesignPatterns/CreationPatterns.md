# Creation Patterns

## Abstract Factory

Abstract factories are used to create difference related related objects without specifying their type.

```plantuml
@startuml

title: Create Pattern - Abstract Factory

interface AbstractFactory {
    AbstractProductA createProductA()
    AbstractProductB createProductB()
}

interface AbstractProductA {
    void doSomething()
}

interface AbstractProductB {
    void doSomething()
}

class ConcreteFactory1 implements AbstractFactory {
    AbstractProductA createProductA()
    AbstractProductB createProductB()
}

class ConcreteFactory2 implements AbstractFactory {
    AbstractProductA createProductA()
    AbstractProductB createProductB()
}

class ProductA1 implements AbstractProductA {
    void doSomething()
}

class ProductA2 implements AbstractProductA {
    void doSomething()
}

class ProductB1 implements AbstractProductB {
    void doSomething()
}

class ProductB2 implements AbstractProductB {
    void doSomething()
}

ConcreteFactory1 --> ProductA1: creates
ConcreteFactory1 --> ProductB1: creates
ConcreteFactory2 --> ProductA2: creates
ConcreteFactory2 --> ProductB2: creates

@enduml
```

## Builder

Builder is used to construct an object instance with control flow

```plantuml
@startuml

title: Create Pattern - Builder

interface Builder {
    Builder setPartA(String partA)
    Builder setPartB(String partB)
    Builder setPartC(String partC)
    Product build()
}

class ConcreteBuilder1 implements Builder {
    Product product = new Product()
    Builder setPartA(String partA)
    Builder setPartB(String partB)
    Builder setPartC(String partC)
    Product build()
}

class ConcreteBuilder2 implements Builder {
    Product product = new Product()
    Builder setPartA(String partA)
    Builder setPartB(String partB)
    Builder setPartC(String partC)
    Product build()
}

class Product {
    String partA
    String partB
    String partC
}

class Director {
    Builder builder
    void construct()
}

Director -> Builder: Uses
ConcreteBuilder1 --> Product: creates
ConcreteBuilder2 --> Product: creates

@enduml
```

## Dependency Injection

Dependency Injection is a means to control/provide dependent functionality to a class

```plantuml
@startuml

title: Create Pattern - Dependency Injection

interface Service {
    void execute()
}

class ConcreteServiceA implements Service {
    void execute()
}

class ConcreteServiceB implements Service {
    void execute()
}

class Client {
    private Service service
    void setService(Service service)
    void doSomething()
}

class Injector {
    Client inject(Service service)
}

Client --> Service: uses
Injector --> Client: injects
Injector --> Service: provides

@enduml
```

## Factory

Factories are used to create the particular type of class instance

```plantuml
@startuml

title: Create Pattern - Factory

interface Product {
    void use()
}

class ConcreteProductA implements Product {
    void use()
}

class ConcreteProductB implements Product {
    void use()
}

abstract class Creator {
    abstract Product factoryMethod()
}

class ConcreteCreatorA extends Creator {
    Product factoryMethod()
}

class ConcreteCreatorB extends Creator {
    Product factoryMethod()
}

ConcreteCreatorA --> ConcreteProductA: creates
ConcreteCreatorB --> ConcreteProductB: creates

@enduml
```

## Pool

Object pools provide a means to reuse object instances that are expensive to create.  Examples may include data service connection or threads.

```plantuml
@startuml

title: Create Pattern - Pool

interface Poolable {
    void initialize()
    void reset()
}

class ObjectPool {
    - pool: List<Poolable>
    + acquire(): Poolable
    + release(obj: Poolable): void
    + createObject(): Poolable
}

class ConcretePoolable implements Poolable {
    void initialize()
    void reset()
}

ObjectPool -> Poolable: manages
ObjectPool --> ConcretePoolable: creates
ObjectPool --> ConcretePoolable: reuses

@enduml
```

## Prototype

Prototypes create instances by copying an existing object

```plantuml
@startuml

title: Create Pattern - Prototype

interface Prototype {
    Prototype clone()
}

class ConcretePrototypeA implements Prototype {
    - fieldA: String
    + clone(): Prototype
}

class ConcretePrototypeB implements Prototype {
    - fieldB: int
    + clone(): Prototype
}

@enduml
```

## Lazy Initialization

Proxies or Lazy Initialized objects may be used for objects that are expensive to create.  The actual creation of the object is not called until the first time the object is required.

```plantuml
@startuml

title: Create Pattern - Lazy Initialization

class Client {
    - lazyObject: LazyObject
    + getLazyObject(): LazyObject
    + someMethod()
}

class LazyObject {
    + doWork()
}

Client --> LazyObject: uses

@enduml
```

## Registry (Multiton)

A registry allowed for storing/re-using a collect of named instances of an object.  

```plantuml
@startuml

title: Create Pattern - Registry

class Registry {
    - registry: Map<String, Object>
    + register(key: String, obj: Object): void
    + unregister(key: String): void
    + get(key: String): Object
}

class Client {
    - registry: Registry
    + useObject(key: String): void
}

Registry --> Client: provides

@enduml
```

## Singleton

Singletons are used to ensure only a single instance of an object is created in the lifetime of the application.

```plantuml
@startuml

title: Create Pattern - Singleton

class Singleton {
    - instance: Singleton
    - Singleton() // private constructor
    + getInstance(): Singleton
    + someMethod()
}

@enduml
```
