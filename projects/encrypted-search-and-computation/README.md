# Encrypted Search & Computation (OPE / ORE / PHE / FHE)

A research survey of four cryptographic techniques that let you search or compute over data
*without decrypting it first* — Order-Preserving Encryption, Order-Revealing Encryption,
Partially Homomorphic Encryption, and Fully Homomorphic Encryption.

## Overview

These four techniques get grouped together because they all answer the same underlying
question — "can a server operate on my data while it stays encrypted?" — but they sit at very
different points on the leakage/power/performance spectrum:

- **OPE** and **ORE** ("property-preserving"/"property-revealing" encryption) trade *some*
  confidentiality (they deliberately leak order) for cheap **range/comparison queries** on an
  encrypted database column — the classic use case is `WHERE salary > 50000` without the DB
  server ever seeing plaintext salaries.
- **PHE** (Partially Homomorphic Encryption) supports exactly **one** algebraic operation
  (addition *or* multiplication) applied to ciphertexts an unlimited number of times, with no
  order or value leakage beyond the operation's result. Decades-old, fast, and already in
  production (e-voting tallies, private set intersection).
- **FHE** (Fully Homomorphic Encryption) supports **arbitrary computation** (both addition and
  multiplication, so any Boolean/arithmetic circuit) on ciphertexts, with strong lattice-based
  security. The 2009 Gentry breakthrough that made this possible at all; only became practical
  for narrow, real workloads in the last few years.

Not covered here (out of scope, different problem): searchable symmetric encryption (SSE) /
blind-index approaches (e.g., CipherSweet-style keyword search), secure multi-party computation
(MPC), and differential privacy — all solve adjacent "compute on private data" problems with
different tradeoffs and are worth a separate research pass if this project continues.

Each per-scheme doc now includes a **Pseudocode** section (illustrative, not implementation-ready
for OPE/ORE; a faithful textbook sketch for Paillier under PHE) and a **Protocol Flow** PlantUML
sequence diagram showing exactly what crosses the client/server boundary encrypted vs. what stays
local — the fastest way to see *why* each scheme's leakage/security story differs.

## Table of Contents

