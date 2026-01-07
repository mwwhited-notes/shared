# SideProject

## Summary

SideProject is a modeling/programming language.  The goal is to have simple to read documentation that is compiled into
a running application.  This will take self documented code to the next level.  Long pole ideas include the abilty to
reverse engineer existing applications in various (read as ANY) programming language into SideProject definition files.  
Then using the SideProject compiler the existing code will be transformed into a new application.

SideProject will be a highly opinionated language with the intention of having simple focused definitions that are easy
to read and write for a human and will be compiled into the platform of choice (.Net to start with.)

## What is a definition anyway?

A definition will be a simple text description of a single unit of functionality.

- Interface/contract
  - Definition of object
- Messages/records
  - Collection of named data element 
  - May have rules associated to define allowed Patterns
  - Immutable
  - May have metadata/attributes
  - Do not have methods
- Simple type
  - Collection of rules
  - No child elements
  - Immutable
  - Do not have methods
- Map/transform/projection
  - Converts data from on form to another
- Query
  - Allows composition and filtering of records
- Implementation/Provider
  - Particular construct of interface/contract
- User interface/interaction
  - List of fields
  - Field groups
    - List of fields
  - Fields may be editable or display only
  - Bindings are maps from and to messages.
  - List of commands
- Style is separate from layout
