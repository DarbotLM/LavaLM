# F17 Bound watchdog resource usage

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The optional event monitor creates a thread for every event and retains each thread object until stop. Monitor shutdown joins all threads, including those waiting on events that may never complete.

## Proposed implementation

Track active operations in a bounded registry and poll deadlines from a small fixed worker set, or at minimum prune completed threads and add cancellation. Attach operation IDs so reuse of a shared event cannot confuse old and new operations. Emit structured warnings through the library logger with rate limiting.

## Acceptance criteria

1. A sustained completed-event workload has stable memory and thread counts.
2. Stop finishes within its deadline when an event never completes.
3. Each warning identifies the correct operation and diagnostics remain off by default without runtime overhead beyond the documented budget.

## Compatibility and review challenge

Measure overhead with watchdog enabled and disabled. Diagnostic facilities must not create a second deadlock path.

## Dependencies and delivery

Dependencies: F05 F16. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/compiler/channels/watchdog.py line 31](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/channels/watchdog.py#L31)
- [src/lava/magma/compiler/channels/watchdog.py line 43](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/channels/watchdog.py#L43)
