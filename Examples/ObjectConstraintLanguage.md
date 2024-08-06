# Object Constraint Language

## Summary

Object Constraint Language (OCL) is a formal language used to describe constraints, rules, and expressions on UML models and their objects. It provides a way to specify conditions that must hold true for the models and their elements, ensuring that the design adheres to certain business rules or requirements.

## Condition Types

- **Invariant**: constraints must always hold true.  No matter how data is altered or access this definition will result true.
- **Precondition**: condition or constraint that must be true before a specific operation (method) is executed. Precondition checks are used to ensure that the operation can be performed safely and correctly, given the current state of the object or system.
- **Postcondition**: a condition or constraint that must be true after a specific operation (method) has been executed. Postconditions specify the expected state of an object or system following the successful completion of an operation.

## Language Description

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

## Example

```ocl
context UserModel
inv: not string.isNullOrEmpty(self.name)
inv: self.age >= 0

-- Check if the user is eligible for registration
pre: self.age >= 18

-- After updating the user name, the new name must be different from the old name
post: self.name <> old(self.name)
```


## Notes and References

- https://modeling-languages.com/wp-content/uploads/2012/03/OCLChapter.pdf
- https://www.omg.org/spec/OCL/2.4/PDF
- https://st.inf.tu-dresden.de/files/general/OCLByExampleLecture.pdf
- https://www.omg.org/spec/OCL/2.4/About-OCL/
- https://www.cs.colostate.edu/~france/CS414/Lectures/Lectures2010/OCL2010.pdf