# F06 Validate public run and shape contracts early

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: S. Evidence: Reproduced and source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

RunSteps accepts negative counts, fractional counts and booleans. Shape checks in base process members are much weaker than those in IO validators. Invalid inputs can travel into actor loops or allocations.

## Proposed implementation

Centralize integer, shape and finite-value validation for public constructors. Reject bool where an integer count is intended; deliberately support NumPy integer scalars. Define zero-step execution as a documented no-op or reject it consistently after compatibility review. Validate before allocating resources or transmitting commands.

## Acceptance criteria

1. Negative, fractional, boolean and excessively large step counts have documented deterministic outcomes.
2. Shape tests cover scalar shape policy, empty dimensions, negative dimensions and NumPy integers.
3. Existing valid examples keep their output and execution timing.

## Compatibility and review challenge

Empty shapes and zero-sized arrays may be meaningful in current internals. Inventory their use before imposing a universal positive-dimension rule.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: C01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/core/run_conditions.py line 36](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/run_conditions.py#L36)
- [src/lava/magma/core/process/interfaces.py line 14](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/interfaces.py#L14)
