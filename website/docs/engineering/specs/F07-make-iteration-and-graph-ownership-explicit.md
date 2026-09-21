# F07 Make iteration and graph ownership explicit

## Maintenance batch status

Iteration now creates an independent membership snapshot. Direct next(collection) remains for compatibility. Registry lifetime/weak-reference work is deferred.

Status: Partial. Priority: P1. Effort: M. Evidence: Reproduced and source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Collection is its own iterator, so a fresh iteration after partial consumption resumes partway through. ProcessServer and VarServer retain strong references until a global reset; this is unsuitable as an implicit lifetime policy for repeated agent workloads.

## Proposed implementation

First return an independent iterator over a defined snapshot of collection members. Separately introduce explicit graph/session ownership with stable IDs and disposal. Audit callers before replacing global registries with weak references; compiled graphs must retain required objects. Avoid resetting shared registries while another graph is alive.

## Acceptance criteria

1. Repeated, nested and partially consumed iterations behave independently and terminate.
2. A repeated create-run-dispose workload reaches a stable retained-object count.
3. Disposing one session does not invalidate IDs or state in another session.

## Compatibility and review challenge

Iterator semantics are a small correction; registry ownership is a separate compatibility change. Do not combine them into one large patch.

## Dependencies and delivery

Dependencies: F13. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: C03 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/core/process/process.py line 639](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/process.py#L639)
- [src/lava/magma/core/process/process.py line 560](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/process.py#L560)
- [src/lava/magma/core/process/variable.py line 224](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/variable.py#L224)
