# Presentation Patterns

## Model View Controller (MVC)

```plantuml
@startuml

title: Presentation Pattern - Model View Controller (MVC)

() User

[Model]
[View]
[Controller]

User <-> View

Model --> View : Updates
View -> Controller : Requests
Controller --> Model : Manipulates

@enduml
```

## Model View Presenter (MVP)

```plantuml
@startuml

title: Presentation Pattern - Model View Presenter (MVP)
() User

[View]
[Presenter]
[Model]

User <-> View

View --> Presenter : User Events
Presenter --> View : Updates

Presenter --> Model : Updates
Model --> Presenter : State Changes Events

@enduml
```

## Model View ViewModel (MVVM)

```plantuml
@startuml

title: Presentation Pattern - Model View ViewModel (MVVM)

() User

[View]
[View Model] as ViewModel
[Model]

User <-> View

ViewModel --> View : Binding
View --> ViewModel : Commands

ViewModel --> Model : Updates
Model --> ViewModel : State Change

@enduml
```

## Micro-frontends

Micro-frontends provide a means to loosely integrate a modular frontend application.  By using micro-frontends is is easier to manage application subsystems in though multiple teams as well as more easily manage a mixture of frontend technologies and framework versions.

```plantuml
@startuml

frame "Shell Application"

folder "Micro-Frontend A"
folder "Micro-Frontend B"
folder "Micro-Frontend C"

component "Service A"
component "Service B"
component "Service C"
component "Shared Library"

cloud "API Gateway"

node "Backend Service A"
node "Backend Service B"
node "Backend Service C"


[Shell Application] --> [Micro-Frontend A]
[Shell Application] --> [Micro-Frontend B]
[Shell Application] --> [Micro-Frontend C]

[Micro-Frontend A] --> [Service A]
[Micro-Frontend B] --> [Service B]
[Micro-Frontend C] --> [Service C]

[Micro-Frontend A] --> [Shared Library]
[Micro-Frontend B] --> [Shared Library]
[Micro-Frontend C] --> [Shared Library]

[Service A] --> [API Gateway]
[Service B] --> [API Gateway]
[Service C] --> [API Gateway]

[API Gateway] --> [Backend Service A]
[API Gateway] --> [Backend Service B]
[API Gateway] --> [Backend Service C]

[User] --> [Shell Application]

@enduml
```