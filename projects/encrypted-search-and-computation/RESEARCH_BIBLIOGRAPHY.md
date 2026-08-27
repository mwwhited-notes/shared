# Research Bibliography — Encrypted Search & Computation

Papers, reference implementations, and further reading for
[OPE](ope-order-preserving-encryption.md), [ORE](ore-order-revealing-encryption.md),
[PHE](phe-partially-homomorphic-encryption.md), and [FHE](fhe-fully-homomorphic-encryption.md).

## Table of Contents

- [Standards Bodies & Ongoing Standardization](#standards-bodies--ongoing-standardization)
- [OPE / ORE](#ope--ore)
- [PHE](#phe)
- [FHE](#fhe)
- [Adjacent Techniques (Not Covered Here)](#adjacent-techniques-not-covered-here)
- [Libraries & Implementations](#libraries--implementations)

## Standards Bodies & Ongoing Standardization

Coverage is uneven across the four schemes — PHE has a finished ISO standard, FHE has one in
active draft plus a mature community standard, and OPE/ORE have neither.

**PHE — finished:**
- **[ISO/IEC 18033-6:2019](https://www.iso.org/standard/67740.html)** — *IT Security techniques —
  Encryption algorithms — Part 6: Homomorphic encryption.* Specifies Exponential ElGamal and
  Paillier encryption: parameter/key generation, encryption, decryption, and the homomorphic
  operation itself, plus object identifiers (Annex A) and numerical test vectors (Annex B). Part
  of the broader ISO/IEC 18033 encryption-algorithms family (Part 1: General, Part 2: Asymmetric
  ciphers, Part 3: Block ciphers, Part 4: Stream ciphers, Part 5: Identity-based ciphers, Part 6:
  Homomorphic encryption).
- Intel — [ISO-compliant Paillier Cryptosystem Library](https://www.intel.com/content/www/us/en/developer/articles/technical/homomorphic-encryption/iso-compliant-paillier-cryptosystem-library.html)
  — a real implementation built to the 18033-6 spec.

**FHE — active draft standard + governing community standard:**
- **[ISO/IEC 28033 series](https://www.iso.org/standard/87638.html)** (ISO/IEC JTC1/SC27/WG2) —
  *Information security — Fully homomorphic encryption*, multi-part:
  - [Part 1: General](https://www.iso.org/standard/87638.html) — foundational definitions,
    security models, hardness assumptions, message/ciphertext/key spaces. At **Draft
    International Standard (DIS)** status as of 2025.
  - [Part 5: Mechanisms for Scheme Switching](https://www.iso.org/standard/91022.html) — based on
    the Chimera framework for switching between FHE schemes. Still a **Working Draft (WD)**.
  - Background: [NIST presentation on the ISO/IEC FHE standardization effort](https://csrc.nist.gov/Presentations/2023/stppa6-iso-iec-fhe);
    [homomorphicencryption.org standards-list thread on the ISO/IEC path](https://groups.google.com/a/homomorphicencryption.org/g/standards/c/VyUu3-xFzTo).
- **[HomomorphicEncryption.org](https://homomorphicencryption.org/)** — open industry/government/
  academic consortium (IBM, Microsoft, Duality Technologies, MIT, Stanford, and others) running
  biannual standards meetings since 2017. Not a formal standards body itself, but its
  [Homomorphic Encryption Security Standard](https://homomorphicencryption.org/standard/)
  (published 2018, community security-guidelines update in 2024) is the de facto reference for FHE
  parameter security industry-wide, and — per NIST — has directly influenced ISO's drafting of the
  28033 series above. Companion whitepapers cover API and Applications.
  [eprint.iacr.org/2019/939](https://eprint.iacr.org/2019/939) is the archived Homomorphic
  Encryption Standard document itself.

**NIST — tracking / adjacent programs (no finished FHE standard yet):**
- [NIST Privacy-Enhancing Cryptography (PEC) program](https://csrc.nist.gov/projects/pec) —
  umbrella project covering FHE, Private Set Intersection (PSI), encrypted search, MPC, and ZKPs.
  Runs the [WPEC workshop series](https://csrc.nist.gov/Events/2026/wpec2026) (WPEC 2026: October
  26-29, virtual).
  See the [FHE-specific PEC page](https://csrc.nist.gov/projects/pec/fhe).
- [NIST Multi-Party Threshold Cryptography (MPTC) project](https://csrc.nist.gov/projects/threshold-cryptography)
  — an open call (**NIST IR 8214C**) for threshold schemes, explicitly scoped to include
  *threshold* FHE (i.e., splitting the FHE decryption key across parties) alongside threshold
  signatures and threshold PKE. Preview submissions were due 2026-08-07; not yet a finished
  standard.

**OPE/ORE — no standard, from any body:**
- Confirmed via direct search: neither OPE nor ORE has a NIST or ISO standard. They remain defined
  solely by their original academic papers (see [OPE / ORE](#ope--ore) below).
- The standardized *relative* worth knowing about is
  **[NIST SP 800-38G](https://csrc.nist.gov/publications/detail/sp/800-38g/rev-1/final)** —
  Format-Preserving Encryption (FPE), defining the FF1 and FF3-1 modes (the FFX construction,
  built on AES). FPE preserves ciphertext *format/length* (e.g., encrypt a 16-digit credit card
  number into another 16-digit string), not *order* — a genuinely different property from
  OPE/ORE, useful for legacy-schema compatibility rather than range queries, but commonly confused
  with OPE because both are "structure-preserving" encryption in a loose sense.

## OPE / ORE

**Foundational papers:**
- Boldyreva, Chenette, Lee, O'Neill — *Order-Preserving Symmetric Encryption* (EUROCRYPT 2009) —
  the BCLO scheme.
- Popa, Li, Zeldovich — *An Ideal-Security Protocol for Order-Preserving Encoding* (IEEE S&P 2013)
  — mOPE, as used in [CryptDB](https://css.csail.mit.edu/cryptdb/).
- Chenette, Lewi, Weis, Wu — *Practical Order-Revealing Encryption with Limited Leakage* (FSE
  2016) — [eprint.iacr.org/2015/1125](https://eprint.iacr.org/2015/1125),
  [Springer](https://link.springer.com/chapter/10.1007/978-3-662-52993-5_24).
- Lewi, Wu — *Order-Revealing Encryption: New Constructions, Applications, and Lower Bounds* (CCS
  2016) — [eprint.iacr.org/2016/612](https://eprint.iacr.org/2016/612).
- Cash, Liu, O'Neill, Zhandry — *Reducing the Leakage in Practical Order-Revealing Encryption*
  (2016) — [eprint.iacr.org/2016/661](https://eprint.iacr.org/2016/661).

**The attack that changed the field:**
- Naveed, Kamara, Wright — *Inference Attacks on Property-Preserving Encrypted Databases* (CCS
  2015) — [cs.brown.edu/people/seny/pubs/edb.pdf](https://cs.brown.edu/people/seny/pubs/edb.pdf),
  [ACM DL](https://dl.acm.org/doi/10.1145/2810103.2813651),
  [Microsoft Research summary](https://www.microsoft.com/en-us/research/publication/inference-attacks-property-preserving-encrypted-databases/).

**Later work:**
- Zhang — *Order-Revealing Encryption: New Constructions and Barriers* (PhD thesis, Rutgers) —
  [rucore.libraries.rutgers.edu](https://rucore.libraries.rutgers.edu/rutgers-lib/64844/PDF/1/play/).
- *Multi-Client Order-Revealing Encryption* —
  [arxiv.org/pdf/1809.01320](https://arxiv.org/pdf/1809.01320).
- *An Efficiently Searchable Encrypted Data Structure for Range Queries* —
  [arxiv.org/pdf/1709.09314](https://arxiv.org/pdf/1709.09314) — range queries without full ORE.

**Reference implementations:**
- [kevinlewi/fastore](https://github.com/kevinlewi/fastore) — Lewi's own ORE implementation.
- [pdroalves/ore_lewi-wu](https://github.com/pdroalves/ore_lewi-wu)
- [averykhoo/order-revealing-encryption](https://github.com/averykhoo/order-revealing-encryption)
  — Python.

## PHE

- Paillier — *Public-Key Cryptosystems Based on Composite Degree Residuosity Classes* (EUROCRYPT
  1999) — the additive PHE workhorse.
- Goldwasser, Micali — *Probabilistic Encryption* (1982) — semantic security + XOR-homomorphic
  scheme.
- ElGamal — *A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms* (1985)
  — multiplicative PHE; exponential ElGamal variant for additive use.
- OpenMined — [What is the Paillier cryptosystem?](https://openmined.org/blog/the-paillier-cryptosystem/)
  and [Private set intersection with the Paillier cryptosystem](https://blog.openmined.org/private-set-intersection-with-the-paillier-cryptosystem/)
  — accessible practitioner-level explainers.
- Wikipedia — [Private set intersection](https://en.wikipedia.org/wiki/Private_set_intersection)
  — overview and protocol survey.
- *PRIVATE SET INTERSECTION AND OTHER SET OPERATIONS IN THE THIRD PARTY SETTING* (2025) —
  [eprint.iacr.org/2025/1328](https://eprint.iacr.org/2025/1328).
- IEEE — *Use case of Paillier Homomorphic Algorithm for Electronic-Voting Systems* —
  [ieeexplore.ieee.org/document/9708030](https://ieeexplore.ieee.org/document/9708030/).
- *Survey on Remote Electronic Voting* — [arxiv.org/pdf/1702.02798](https://arxiv.org/pdf/1702.02798).
- *Advancement on Security Applications of Private Intersection Sum Protocol* —
  [arxiv.org/pdf/2308.14741](https://arxiv.org/pdf/2308.14741) — the contact-tracing-style PSI use
  case referenced in the PHE write-up.

## FHE

- Gentry — *Fully Homomorphic Encryption Using Ideal Lattices* (STOC 2009) — the original
  construction; Gentry's PhD thesis covers the same material in more depth.
- [fhe.org](https://fhe.org/resources/) — community resource hub (papers, talks, tooling) for the
  FHE research/practitioner community.
- Wavect — *Fully Homomorphic Encryption in 2026: What Ships and What Is Still Hype* —
  [wavect.io/blog/fully-homomorphic-encryption-practical-2026](https://wavect.io/blog/fully-homomorphic-encryption-practical-2026/)
  — source for the 2026 production-use examples (Apple Live Caller ID, Edge Password Monitor,
  Zama's Ethereum mainnet deployment).
- FHE Toolkit — *FHE 2026 Trends: Microsoft SEAL vs OpenFHE vs Concrete Benchmarks* —
  [fhetoolkit.com/fhe-2026-trends-seal-openfhe-concrete-benchmarks](https://fhetoolkit.com/fhe-2026-trends-seal-openfhe-concrete-benchmarks)
  — current-generation library comparison.
- ResearchGate — *A Review of Open-Source Fully Homomorphic Encryption Libraries: Zama.ai Concrete
  Compiler, Applications and Vulnerability* —
  [researchgate.net/publication/382305364](https://www.researchgate.net/publication/382305364_A_Review_of_Open-Source_Fully_Homomorphic_Encryption_Libraries_Zamaai_Concrete_Compiler_Applications_and_Vulnerability).

## Adjacent Techniques (Not Covered Here)

Flagged in the [README](README.md#overview) as out of scope for this pass but worth a follow-up
research project if a concrete use case points that direction:

- **Searchable Symmetric Encryption (SSE) / blind-index search** — keyword search over encrypted
  data (e.g., the pattern used by libraries like CipherSweet) rather than range/order queries;
  usually the better-secured answer when the actual need is "find records matching a keyword," not
  "sort/range-query a numeric column."
- **Secure Multi-Party Computation (MPC)** — multiple parties jointly compute a function over
  their private inputs without a single party ever holding all the data; different trust model
  than the single-server-computes-on-ciphertext model of PHE/FHE.
- **Differential Privacy** — protects aggregate statistics from revealing individual records;
  orthogonal to (and sometimes combined with) the encryption-based approaches here.

## Libraries & Implementations

| Library | Scheme(s) | Language | Notes |
|---------|-----------|----------|-------|
| [Microsoft SEAL](https://github.com/microsoft/SEAL) | BFV, CKKS | C++ | Mature, enterprise-oriented |
| [OpenFHE](https://github.com/openfheorg/openfhe-development) | BGV, BFV, CKKS, TFHE-style | C++ | Broadest single-API scheme coverage |
| [TFHE-rs](https://github.com/zama-ai/tfhe-rs) | TFHE | Rust | Zama |
| [Concrete](https://github.com/zama-ai/concrete) | TFHE (compiled) | Python→FHE via LLVM | Zama; compiles plain Python to FHE |
| [TFHE library](https://www.tfhe.com/) | TFHE | C/C++ | Original reference implementation |
| [fastore](https://github.com/kevinlewi/fastore) | ORE (Lewi-Wu) | — | Reference ORE implementation |

---

*Last updated: 2026-08-27*

