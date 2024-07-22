# Data Access Patterns

## Create, Read, Update, Delete (CRUD)

```plantuml
title: Data Access Pattern - Create, Read, Update, Delete (CRUD)

()User

[Create]
[Read]
[Update]
[Delete]

database "Data Store" as Storage

User --> Read : Get
User --> Create : Post
User --> Update : Put
User --> Delete : Delete

Read   --> Storage : Select
Create --> Storage : Insert
Update --> Storage : Update
Delete --> Storage : Delete
```

## Command Query Responsibility Segregation (CQRS)

```plantuml
title: Data Access Pattern - Command Query Responsibility Segregation (CQRS) 

()User
cloud "Front End"{
    [Read API] as Read
    [Write API] as Write
}
frame Services {
    database "Data Store" as Storage
    queue "Event Store" as Queue
}

User --> Read : Query
User --> Write : Command

Read --> Storage : Data Query
Write --> Queue : Store Command
Queue -> Storage : Handle Command
```