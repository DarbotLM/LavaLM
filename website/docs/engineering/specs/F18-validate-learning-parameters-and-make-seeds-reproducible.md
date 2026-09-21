# F18 Validate learning parameters and make seeds reproducible

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M. Evidence: Reproduced validation gap and source confirmed RNG behavior.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

A fractional learning epoch and NaN trace time constant are accepted. TraceRandom and ConnVarRandom already use local generators; the default learning-rule seed is drawn from NumPy’s global RNG.

## Proposed implementation

Require a positive integral epoch and finite nonnegative impulse/tau values, preserving the defined zero-tau behavior. Add an optional session seed policy that derives stable independent per-model streams and records generator state for resumption. Keep explicitly supplied historical seeds reproducible and document any new seed mode separately.

## Acceptance criteria

1. NaN, infinity, fractional epochs, bool epochs and invalid seeds fail at construction with parameter-specific messages.
2. Identical explicit seeds reproduce existing golden learning traces.
3. Parallel runs with a recorded session seed reproduce results across repeated executions within the declared backend/version contract.

## Compatibility and review challenge

Replacing RNG algorithms or draw order changes scientific outputs. Treat that as a versioned behavior change, not cleanup.

## Dependencies and delivery

Dependencies: F06 F31. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: L01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/core/learning/learning_rule.py line 565](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/learning_rule.py#L565)
- [src/lava/magma/core/learning/learning_rule.py line 126](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/learning_rule.py#L126)
- [src/lava/magma/core/learning/random.py line 19](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/random.py#L19)
