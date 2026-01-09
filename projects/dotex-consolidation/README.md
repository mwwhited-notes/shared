# dotex Consolidation Project

**Status**: Planning

Consolidate all .NET extension libraries and utilities into the single dotex framework repository.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Software Architecture / Library Consolidation |
| Status | Planning |
| Start Date | 2026-01-08 |
| Purpose | **Unify scattered .NET utilities into cohesive framework** |
| Target Repository | [dotex](https://github.com/OutOfBandDevelopment/dotex) |

## Problem Statement

Currently, .NET utilities and extensions are scattered across multiple standalone repositories. This creates:
- **Fragmented dependency management** - each library independently versioned
- **Discovery challenges** - users don't know what utilities exist
- **Duplication risk** - similar functionality in different repos
- **Maintenance overhead** - CI/CD for each repository
- **Resume dilution** - "Created 10 standalone tools" vs "Created 50+ module framework"

## Solution

Consolidate reusable .NET libraries into the dotex framework as modular packages following established patterns in `code/public/dotex`.

## dotex Framework Structure

The target framework organizes extensions by category:

| Category | Purpose | Example Modules |
|----------|---------|-----------------|
| **dotex.Build.*** | Build/MSBuild utilities | FirstOnce (orchestration) |
| **dotex.Data.*** | Data access/manipulation | TBD |
| **dotex.Decoders.*** | Binary/format decoders | BinaryDataDecoders (in progress) |
| **dotex.AI.*** | AI/ML integrations | TBD |
| **dotex.Messaging.*** | Message queues | TBD |
| **dotex.Testing.*** | Testing utilities | oobtainium (mocking) |
| **dotex.IO.*** | I/O abstractions | Device communication patterns |
| **dotex.Web.*** | Web utilities | TBD |
| **dotex.Documents.*** | Document processing | TBD |
| **dotex.Hosting.*** | Hosting/deployment | TBD |

## Migration Candidates

### High Priority (Active Migration)

| Project | Target Module | Status | NuGet Downloads |
|:--------|:-------------|:-------|:----------------|
| **BinaryDataDecoders** | dotex.Decoders.* | In Progress | 796K+ |
| **BuildFirstOnce** | dotex.Build.FirstOnce | Planned | TBD |
| **oobtainium** | dotex.Testing.Mocking | Planned | TBD |

### Medium Priority (Evaluation)

| Project | Possible Module | Notes |
|:--------|:----------------|:------|
| PrinterEmulator | dotex.IO.Devices | Extract IEEE-1284 protocol |
| DeviceBridge | dotex.IO.Legacy | Extract device communication patterns |

### Keep Standalone

| Project | Reason |
|:--------|:-------|
| EmbeddedBakery | Hardware/FPGA projects, different domain |
| RunScripts | Docker wrappers, different purpose |
| Samples | Example/demo code |

## Migration Process

For each candidate project:

1. **Analyze** - Extract reusable components
2. **Plan** - Map to dotex module structure
3. **Create** - Build module in dotex following standards
4. **Migrate** - Copy code with namespace updates
5. **Test** - Ensure all tests pass
6. **Document** - Add to dotex README and module docs
7. **Mark Original** - Add MIGRATED.md to source repo
8. **Publish** - NuGet package or shim for compatibility

See protocol: `.claude/protocols/DOTNET_CONSOLIDATION_PROTOCOL.md`

## Benefits

1. **Single Dependency** - One repo to clone, one dependency to manage
2. **Unified Versioning** - All modules versioned together
3. **Better Integration** - Modules work together seamlessly
4. **Easier Maintenance** - One CI/CD, one set of standards
5. **Improved Discoverability** - All extensions in one place
6. **Resume Impact** - "Created 50+ module framework" vs "Created 10 standalone tools"

## Standards Review

All migrations must follow patterns established in `code/public/dotex`:

### Project Structure
```
dotex/
├── src/
│   ├── [Category]/
│   │   ├── [Name]/
│   │   │   ├── [Name]/              # Main library
│   │   │   │   └── *.csproj
│   │   │   ├── [Name].Tests/        # Unit tests
│   │   │   │   └── *.csproj
│   │   │   └── [Name].Examples/     # Optional examples
│   │   │       └── *.csproj
```

### Project Configuration
- **Target Frameworks**: net8.0, net6.0, netstandard2.1
- **Package ID**: dotex.[Category].[Name]
- **Namespace**: OutOfBandDevelopment.Extensions.[Category].[Name]
- **Documentation**: XML documentation required
- **Package Generation**: GeneratePackageOnBuild=true

### Dependencies
- Common: Microsoft.Extensions.DependencyInjection.Abstractions
- Common: Microsoft.Extensions.Logging.Abstractions
- Keep dependencies minimal and compatible

## Tracking

| Metric | Target |
|--------|--------|
| Projects Migrated | 3+ (high priority) |
| dotex Modules | 50+ total (including new) |
| Test Coverage | Maintain existing coverage |
| Breaking Changes | Documented with migration guides |

## Current Status

**Phase**: Planning
- [x] Create consolidation protocol
- [x] Identify migration candidates
- [x] Document project in shared notes
- [ ] Review dotex patterns and standards
- [ ] Create detailed migration plan for BuildFirstOnce
- [ ] Create detailed migration plan for oobtainium
- [ ] Begin BinaryDataDecoders migration (in progress elsewhere)

## Related Files

**Protocols:**
- `.claude/protocols/DOTNET_CONSOLIDATION_PROTOCOL.md` - Complete migration workflow
- `.claude/protocols/SINGLE_REPOSITORY_ANALYSIS_PROTOCOL.md` - Repository analysis process
- `.claude/protocols/REPOSITORY_ACTION_ITEMS_PROTOCOL.md` - Actionable work items

**Analysis:**
- `repository-analysis-summary.md` - Quick triage results
- `.claude/analysis/` - Individual project analyses (to be created)

**Source Repository:**
- `code/public/dotex/` - Target framework location

## References

### Target Framework
- [dotex Repository](https://github.com/OutOfBandDevelopment/dotex)
- Analysis: [.claude/analysis/dotex/687bd7d-2025-08-01.md](../../../.claude/analysis/dotex/687bd7d-2025-08-01.md)
  - 109 .NET projects
  - .NET 9.0 target framework
  - Categories: Build, Data, Decoders, AI, Messaging, Testing, IO, Web, Documents, Hosting

### Migration Candidates
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - 796K+ downloads
  - Analysis: [.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md](../../../.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md)
  - 65 .NET projects, 342 C# files
  - Target: `dotex.Decoders.*`
- [BuildFirstOnce](https://github.com/OutOfBandDevelopment/BuildFirstOnce)
  - Analysis: [.claude/analysis/BuildFirstOnce/619fa7c-2025-02-14.md](../../../.claude/analysis/BuildFirstOnce/619fa7c-2025-02-14.md)
  - MSBuild orchestration tool
  - Target: `dotex.Build.FirstOnce`
- [oobtainium](https://github.com/OutOfBandDevelopment/oobtainium)
  - Analysis: [.claude/analysis/oobtainium/7869582-2025-02-14.md](../../../.claude/analysis/oobtainium/7869582-2025-02-14.md)
  - Mocking framework
  - Target: `dotex.Testing.Mocking`

---

*Last updated: 2026-01-08*
*Next review: After first migration completes*
