# F22 Keep S4D expansion matrices sparse

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: S then M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

S4D layer construction materializes a dense Kronecker expansion that is fed to Sparse processes. The conn_weights Var shape also describes the layer shape rather than the actual expansion matrix.

## Proposed implementation

Construct expansion/reduction maps directly with sparse eye/kron or CSR indices. Align the declared Var shape with its actual matrix, and clarify whether this connectivity belongs in immutable process parameters or a mutable Var. Validate d_states and coefficient broadcasting explicitly.

## Acceptance criteria

1. Small dense-reference and sparse implementations produce identical state/output sequences.
2. Construction storage scales with nonzero connections rather than the full expanded matrix area.
3. Coefficient shape errors and invalid d_states fail before compilation; alias access remains correct.

## Compatibility and review challenge

Changing conn_weights representation can affect serialization and model builders. Preserve a compatibility adapter for existing saved graphs.

## Dependencies and delivery

Dependencies: F20 F28. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/proc/s4d/process.py line 207](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/s4d/process.py#L207)
- [src/lava/proc/s4d/process.py line 238](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/s4d/process.py#L238)
- [src/lava/proc/s4d/models.py line 197](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/s4d/models.py#L197)
