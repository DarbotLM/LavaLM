# F13 Make runtime startup and cleanup transactional

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: L. Evidence: Reproduced cleanup defect and source confirmed lifecycle risks.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Cleanup before SharedMemoryManager starts raises AttributeError. The broad test run showed this masking startup failures. Runtime initialization allocates several resources without an explicit unwind stack; receives and actor joins can wait indefinitely.

## Proposed implementation

Define CREATED, INITIALIZING, READY, RUNNING, PAUSED, STOPPING, STOPPED and FAILED states. Register cleanup immediately after each acquisition, unwind in reverse order and preserve the primary exception. Make stop and close idempotent. Add startup and shutdown deadlines with graceful stop first and bounded termination of owned actors only. Destructors must be best-effort and nonblocking.

## Acceptance criteria

1. Inject failure after each startup stage and verify owned actors, ports, shared-memory handles and watchdogs are released.
2. Stop before start, stop after failed start, repeated stop and exception exit all succeed without masking the original error.
3. An unresponsive child reaches a deterministic timeout result; healthy children still shut down gracefully.

## Compatibility and review challenge

Blindly terminating actors can corrupt in-flight state. Distinguish cancellation from successful completion and retain error context.

## Dependencies and delivery

Dependencies: F16. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: R05 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/runtime/runtime.py line 158](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/runtime.py#L158)
- [src/lava/magma/runtime/runtime.py line 485](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/runtime.py#L485)
- [src/lava/magma/runtime/message_infrastructure/shared_memory_manager.py line 20](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/message_infrastructure/shared_memory_manager.py#L20)
- [src/lava/magma/runtime/message_infrastructure/multiprocessing.py line 74](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/message_infrastructure/multiprocessing.py#L74)
