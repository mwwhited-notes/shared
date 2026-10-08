# Plugin Sandboxing Project (migrated design)

Design and reference code for a sandboxed, any-language plugin system for a .NET 10 host app, migrated from a claude.ai conversation.

## Using this in Claude Code

```bash
unzip plugin-sandbox-project.zip
cd plugin-sandbox-project
claude
```

Claude Code loads `CLAUDE.md` automatically, which summarizes the goals, settled decisions, corrections and open questions. A good first prompt:

> Read docs/design.md and docs/decision-log.md, then propose a solution layout for the .NET 10 host and start on step 1 of the build order.

## Contents

| Path | What it is |
|---|---|
| `CLAUDE.md` | Project memory for Claude Code: context, decisions, conventions |
| `docs/design.md` | Design index: section map, review status, reading paths |
| `docs/design/` | The design itself, in 12 topic files with inline PlantUML (sandbox, communication, lifecycle, permissions, brokered access, and so on) |
| `docs/decision-log.md` | Why each decision was made, what was corrected, open questions |
| `docs/use-cases.md` | Scenarios the design should serve, with status and open items (added 2026-10-08) |
| `docs/diagrams/src/` | PlantUML sources (12 diagrams; 10-12 are proposed additions) |
| `docs/diagrams/svg/` | Rendered SVGs (diagrams 1-9 only; 10-12 not yet rendered) |
| `reference/windows/` | AppContainer launcher and per-plugin job object (uncompiled C# sketches) |
| `reference/shared/` | `ManagedPlugin` supervisor and `PluginManager` (uncompiled C# sketch) |

## Review status (2026-10-08)

`docs/design.md` sections 10-13 (permissions and approval, brokered external access, network isolation, resource limits and abuse handling) were added after the original design as **proposals for review**. They are not settled decisions. See decisions 17-26 and open questions 6-15 in `docs/decision-log.md`, and `docs/use-cases.md` for the scenarios behind them.

## Notes

- Nothing under `reference/` has been compiled or tested. Treat it as a starting point.
- Not included, because it was never written in the conversation: the Linux native shim (Landlock/seccomp), the macOS Seatbelt profile, the wire protocol/IDL, and the SDKs. They are the next build steps.
- Re-render diagrams: `java -jar plantuml.jar -tsvg -o ../svg docs/diagrams/src/*.puml` (requires Java and Graphviz).
