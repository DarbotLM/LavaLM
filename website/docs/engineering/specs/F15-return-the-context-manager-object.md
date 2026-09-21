# F15 Return the context manager object

## Maintenance batch status

Process and Runtime context managers return self. Bounded tests verify binding, cleanup calls, and propagation of body exceptions. Live startup/shutdown still requires hosted runtime validation.

Status: Implemented; integration validation pending. Priority: P2. Effort: S. Evidence: Reproduced for Runtime and source confirmed for Process.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Runtime.__enter__ initializes but returns None; AbstractProcess.__enter__ also returns None. Existing context tests exercise cleanup without checking the as binding.

## Proposed implementation

Return self from both context manager entry methods after their existing entry behavior. Retain exception propagation and existing stop semantics. Handle startup failure through the lifecycle work rather than swallowing exceptions here.

## Acceptance criteria

1. with process as p binds the original process.
2. with runtime as r binds the initialized runtime.
3. A body exception is propagated and cleanup is invoked once logically, with repeated cleanup safe.

## Compatibility and review challenge

Small independent API repair; do not make it depend on a wholesale runtime rewrite.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: R02 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/runtime/runtime.py line 149](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/runtime.py#L149)
- [src/lava/magma/core/process/process.py line 227](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/process.py#L227)