- [The Spectrum](#the-spectrum) — comparison matrix
- [Related Standards](#related-standards)
- [Order-Preserving Encryption (OPE)](ope-order-preserving-encryption.md)
- [Order-Revealing Encryption (ORE)](ore-order-revealing-encryption.md)
- [Partially Homomorphic Encryption (PHE)](phe-partially-homomorphic-encryption.md)
- [Fully Homomorphic Encryption (FHE)](fhe-fully-homomorphic-encryption.md)
- [Decision Guide](#decision-guide)
- [Research Bibliography](RESEARCH_BIBLIOGRAPHY.md)
- [Project Status](#project-status)

## The Spectrum

| | **OPE** | **ORE** | **PHE** | **FHE** |
|---|---|---|---|---|
| **Category** | Property-preserving encryption | Property-revealing encryption | Homomorphic encryption (single op) | Homomorphic encryption (arbitrary) |
| **What it reveals** | Full plaintext order — ciphertext byte order *is* plaintext order | Order, via a separate compare function rather than ciphertext structure (can hide value frequency) | Nothing beyond the result of the one supported operation | Nothing — arbitrary circuits evaluate without ever decrypting |
| **Operations supported** | Comparison only (`<`, `>`, `=`, range) | Comparison only | One operation (add **or** multiply), unlimited times | Arbitrary (add **and** multiply → any circuit) |
| **Performance** | Fast — near-native indexing/B-tree performance | Fast — ~55μs to encrypt a 32-bit int (Lewi-Wu), ~65x faster than contemporary OPE | Fast, practical today | Historically very slow; improving fast but still orders of magnitude slower than plaintext for general circuits |
| **Security model** | Weak by design — deliberately leaks order, which enables statistical inference attacks | Same fundamental leakage as OPE (order is inherently revealed) but a tighter, better-defined leakage profile than early OPE schemes | Strong — standard semantic security (IND-CPA) under classical hardness assumptions (RSA, DDH, composite residuosity) | Strong — lattice-based (LWE/RLWE), believed post-quantum resistant |
| **Maturity / adoption** | Largely deprecated for new designs after the [2015 inference attacks](RESEARCH_BIBLIOGRAPHY.md#ope--ore) broke CryptDB-style systems | Research-mature (2016-era constructions), limited production adoption | Mature, decades old, in production (e-voting tallies, private set intersection, contact tracing) | Practical **for narrow workloads** as of 2026 (private lookups, encrypted balances); general-purpose FHE still costly |
| **Standardization** | **None.** Academic/research constructions only — no NIST or ISO standard exists. | **None.** Same as OPE — research domain only. | **[ISO/IEC 18033-6:2019](RESEARCH_BIBLIOGRAPHY.md#standards-bodies--ongoing-standardization)** — Paillier and Exponential ElGamal are formally standardized. | **In progress**: [ISO/IEC 28033 series](RESEARCH_BIBLIOGRAPHY.md#standards-bodies--ongoing-standardization) (Part 1 General at Draft International Standard as of 2025), guided by the industry/academic [HomomorphicEncryption.org](https://homomorphicencryption.org/) community security standard; also tracked by NIST's Privacy-Enhancing Cryptography program. |

## Related Standards

Standardization coverage across these four techniques is uneven — see
[RESEARCH_BIBLIOGRAPHY.md § Standards Bodies & Ongoing Standardization](RESEARCH_BIBLIOGRAPHY.md#standards-bodies--ongoing-standardization)
for the full picture, but in short:

- **OPE/ORE** have no formal standard from any recognized body (NIST, ISO, IETF). They remain
  academic constructions defined only by their original papers. The closest *standardized*
  relative is [NIST SP 800-38G](RESEARCH_BIBLIOGRAPHY.md#standards-bodies--ongoing-standardization)
  (Format-Preserving Encryption, FF1/FF3-1) — but FPE preserves ciphertext *format/length*, not
  *order*, so it solves a different problem and isn't a substitute.
- **PHE** is standardized: **ISO/IEC 18033-6:2019** covers Paillier and Exponential ElGamal
  directly, specifying parameter/key generation, encryption/decryption, and the homomorphic
  operation itself.
- **FHE** standardization is active but not yet finished: the **HomomorphicEncryption.org**
  industry/government/academic consortium (IBM, Microsoft, Duality, MIT, Stanford, and others)
  has published community security guidelines since 2018 (updated 2024) that are the de facto
  reference for FHE parameter security today, and has directly fed into **ISO/IEC JTC1/SC27/WG2's**
  new **ISO/IEC 28033** multi-part standard (Part 1: General is at Draft International Standard
  status as of 2025; Part 5: Scheme Switching is still a Working Draft). Separately, **NIST's**
  Privacy-Enhancing Cryptography program tracks FHE alongside PSI/MPC/ZKP, and its Multi-Party
  Threshold Cryptography project (NIST IR 8214C) has an open call covering *threshold* FHE
  specifically.

## Decision Guide

```
START: What do you actually need to do to the encrypted data?

├─ Only need to compare/sort/range-query it (e.g. "salary BETWEEN X AND Y")?
│  └─ Consider ORE over OPE — same leakage class, better security profile, faster.
│     But first ask: could a blind index / bucketed range (SSE-style) avoid
│     leaking full order at all? That's usually the better-secured answer today.
│
├─ Only need ONE arithmetic operation, repeatedly, on many values?
│  (tallying votes, summing encrypted amounts, private-set-intersection matching)
│  └─ PHE. Cheapest, most mature, strongest security of the four. Pick the
│     scheme by the operation you need: Paillier (additive), RSA/ElGamal
│     (multiplicative).
│
├─ Need a mix of operations / an arbitrary function (ML inference, a real
│  query planner, general business logic) evaluated over encrypted inputs?
│  └─ FHE. Confirm the workload is narrow and latency-tolerant first — this
│     is still the most expensive option by a wide margin. Check whether an
│     approximate scheme (CKKS, for real-valued ML) or an exact scheme
│     (BFV/BGV, for integers; TFHE, for fast per-gate boolean ops) fits.
│
└─ Need strong confidentiality AND you control both ends (client encrypts,
   same client decrypts, server never needs to compute anything)?
   └─ None of these — just use standard authenticated encryption (AES-GCM).
      OPE/ORE/PHE/FHE only earn their cost when a third party must compute
      on the ciphertext without holding the key.
```

## Project Status

**Status:** Research documentation — no implementation planned yet.

**Next Steps:**
1. Read the four scheme write-ups and bibliography for a working mental model of the tradeoffs.
2. If a hands-on need materializes (e.g., a real range-query or PSI use case), scope a
   from-scratch prototype project the way [JWS/JWT From Scratch](../jws-jwt-from-scratch/) did —
   pick one scheme, implement the minimal primitive, and cross-check against a reference library
   (Paillier against a known test vector; a toy FHE circuit against Microsoft SEAL/OpenFHE output).
3. Revisit adjacent techniques called out above (SSE/blind-index search, MPC) if the search use
   case turns out to be closer to keyword search than range comparison — that's a different
   problem with better modern answers than OPE/ORE.

## References

See [RESEARCH_BIBLIOGRAPHY.md](RESEARCH_BIBLIOGRAPHY.md) for papers, libraries, and further
reading, organized by scheme.

---

*Last updated: 2026-08-27*
