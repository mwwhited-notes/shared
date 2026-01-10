# Async versus parallel.

## Async Work

```plantuml
title Async Work

Alice -> Alice : Stuff envelope
activate Alice
Alice -> Bob: Request address 
deactivate Alice
activate Bob
Bob -> Bob: Lookup Address
Bob -> Jane: Addressed Envelope
activate Jane
Bob --> Alice: Let know Envelope Addressed
deactivate Bob
Jane -> Jane: Collect Envelopes
activate Jane
alt when box full
Jane -> Jane: Take to Post Office
deactivate Jane
Jane --> Alice: Let know Envelope Sent
deactivate Jane
end
```

## Parallel Work


```plantuml
title Parallel Work


(*) --> Send Mail
--> === Fork ===

partition Alice {
=== Fork === --> check for things to Stuff
--> stuff envelope
--> send to address
}


partition Bob {
=== Fork === --> check for things to Address
--> lookup address
--> Send to mail
}


partition Jane {
=== Fork === --> check for things to mail
--> mail packages
}

```