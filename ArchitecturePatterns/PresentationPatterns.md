# Presentation Patterns

## Model View Controller (MVC)

```plantuml
title: Presentation Pattern - Model View Controller (MVC)

() User

[Model]
[View]
[Controller]

User <-> View

Model --> View : Updates
View -> Controller : Requests
Controller --> Model : Manipulates

```

## Model View Presenter (MVP)

```plantuml
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

```

## Model View ViewModel (MVVM)

```plantuml
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

```