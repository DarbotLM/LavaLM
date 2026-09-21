# F20 Normalize delayed synapse validation

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: S. Evidence: Reproduced for sparse int32 and source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

DelaySparse rejects an int32 sparse delay matrix on this 64-bit environment because its validation compares dtype to int. Buffer capacity also needs an explicit relationship to supplied delays.

## Proposed implementation

Share a validation helper for scalar and array integer delays using integer-subtype checks. Reject bool, negative and out-of-range delays deliberately. Check shape compatibility and max_delay capacity before allocating buffers. Preserve sparse storage and define whether later updates can exceed initial capacity.

## Acceptance criteria

1. int32, int64 and NumPy integer scalars work where supported; equivalent dense and sparse inputs agree.
2. A max_delay below an actual delay fails at construction with a clear message.
3. Zero-delay, maximum-delay, recurrent and graded-spike golden outputs remain unchanged.

## Compatibility and review challenge

Delay zero represents the established buffered execution timing. Do not silently change it to same-timestep delivery.

## Dependencies and delivery

Dependencies: F06. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: P01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/proc/sparse/process.py line 283](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/sparse/process.py#L283)
- [src/lava/proc/dense/process.py line 266](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/dense/process.py#L266)
