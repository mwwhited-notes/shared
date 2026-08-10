# Project Context Retention Protocol

**Purpose:** Make sure any project in `projects/` (or elsewhere in this notebook) can be
picked up cold — new machine, new session, months later — without re-deriving
decisions that were already made, and without a stale cross-reference pointing at a
file that no longer exists.

## Core Principle

**README.md is the default and usually sufficient context store** — per
[PROJECTS_PROTOCOL.md](PROJECTS_PROTOCOL.md), every project already gets a Project
Status section with Status and Next Steps. For most projects that's genuinely enough:
they're either finished, on hold with a clear next action, or simple enough that the
whole README re-establishes context in one read.

**This protocol exists for the projects where that's not quite enough** — multi-session
builds with several undecided technical choices, cross-repository dependencies, or
research findings that will go stale. Rather than reaching for a separate context file
by default, **first make the README's Project Status section do the job properly.**

## When to Use

Apply this protocol's checklist when a project has **any** of:
- Multiple genuinely open technical decisions (framework A vs. B, not yet chosen)
- Dependencies on another project or repository whose state could change
  independently (e.g. shared compute, a parallel research thread elsewhere in the
  notebook)
- Research findings with a shelf life — tool names, pricing, API availability — that
  a future reader shouldn't assume are still current without checking
- The user explicitly asks to "make sure context is retained" or "so this can resume
  on a different machine"

Most projects in `projects/` don't need this — a completed build, a simple reference
project, or a single-session note is already resumable via its plain README.

## Required Content for "Resumable" Status

When a project needs this, its **Project Status** section (not a new file, see below)
must answer all four of these, explicitly:

1. **What's actually built vs. only planned.** State it directly — "nothing built yet,
   no code, no accounts" is a real, useful sentence. Don't let a detailed Construction
   Method section imply progress that hasn't happened.
2. **Open decisions, listed by name.** Every unresolved "A vs. B" choice, as a bullet,
   not buried in prose — a future reader (or session) needs to see at a glance what's
   still undecided, not re-read the whole research section to find out.
3. **Anything with a shelf life, dated.** Tool comparisons, pricing, API terms — note
   the date the research was done so a much-later reader knows to re-verify rather
   than trust it blindly. (The project README template's own footer date covers the
   document as a whole; call out specific facts that are more perishable than the
   document itself when it matters.)
4. **Cross-references to anything that could drift independently.** A parallel
   research thread in another project's notes, a shared compute resource, a
   dependency on another project's decisions. Link to it and say what the open
   question is — don't assume the two threads will stay in sync on their own.

## Where This Content Lives

**Default: inside the project's own `README.md`, in Project Status.** See
`offline-mapping-system/README.md` for a worked example — it states "nothing built
yet" explicitly, lists open decisions as bullets, and cross-references a parallel
research thread found in a different repository.

**Escalate to a separate file only if the README would otherwise bloat past a
reasonable length** (same threshold logic as
[CLAUDE_MD_MAINTENANCE_PROTOCOL.md](CLAUDE_MD_MAINTENANCE_PROTOCOL.md) — a few hundred
lines is fine, four figures is not). In that case:
- A `build-log.md` (already a documented optional file in PROJECTS_PROTOCOL.md) is the
  right place for session-by-session progress notes once there's real build history.
- A project-specific `CLAUDE.md` is the *last* resort, not the first — it adds a
  second file that can silently go stale or get deleted without anyone updating what
  pointed to it (see the failure mode below, which is exactly what happened here).

**Do not create a project-specific `CLAUDE.md` reflexively just because a project
feels important.** Check whether the README's Project Status section, done properly,
already covers it first.

## Preventing Stale Cross-References (the concrete failure this protocol exists to stop)

`shared/CLAUDE.md` referenced `home-automation/CLAUDE.md` as an example of a
project-specific context file — **that file doesn't exist.** It was apparently removed
or never actually created, and the reference was never cleaned up. This is exactly the
failure mode this protocol is meant to prevent: a resumability pointer that's gone
stale and would send a future session chasing a file that isn't there.

**Rule: whenever a project-level context file is created, renamed, or removed, grep the
whole repository for references to its old path in the same edit** — at minimum check
`CLAUDE.md`, `.claude/protocols/README.md`, and `projects/README.md`. Don't leave a
dangling pointer for someone else to discover later.

```bash
# Before removing or renaming a project context file, check who points to it:
grep -rn "project-name/CLAUDE.md" --include="*.md" .
```

## Template — Project Status Section for a Context-Sensitive Project

```markdown
## Project Status

**Status:** Planning — **nothing built yet.** [State plainly what exists vs. doesn't —
code, accounts, data, running services.]

**Open decisions, not yet made — don't assume either default:**
- [Decision A] vs. [Decision B]
- [Unresolved parameter, e.g. a config value still a placeholder]
- Whether [this project] duplicates or extends [related thread elsewhere], not yet
  reconciled — see [cross-reference]

**Next Steps:**
1. ...
```

## Common Mistakes

- **Writing a detailed Construction Method and no state-of-the-build statement** — a
  future reader can't tell whether Phase 2 happened without an explicit callout.
- **Burying open decisions in prose** inside the Overview or Construction Method
  instead of listing them where Project Status is scanned.
- **Creating a project-specific `CLAUDE.md` by default** instead of trying the README
  approach first — adds a file that needs its own maintenance and its own
  cross-reference upkeep.
- **Not dating perishable research** — a tool comparison or pricing table with no date
  reads as current forever, even after it's stale.
- **Removing or renaming a context file without grepping for who references it.**

## Example

See [`offline-mapping-system/README.md`](../../projects/offline-mapping-system/README.md)'s
Project Status section — written directly against this protocol: explicit "nothing
built yet," a bulleted open-decisions list, and a cross-reference to a parallel,
not-yet-reconciled research thread in `Personal/Vans/DriftCampervans/change-tracking.md`.

---

*Protocol Version: 1.0*
*Created: 2026-08-10*
