# Example Diagrams

## Activity Diagram

Activity diagrams are used to visualize the workflow of a process or the activities involved in a system. They illustrate the flow of control and data between activities, making them useful for modeling business processes and system functionalities.

Also know as `Process Map` under BPMN.

[reference](https://plantuml.com/activity-diagram-beta)

```plantuml
@startuml
start

:Browse Products;
:Select Product;

if (Product Available?) then (yes)
    :Add to Cart;
    :Proceed to Checkout;
    :Enter Shipping Information;
    :Enter Payment Information;

    if (Payment Successful?) then (yes)
        :Generate Order Confirmation;
        :Send Confirmation Email;
    else (no)
        :Notify Payment Failure;
    endif
else (no)
    :Notify Product Unavailability;
endif

stop
@enduml
```

## Class Diagram

Class diagrams are used to model the static structure of a system by depicting its classes, attributes, methods, and the relationships between the classes. They are an essential part of object-oriented design and help in understanding the organization and design of the software.

Also known as `Component Diagram` under C4-Model

[reference](https://plantuml.com/component-diagram)

```plantuml
@startuml
enum OrderStatus {
    Pending
    Shipped
    Delivered
    Canceled
}

abstract class User {
    +user_id: int
    +name: string
    +email: string
    +login()
    +logout()
}

class Customer extends User {
    +phone: string
    +register()
}

class Admin extends User {
    +manageUsers()
    +generateReports()
}

interface Payment {
    +processPayment(amount: float): boolean
}

class CreditCardPayment implements Payment {
    +cardNumber: string
    +expirationDate: string
    +processPayment(amount: float): boolean
}

class PayPalPayment implements Payment {
    +email: string
    +processPayment(amount: float): boolean
}

class Product {
    +product_id: int
    +name: string
    +description: string
    +price: float
    +checkAvailability()
}

class Order {
    +order_id: int
    +order_date: date
    +total_amount: float
    +status: OrderStatus
    +placeOrder()
}

class OrderItem {
    +order_item_id: int
    +quantity: int
}

Customer "1" -- "0..*" Order : places
Order "1" -- "1..*" OrderItem : contains
OrderItem "1" -- "1" Product : includes
Order "1" -- "1" Payment : uses
@enduml
```

## Collaboration Diagram

Collaboration diagrams (also known as communication diagrams) are used to show how objects interact in a particular scenario, emphasizing the relationships and messages exchanged between them. They focus on the structural organization of the system and how objects collaborate to fulfill a specific task.

Also known as `Choreography Diagram` under BPMN

[reference](https://plantuml.com/component-diagram)

```plantuml
@startuml
object Customer {
    +browseProducts()
    +addToCart()
    +checkout()
}

object WebApplication {
    +displayProducts()
    +processOrder()
}

object OrderService {
    +createOrder()
}

object PaymentGateway {
    +processPayment()
}

object EmailService {
    +sendConfirmationEmail()
}

Customer --> WebApplication : 1. browseProducts()
WebApplication --> Customer : 2. displayProducts()

Customer --> WebApplication : 3. addToCart()
Customer --> WebApplication : 4. checkout()
WebApplication --> OrderService : 5. createOrder()
OrderService -> PaymentGateway : 6. processPayment()
PaymentGateway -> OrderService : 7. paymentConfirmation()
OrderService --> WebApplication : 8. orderStatus()
WebApplication --> EmailService : 9. sendConfirmationEmail()
EmailService --> Customer : 10. confirmationEmail()
@enduml
```

## Component Diagram

Component diagrams are used to visualize the components of a system and their relationships, illustrating how they interact and depend on each other.

Also know as `Value Chain Diagram` under BPMN or `Container Diagram` under C4-Model.

[reference](https://plantuml.com/component-diagram)

```plantuml
@startuml
package "Online Shopping System" {
    [Web Application] as web_app
    [API Gateway] as api_gateway
    [User Service] as user_service
    [Product Service] as product_service
    [Order Service] as order_service
    [Database] as database

    web_app --> api_gateway : "HTTP Requests"
    api_gateway --> user_service : "User Requests"
    api_gateway --> product_service : "Product Requests"
    api_gateway --> order_service : "Order Requests"
    
    user_service --> database : "User Data"
    product_service --> database : "Product Data"
    order_service --> database : "Order Data"
}
@enduml
```

## Cross-Functional Flowchart

A cross-functional flowchart, also known as a swimlane diagram, is a type of flowchart that organizes the activities and processes of a system across different departments or functions within an organization. It visually distinguishes who does what in a process, making it easier to understand the roles and responsibilities of each function involved.

Also know as `Business Process Diagram` under BPMN.

[reference](https://plantuml.com/activity-diagram-beta)

```plantuml
@startuml
|#pink|Actor_For_red|
start
if (color?) is (red) then
#pink:**action red**;
:foo1;
else (not red)
|#lightgray|Actor_For_no_red|
#lightgray:**action not red**;
:foo2;
endif
|Next_Actor|
#lightblue:foo3;
:foo4;
|Final_Actor|
#palegreen:foo5;
stop
@enduml
```

## Data Flow Diagram (DFD)

Data Flow Diagram (DFD) are used to visualize the flow of data within a system, showing how data is processed, stored, and transmitted.

[reference](https://plantuml.com/activity-diagram-beta)

```plantuml
@startuml
start

:Receive Order;
:Check Product Availability;

if (Product Available?) then (yes)
    :Process Payment;
    :Update Inventory;
    :Generate Invoice;
    :Send Confirmation to Customer;
else (no)
    :Notify Customer about Unavailability;
endif

stop
@enduml
```

## Data Model - JSON

[reference](https://plantuml.com/json)

```plantuml
@startjson
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}
@endjson
```

## Data Model - Object

[reference](https://plantuml.com/object-diagram)

```plantuml
@startuml
object London
object Washington
object Berlin
object NewYork

map CapitalCity {
 UK *--> London
 USA *--> Washington
 Germany *--> Berlin
}

NewYork -> CapitalCity::USA
@enduml
```

## Data Model - YAML

[reference](https://plantuml.com/yaml)

```plantuml
@startyaml
doe: "a deer, a female deer"
ray: "a drop of golden sun"
pi: 3.14159
xmas: true
french-hens: 3
calling-birds: 
	- huey
	- dewey
	- louie
	- fred
xmas-fifth-day: 
	calling-birds: four
	french-hens: 3
	golden-rings: 5
	partridges: 
		count: 1
		location: "a pear tree"
	turtle-doves: two
@endyaml
```

## Deployment Diagram

Deployment diagrams are used to model the physical deployment of artifacts (software components) on nodes (hardware devices) in a system. They illustrate how software components are distributed across different hardware environments, showing the relationships between various components and the physical architecture of the system.

[reference](https://plantuml.com/deployment-diagram)

```plantuml
@startuml
node "Web Server" {
    component "Web Application" as webApp
}

node "Application Server" {
    component "Order Service" as orderService
    component "Payment Gateway" as paymentGateway
}

node "Database Server" {
    component "Customer Database" as customerDB
    component "Product Database" as productDB
}

node "Email Server" {
    component "Email Service" as emailService
}

webApp --> orderService : HTTP Request
orderService --> paymentGateway : Process Payment
orderService --> customerDB : Query Customer Data
orderService --> productDB : Query Product Data
orderService --> emailService : Send Confirmation Email
@enduml
```

## Entity Relation Diagram (ERD)

Entity Relation Diagram (ERD) are used to design/describe relational databases and data modeling.

[reference](https://plantuml.com/class-diagram)

```plantuml
@startuml
entity "Customer" {
    + customer_id : int <<PK>>
    + name : string
    + email : string
    + phone : string
}

entity "Order" {
    + order_id : int <<PK>>
    + order_date : date
    + total_amount : float
    + customer_id : int <<FK>>
}

entity "Product" {
    + product_id : int <<PK>>
    + name : string
    + description : string
    + price : float
}

entity "OrderItem" {
    + order_item_id : int <<PK>>
    + quantity : int
    + order_id : int <<FK>>
    + product_id : int <<FK>>
}

Customer ||--o{ Order : places
Order ||--o{ OrderItem : contains
Product ||--o{ OrderItem : includes
@enduml
```

## Gantt Chart

A Gantt chart is a visual project management tool that displays a project's schedule, illustrating the start and finish dates of various elements. It helps in planning, coordinating, and tracking specific tasks within a project.

[reference](https://plantuml.com/gantt-diagram)

```plantuml
@startgantt
[Task1] requires 4 days 
then [Task1.1] requires 4 days
[Task1.1] is 40% completed

[Task1.2] starts at [Task1]'s end and requires 7 days
[Task1.2] is 55% completed

[Task2] requires 5 days
then [Task2.1] requires 4 days
[Task2.1] is 35% completed

[MaxTaskEnd] happens at [Task1.1]'s end
[MaxTaskEnd] happens at [Task1.2]'s end
[MaxTaskEnd] happens at [Task2.1]'s end

@endgantt
```

## Mindmap

A mind map is a visual representation of information that organizes concepts, ideas, and tasks around a central topic. It utilizes a hierarchical structure to show relationships between different elements, making it easier to understand and analyze complex information.

[reference](https://plantuml.com/mindmap-diagram)

```plantuml
@startmindmap
+ OS
++_ Linux
+++ Ubuntu
++++ Linux Mint
++++ Kubuntu
++++ Lubuntu
++++ KDE Neon
+++ LMDE
+++ SolydXK
+++ SteamOS
+++ Raspbian
--_ Windows 9x
--- Windows 95
--- Windows 98
-- Windows NT
--- Windows 8
--- Windows 10
@endmindmap
```

## Network Diagram

Network diagrams are used to represent the layout and connections of a network, illustrating how different devices and components are interconnected. They provide a visual representation of the network's structure, showing how data flows between devices and the relationships between network elements.

[reference](https://plantuml.com/nwdiag)

```plantuml
@startuml
nwdiag {
  network Sample_front {
    address = "192.168.10.0/24";

    // define group
    group web {
      web01 [address = ".1"];
      web02 [address = ".2"];
    }
  }
  network Sample_back {
    address = "192.168.20.0/24";
    web01 [address = ".1"];
    web02 [address = ".2"];
    db01 [address = ".101"];
    db02 [address = ".102"];

    // define network using defined nodes
    group db {
      db01;
      db02;
    }
  }
}
@enduml
```

## Package Diagram

A package diagram is a type of UML diagram that organizes classes, interfaces, and other elements into groups called packages. It visually represents the structure of a system by showing how these packages are related to one another and how they depend on each other.

[reference](https://plantuml.com/class-diagram)

```plantuml
@startuml
package "Online Shopping System" {
    package "User Management" {
        class User
        class UserProfile
        class Authentication
    }

    package "Product Management" {
        class Product
        class Category
        class Inventory
    }

    package "Order Management" {
        class Order
        class Payment
        class Shipment
    }

    package "Notification" {
        class EmailService
        class SMSService
    }

    User --> Authentication : manages
    UserProfile --> User : contains
    Product --> Inventory : tracks
    Order --> Payment : processes
    Order --> Shipment : ships
    EmailService --> User : notifies
    SMSService --> User : alerts
}

@enduml
```

## Sequence Diagram

Sequence diagrams are used to model the interactions between objects or components in a system over time. They depict how messages are exchanged between participants and the order in which these interactions occur, providing a detailed view of the flow of control and data.

Also known as `Orchestration Diagram` or `Collaboration Diagram` under BPMN or `Code Diagram` under C4-Model.

[reference](https://plantuml.com/sequence-diagram)

```plantuml
@startuml
actor "Customer" as customer
participant "Web Application" as webApp
participant "Order Service" as orderService
participant "Payment Gateway" as paymentGateway
participant "Email Service" as emailService

customer -\ webApp : Browse Products

customer -\ webApp : Add to Cart

customer -> webApp : Proceed to Checkout
activate webApp
    webApp -> orderService : Create Order
    activate orderService
        orderService -> paymentGateway : Process Payment
        activate paymentGateway
        return Payment Confirmation
    return Order Status

    webApp -\ emailService : Send Confirmation Email
    deactivate webApp

    activate emailService
    emailService -\ customer : Confirmation Email
    deactivate emailService

@enduml
```

## State Diagram

State diagrams are used to model the dynamic behavior of an object by illustrating its states and the transitions between those states based on events. They help in understanding how an object reacts to different events throughout its lifecycle.

Also know as `Event-Driven Process Chain (EPC)` under BPMN.

[reference](https://plantuml.com/state-diagram)

```plantuml
@startuml
[*] --> Pending

Pending --> Shipped : Ship Order
Shipped --> Delivered : Deliver Order
Shipped --> Canceled : Cancel Order
Pending --> Canceled : Cancel Order
Delivered --> [*]
Canceled --> [*]
@enduml
```

## Timing Diagram

Timing diagrams are used to represent the timing of messages exchanged between objects over a specified period. They focus on the state changes of the system or components over time, illustrating how the timing of events affects the interactions.

```plantuml
@startuml
clock   "Clock_0"   as C0 with period 50
clock   "Clock_1"   as C1 with period 50 pulse 15 offset 10
binary  "Binary"  as B
concise "Concise" as C
robust  "Robust"  as R
analog  "Analog"  as A


@0
C is Idle
R is Idle
A is 0

@100
B is high
C is Waiting
R is Processing
A is 3

@300
R is Waiting
A is 1
@enduml
```

## Use Case Diagram

Use case diagrams are used to visualize the interactions between users (actors) and the system, capturing the functional requirements and depicting how users will interact with the system to achieve specific goals.

Also known as `Context Diagram` under C4-Model

[reference](https://plantuml.com/use-case-diagram)

```plantuml
@startuml
actor "Customer" as customer
actor "Admin" as admin

rectangle "Online Shopping System" {
    usecase "Browse Products" as UC1
    usecase "Add to Cart" as UC2
    usecase "Checkout" as UC3
    usecase "Process Order" as UC4
    usecase "Manage Inventory" as UC5

    customer --> UC1
    customer --> UC2
    customer --> UC3

    admin --> UC5
    UC3 --> UC4
}
@enduml
```

## Wireframe

Wireframes are visual representations of a user interface, showing the layout and structure of a webpage or application without detailed design elements. They help in planning the design and functionality of a product.

[reference](https://plantuml.com/salt)

```plantuml
@startsalt
{+
    {/ <b>General | Fullscreen | Behavior | Saving }
    {
        { Open image in: | ^Smart Mode^ }
        [X] Smooth images when zoomed
        [X] Confirm image deletion
        [ ] Show hidden images
    }
    [Close]
}
@endsalt
```

## Work Breakdown Structure (WBS)

A Work Breakdown Structure (WBS) is a hierarchical decomposition of a project into smaller, more manageable components. It helps in organizing the project into tasks and sub-tasks, making it easier to plan, execute, and monitor.

[reference](https://plantuml.com/wbs-diagram)

```plantuml
@startwbs
* Online Shopping Platform Project
** Project Initiation
*** Define Project Scope
*** Identify Stakeholders
*** Conduct Feasibility Study
** Design Phase
*** User Interface Design
**** Create Wireframes
**** Design Mockups
*** Database Design
**** Define Data Model
**** Create ER Diagram
** Development Phase
*** Frontend Development
**** Implement User Authentication
**** Create Product Pages
**** Implement Shopping Cart
*** Backend Development
**** Set Up Web Server
**** Implement Order Processing
**** Integrate Payment Gateway
** Testing Phase
*** Unit Testing
*** Integration Testing
*** User Acceptance Testing
** Deployment Phase
*** Prepare Deployment Environment
*** Deploy Application
*** Monitor Post-Deployment
** Project Closure
*** Document Lessons Learned
*** Release Project Resources
*** Conduct Project Review
@endwbs
```
