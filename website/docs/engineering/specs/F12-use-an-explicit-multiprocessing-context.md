# F12 Use an explicit multiprocessing context

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: L. Evidence: Reproduced.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Importing Runtime after the host selects spawn raises RuntimeError because a module import sets the global start method to fork. Dynamic async-model construction also has explicit Windows limitations, so removing one line alone does not establish spawn support.

## Proposed implementation

Pass a multiprocessing context through infrastructure construction and use it consistently for processes, pipes, queues, locks, semaphores, managers and watchdogs. Preserve an explicitly documented legacy fork option while adding spawn-compatible serializable builders and top-level actor entry points. The library must not change the application’s global context during import.

## Acceptance criteria

1. Import succeeds after a host selects spawn or forkserver and leaves that selection unchanged.
2. A minimal connected graph runs and stops under each advertised context.
3. No synchronization primitive created in one context is passed to actors from another; unsupported dynamic-model combinations fail before launch.

## Compatibility and review challenge

This is an integration change, not low-hanging one-line work. Validate on real Linux, macOS and Windows runners before advertising portability.

## Dependencies and delivery

Dependencies: F04 F13. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: R01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/runtime/message_infrastructure/multiprocessing.py line 47](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/message_infrastructure/multiprocessing.py#L47)
- [src/lava/magma/core/model/py/model.py line 687](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/model/py/model.py#L687)
