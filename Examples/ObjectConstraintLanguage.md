# Object Constraint Language

## Summary

Object Constraint Language (OCL) is a formal language used to describe constraints, rules, and expressions on UML models and their objects. It provides a way to specify conditions that must hold true for the models and their elements, ensuring that the design adheres to certain business rules or requirements.

## Condition Types

- **Invariant**: constraints must always hold true.  No matter how data is altered or access this definition will result true.
- **Precondition**: condition or constraint that must be true before a specific operation (method) is executed. Precondition checks are used to ensure that the operation can be performed safely and correctly, given the current state of the object or system.
- - **Postcondition**: a condition or constraint that must be true after a specific operation (method) has been executed. Postconditions specify the expected state of an object or system following the successful completion of an operation.



## Example

```ocl
-- Object Constraint Language (OCL) is used to describe data models and classes 
context UserModel
inv: !string.IsNullOrEmpty(self.name)
inv: self.age >= 0

```

```ebnf
OCL           ::= Expression

Expression    ::= Invariant | Precondition | Postcondition | Query

Invariant     ::= "context" ClassName "inv:" Condition
Precondition  ::= "context" ClassName "::" OperationName "pre:" Condition
Postcondition ::= "context" ClassName "::" OperationName "post:" Condition
Query         ::= "context" ClassName "::" OperationName "result:" Expression

Condition     ::= BooleanExpression
BooleanExpression ::= "true" | "false" | LogicalExpression
LogicalExpression ::= Relation | LogicalExpression "and" LogicalExpression | LogicalExpression "or" LogicalExpression | "not" LogicalExpression
Relation      ::= ArithmeticExpression ComparisonOperator ArithmeticExpression
ArithmeticExpression ::= Number | Identifier | "(" ArithmeticExpression ")"
ComparisonOperator ::= "=" | "<>" | "<" | ">" | "<=" | ">="
Number        ::= Digit | Digit Number
Identifier    ::= Letter (Letter | Digit)*
Letter        ::= "a" | "b" | ... | "z" | "A" | ... | "Z" | "_"
Digit         ::= "0" | "1" | ... | "9"

```