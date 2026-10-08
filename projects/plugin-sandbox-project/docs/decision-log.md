# Decision Log

A condensed record of how the design evolved in the original conversation: what the user asked, what was decided, and what was rejected or corrected. Read this when you need the *why* behind something in `design.md`.

## Starting question

"How can I sandbox a process so it cannot access the network or files I select?" The user then clarified: Windows and Linux (macOS later), minimal latency, a plugin system for their own application, and third-party plugins that must be bound by rules the host sets.

## Decisions, in the order they were made

| # | Topic | Decision | Notes |
|---|---|---|---|
| 1 | Isolation model | Each plugin is its own sandboxed child process, kept alive between calls | Startup cost paid once, so no per-call latency. In-process sandboxing of native code doesn't work. |
| 2 | Windows sandbox | AppContainer (optionally LPAC) | Added in Windows 8 / Server 2012. LPAC (Windows 10+) drops the default "ALL APPLICATION PACKAGES" access and is stricter. |
| 3 | Launching on Windows | P/Invoke `CreateProcessW` with `STARTUPINFOEX` and `PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES` | `Process.Start` / `ProcessStartInfo` can't set the AppContainer attribute. See `reference/windows/`. |
| 4 | Linux sandbox | Landlock (filesystem, plus TCP on kernel 6.7+) + seccomp-bpf + `NO_NEW_PRIVS` | seccomp is the reliable way to deny all networking including UDP and Unix sockets. |
| 5 | Lifetime binding | Windows: job object with `KILL_ON_JOB_CLOSE`. Linux: `PR_SET_PDEATHSIG`. macOS: none, so channel-EOF watchdog | Kernel-enforced, so it fires on crash, `kill -9`, Task Manager and normal exit. |
| 6 | Kill semantics | Both mechanisms are outright kills with no cleanup | Graceful path is a shutdown message, ~2 s grace, then kill. Plugins must be killable at any instant. |
| 7 | "Reentrant?" | No. Plugins must be **idempotent and restartable** | Host owns committed state. Plugins stream checkpoints. |
| 8 | Locks | Don't share OS locks with plugins | Windows named mutexes become *abandoned*. POSIX named semaphores and non-robust pthread mutexes stay locked forever. |
| 9 | Bound vs Detached | Per-plugin policy. Detached plugins survive a host crash (e.g. telemetry collection) | Detached needs a well-known endpoint, state file (PID + **start time**), single-instance lock, auth token, orphan buffering and a max-orphan timeout. OS services are often a better home. |
| 10 | Watchdog / restart | Supervisor per plugin: exit or missed heartbeat, then restart with exponential backoff + jitter, crash-loop limit (5 in 60 s) | Hung plugins are killed and treated as crashes. |
| 11 | Start/stop control | Desired-state vs actual-state loop | Stop never triggers a restart. `StopAsync` completes only once the process is gone. |
| 12 | Cross-platform | `IPluginLauncher` per OS, everything else shared (~70-80%) | macOS has weaker guarantees (no pdeathsig, rlimits only, deprecated `sandbox_init`). |
| 13 | Communication | Hub and spoke: one channel per plugin, to the host only | Enforced structurally by the sandbox (no sockets or pipes to open), not just by convention. Host stamps `Source`. Default-deny policy. |
| 14 | Plugin language | Plugins can be **any language**, so the protocol is the contract | The .NET stub and `IPlugin` interface idea was dropped. SDKs are optional helpers. |
| 15 | Portability | No cross-platform runtime exists for every language | One package with an executable per platform. WASM (Wasmtime) is an optional extra entry. |
| 16 | Packaging | Fat package first (all platforms in one zip), split later if size matters | Signature + per-file hashes verified before extraction. Run only from host-owned read-only locations. |

## Corrections made along the way

These supersede earlier statements in the conversation. The reference code and `design.md` already reflect them.

1. **.NET-only plugin stub (superseded).** When plugins were assumed to be .NET, the plan was a shared plugin-host stub and an `IPlugin` contract package. This was abandoned once plugins became any-language. One lesson survived: **Landlock and seccomp apply per thread, and a managed runtime has already started threads**, so restrictions must be applied by a native shim *before* the runtime or plugin starts.
2. **Shared static job object (wrong).** The first job-object sketch used one static job with `ActiveProcessLimit = 1`, which would let only one plugin ever run. Fix: **one job per plugin**, created fresh at each launch.
3. **`bInheritHandles = false` (refined).** With stdio channels, the rule became "inherit **only** the channel handles" via `PROC_THREAD_ATTRIBUTE_HANDLE_LIST`.
4. **Seccomp `execve` / `clone` (refined).** An early version denied `execve` and `fork`/`clone`. For arbitrary languages: allow thread creation (`clone` with `CLONE_THREAD`), deny only process-creating `fork`/`vfork`/`clone`, and don't deny `execve` because the shim's own exec must succeed. Landlock's execute right limits what can run.
5. **Heartbeat semantics.** A heartbeat from a dedicated side thread can keep beating while the plugin's logic is deadlocked. The spec requires pings to be answered by the same loop that handles requests.
6. **Detached plugins and stdio.** Inherited stdio dies with the host, so Detached plugins can't use it. They listen on a named pipe or Unix socket instead, which means the seccomp filter must allow `socket(AF_UNIX)` for those plugins only.

## Performance notes (WASM)

Roughly 1.1-2x slower than native on compute-heavy code, near native for I/O-bound work. SIMD is limited to 128-bit. Host-call crossings cost tens to hundreds of ns, so batch messages. Epoch interruption (a few % overhead) is preferable to fuel metering (often 10-30%+). Precompile and cache modules. Go via `wasip1` is much heavier than Rust. Benchmark a real plugin both ways before committing. Wasmtime's .NET binding is the recommended host (Component Model support has historically lagged the Rust/C APIs, so verify its current state).

## Language notes

- **Rust and Go compile to native.** Go embeds its own runtime (scheduler, GC) in the binary. Prefer static builds on Linux (`musl` target for Rust, `CGO_ENABLED=0` for Go).
- **Go creates threads**, so seccomp must allow them.
- **Interpreted languages** (Python, Node, Java) should bundle their runtime into each platform folder so grants stay minimal.
- **macOS universal binaries** collapse x64 + arm64 into one artifact. Linux and Windows have no equivalent.

## Open questions (carried forward)

1. How strong must the macOS guarantee be?
2. Build WASM in v1, or after native packages are stable?
3. Detached children vs OS services for long-running telemetry plugins?
4. Fat packages vs per-platform packages with a registry?
5. Which SDK languages ship first?

## Suggested first tasks for Claude Code

- Scaffold the .NET 10 solution: `Host` (manager, supervisor, router, policy, package loader), `Protocol` (envelope + framing + IDL), `Launchers.Windows`, `Launchers.Unix`, and a `Conformance` test project.
- Turn `reference/shared/ManagedPlugin.cs` into compiled, unit-tested code (backoff, crash-loop, stop-during-backoff).
- Define the wire protocol (pick protobuf or JSON-RPC) and implement the .NET SDK first, then one more language.
- Build the Windows launcher from `reference/windows/` and verify with a test plugin that network and file escapes are denied.
