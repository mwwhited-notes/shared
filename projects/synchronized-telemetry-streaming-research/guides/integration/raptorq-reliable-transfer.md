# RaptorQ Reliable Transfer Integration Guide

## Overview
Use RaptorQ fountain codes for high-reliability data transfer over lossy networks (wireless, satellite, poor connections).

## When to Use RaptorQ
- Packet loss >5%
- Wireless/satellite links
- Cannot afford retransmission overhead
- Large file transfers over unreliable networks

## Architecture
```
Source Data
    ↓
RaptorQ Encoder (RFC 6330)
    ↓
Fountain Symbols (unlimited generation)
    ↓
Lossy Network (no ACKs needed)
    ↓
Receivers (any K+ symbols sufficient)
    ↓
RaptorQ Decoder → Original Data
```

## Implementation
- Code: `examples/dotnet/raptorq-transfer/`
- Symbol redundancy: 10-30% overhead
- Encoding O(K²): 245ms for 1MB
- Decoding O(K²): 312ms for 1MB

## Comparison
```
Loss Rate | Method | Efficiency
5%        | TCP retransmit | Low (many RTTs)
10%       | Reed-Solomon | Medium (slow)
20%+      | RaptorQ | High (no retransmit)
```

## Configuration
```csharp
var encoder = new RaptorQEncoder(data, symbolSize: 16);
var symbols = encoder.GenerateSymbols(K + redundancy);
```

## Diagrams

### Erasure-Coded Transfer Architecture

```plantuml
@startuml RaptorQ Erasure-Coded Transfer Architecture
skinparam backgroundColor #FEFEFE
skinparam defaultFontName Helvetica
skinparam defaultFontSize 10

title RaptorQ Fountain Code Transfer (RFC 6330)

package "Source Data" {
    database [File/Stream K source symbols] as source
}

package "Encoder (RFC 6330)" {
    component [Symbol Generator] as encoder
    component [FEC Parameters (K, N)] as fec_params
}

package "Transmission Network" {
    component [Network (Unreliable)] as network
    note "Packet Loss Rate: 0-30% Latency: Variable Out-of-order: Allowed" as net_note
}

package "Multiple Receivers" {
    component [Receiver 1] as rx1
    component [Receiver 2] as rx2
    component [Receiver 3] as rx3
}

package "Decoder (RFC 6330)" {
    component [Erasure Recovery] as decoder
    component [Constraint Solver] as solver
}

package "Output Data" {
    database [Reconstructed File/Stream] as output
}

' Main flow
source --> fec_params
source --> encoder
fec_params --> encoder

encoder --> network
network --> rx1
network --> rx2
network --> rx3

rx1 --> decoder
rx2 --> decoder
rx3 --> decoder

decoder --> solver
solver --> output

note right of encoder
  Fountain Code Properties:
  - Generates unlimited symbols
  - Any K symbols sufficient to recover
  - Linear operations over GF(2)
  - Computational complexity: O(K²)
end note

note right of fec_params
  FEC Configuration:
  - K: Source blocks
  - N_max: Max source symbols
  - Symbol size: 16-64 bytes
  - Repair percentage: 10-50%
end note

note right of network
  Benefits:
  - Loss agnostic (doesn't need ACK)
  - Parallel transmission safe
  - Out-of-order delivery OK
  - No retransmission overhead
end note

note right of decoder
  Recovery Process:
  1. Collect K+ symbols
  2. Solve system of equations
  3. Reconstruct source symbols
  4. Output original file

  Probability of success >99.9%
end note

@enduml
```

### Encoding/Decoding Sequence

```plantuml
@startuml RaptorQ Encoding Decoding Flow
skinparam backgroundColor #FEFEFE
skinparam defaultFontName Helvetica
skinparam defaultFontSize 10
skinparam sequenceArrowThickness 2

title RaptorQ Encoder Decoder Sequence (RFC 6330)

participant "Sender" as sender
participant "RaptorQ Encoder" as encoder
participant "Network (Lossy)" as network
participant "Receiver 1" as rx1
participant "Receiver 2" as rx2
participant "RaptorQ Decoder" as decoder

autonumber

sender -> encoder: ReadFile(K symbols)
note right of encoder
  Symbol Count = K
  Redundancy = 20%
  Repair Symbols = 0.2*K
end note

encoder -> encoder: GenerateSourceBlock

loop Generate Symbols
    encoder -> network: SendSymbol(ISI, payload)
end

note right of network
  Simulating 20% packet loss
  Packets arrive out-of-order
  Delay = variable
end note

network -> rx1: RecvSymbol(ISI=0)
network -> rx1: RecvSymbol(ISI=5)
network -> rx1: RecvSymbol(ISI=12)
network -> rx2: RecvSymbol(ISI=3)
network -> rx2: RecvSymbol(ISI=7)
network -> rx2: RecvSymbol(ISI=15)

rx1 -> decoder: AddSymbol(ISI=0, data)
rx1 -> decoder: AddSymbol(ISI=5, data)
rx1 -> decoder: AddSymbol(ISI=12, data)

rx2 -> decoder: AddSymbol(ISI=3, data)
rx2 -> decoder: AddSymbol(ISI=7, data)
rx2 -> decoder: AddSymbol(ISI=15, data)

decoder -> decoder: CheckIfDecoded()
note left of decoder
  Received 6 symbols
  Required K >= 5
  Ready to decode
end note

decoder -> decoder: SolveGaussianElimination

decoder -> decoder: RecoverSourceSymbols

decoder --> sender: WriteFile(K symbols)

note right of decoder
  Recovery complete
  From 6 received symbols
  Recovered all K source symbols
  With less than 20% overhead
end note

autonumber stop

@enduml
```

## References
- RFC 6330: RaptorQ Specification
- Code: `examples/dotnet/raptorq-transfer/`

---
Created: 2026-01-16
