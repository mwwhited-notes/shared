# Application - User Management v2

## Summary

User/Person model is used to provide authentication and authorization for Application modules.

## Questions

* Should admins be able to add/remove their own group assignments
* Should groups management be scopeable to a single user/group of users?
* Should Rights always be inclusive or should there be a deny right as well?
* Should any admin be able to edit any user or do we need the ability to scope user management per application/module?
* Should we have dynamic membership evaluation for groups and their back references?
* Should we have group attributes?
* How to swap providers?
* How to import and manage existing accounts?

* Do we want the ability to have multiple instances of the application within the same database?


## Use Cases

```plantuml

left to right direction

actor User
actor Admin
actor Application

package "User Management" {
    usecase (Create New User) as createUser
    usecase (Unlink/Link Account to User) as linkAccount
    usecase (Enable/Disable User) as enableUser
    usecase (Request Password Reset) as passwordReset
}

package "Group Management" {
    usecase (Create/Delete Group) as createGroup    
    usecase (Add/Remove Group Member) as addGroupMember
    usecase (Add/Remove Group Permission) as addGroupPermission
    usecase (Add/Remove Group Children) as addGroupChild
}

package "Profile Management" {
    usecase (Add/Remove Contact Details) as createContact
    usecase (Add/Remove Person Attributes) as createAttributes
    usecase (Edit Person Details) as editPersonDetails
    usecase (Set/Clear System Person Attribute) as systemAttributes
}

Admin o-- User
Admin --> createUser
Admin --> enableUser
Admin --> createGroup
Admin --> addGroupMember
Admin --> addGroupChild
Admin --> addGroupPermission
Admin --> createAttributes

User --> linkAccount
User --> createContact
User --> createAttributes : "[!IsSystem]"
User --> editPersonDetails
User --> passwordReset

Application --> systemAttributes
Application --* Admin
Admin --* User

```

## Entity Design

```plantuml

package Security {

    entity User {
        IsActive : bool
    }
    entity Account {
        ProviderName : string
        ExternalReference : string
    }
    
    entity Permission {
        Name => $"{Application}-{Module}-{Right}"
    }
}

package Profile {

    entity Person {
        Prefix : string?
        FirstName : string?
        MiddleName : string?
        LastName : string
        Suffix : string?
        EmailAddress: string?
    }

    entity Attribute {
        Type : string
        Value : string
        IsSystem : bool
    }

    entity AttributeType {
        Name : string
        IsEditable : bool
        IsSystem : bool
        IsPII : bool
        AllowedCount : int
        ---
        DataPattern : string?
        DataType : string?
    }

    entity Group {
        Name : string
    }
}

package Platform { 
    entity Application {
        Name : string
    }
    entity Module {
        Name : string
    }
    entity Right {
        Name : string
    }
}

Account --> User : User

User --* Account : Accounts 
User --> Person : PersonInfo

Person --* Attribute : Attributes
Person --* Group : Groups

Attribute --* AttributeType : Attributes

AttributeType --> Module : Module

Group --* Person : Members
Group --> Group  : Parent
Group --* Group  : Child
Group --* Permission : Permissions
Group --* Attribute : Attributes

Permission --> Application : Application
Permission --> Module : Module
Permission --> Right : Right

Module *--* Application 

```
