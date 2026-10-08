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
| `docs/design.md` | Full design document with inline PlantUML |
| `docs/decision-log.md` | Why each decision was made, what was corrected, open questions |
| `docs/diagrams/src/` | PlantUML sources (9 diagrams) |
| `docs/diagrams/svg/` | Rendered SVGs |
| `reference/windows/` | AppContainer launcher and per-plugin job object (uncompiled C# sketches) |
| `reference/shared/` | `ManagedPlugin` supervisor and `PluginManager` (uncompiled C# sketch) |

## Notes

- Nothing under `reference/` has been compiled or tested. Treat it as a starting point.
- Not included, because it was never written in the conversation: the Linux native shim (Landlock/seccomp), the macOS Seatbelt profile, the wire protocol/IDL, and the SDKs. They are the next build steps.
- Re-render diagrams: `java -jar plantuml.jar -tsvg -o ../svg docs/diagrams/src/*.puml` (requires Java and Graphviz).
