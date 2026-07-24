# JWS/JWT From Scratch

Understand JSON Web Signature (RFC 7515) by implementing the signing/verification primitives
directly, rather than only calling a library like `System.IdentityModel.Tokens.Jwt`.

## Overview

Most .NET tutorials on JWT authentication — including the
[C# Corner ASP.NET JWS/HMAC walkthrough](https://www.c-sharpcorner.com/article/how-to-use-jwshmac-in-asp-net-web-application)
that prompted this — stop at "add the NuGet package, call `GenerateToken()`." That's the right
call for production auth, but it skips the actual cryptographic mechanics: base64url-encoding the
header and payload, forming the signing input, computing an HMAC-SHA256 (or RSA/ECDSA) signature
over it, and verifying that signature on the receiving end.

**Goal:** build a minimal JWS implementation from the RFC 7515 spec, then compare it against
`System.IdentityModel.Tokens.Jwt`'s output for the same header/payload/key to confirm it's
byte-for-byte compatible — proof the from-scratch version is actually correct, not just plausible.

## Background — What JWS Is

Per [RFC 7515 / Wikipedia](https://en.wikipedia.org/wiki/JSON_Web_Signature): JWS is an
IETF-standard format for signing arbitrary data (not necessarily a JWT claims set — JWS is the
general signing mechanism; JWT is one specific application of it as a claims container). Structure:

```
base64url(header) . base64url(payload) . base64url(signature)
```

Where `signature = HMAC-SHA256(secret, base64url(header) + "." + base64url(payload))` for the
HS256 algorithm (the simplest case — RSA/ECDSA variants sign the same input differently).

Part of the broader JOSE family alongside JWE (JSON Web Encryption, for confidentiality — JWS only
guarantees integrity/authenticity, not secrecy of the payload contents, which are just base64url,
not encrypted).

## Materials

Software-only project — no hardware required.

| Component | Purpose |
|-----------|---------|
| .NET (any recent version) | Implementation language |
| `System.Security.Cryptography.HMACSHA256` | The only crypto primitive actually needed for HS256 |
| `System.IdentityModel.Tokens.Jwt` (reference only, not used in the from-scratch implementation) | Cross-check that output matches a known-good library |

## Construction Method / Build Steps

1. Implement base64url encode/decode (standard base64 with `+`→`-`, `/`→`_`, no padding) — this
   trips people up if skipped
2. Build the JSON header (`{"alg":"HS256","typ":"JWT"}`) and a sample payload, encode both
3. Concatenate `encodedHeader + "." + encodedPayload` as the signing input
4. Compute `HMACSHA256` over that signing input with a secret key, base64url-encode the result
5. Assemble the final token: `header.payload.signature`
6. Generate the same token via `System.IdentityModel.Tokens.Jwt` with an identical header/payload/
   key and diff the two outputs — should match exactly
7. Implement verification: recompute the signature from the received header+payload and compare
   (constant-time comparison — this is where naive implementations introduce timing side-channels)
8. Optional stretch: add RS256 (RSA) signing as a second algorithm once HS256 round-trips correctly

## Key Features

- No black-box crypto — every step from RFC 7515 is implemented and understood
- Verified against a real library's output, not just "looks right"
- Demonstrates the actual attack surface JWT libraries protect against (timing attacks on
  signature comparison, algorithm-confusion attacks if `alg` isn't pinned server-side)

## Use Cases

- Foundational understanding before touching JWT-based auth in any real project
- Reference for anyone debugging "why doesn't my JWT verify" issues at the encoding/signing level
  instead of guessing at library configuration

## Project Status

**Status:** Planning

**Next Steps:**
1. Implement base64url encode/decode and unit test against known RFC 7515 test vectors
2. Implement HS256 sign + verify, cross-check against `System.IdentityModel.Tokens.Jwt` output
3. Write up the "why constant-time comparison matters" note once verification is implemented
4. Decide whether to stop at HS256 or extend to RS256

## References

- [JSON Web Signature - Wikipedia / RFC 7515 overview](https://en.wikipedia.org/wiki/JSON_Web_Signature)
- [How to use JWS/HMAC in an ASP.NET Web Application - C# Corner](https://www.c-sharpcorner.com/article/how-to-use-jwshmac-in-asp-net-web-application) (the production-library approach this project builds understanding underneath)
- [RFC 7515: JSON Web Signature (JWS)](https://www.rfc-editor.org/rfc/rfc7515) - primary spec

---

*Last updated: 2026-07-24*
