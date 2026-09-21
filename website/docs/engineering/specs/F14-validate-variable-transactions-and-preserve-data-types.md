# F14 Validate variable transactions and preserve data types

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M then L. Evidence: Reproduced indexing defect and source confirmed transport limitation.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Array indexing raises an ambiguous-truth-value error after three SET header messages have already been sent; get(idx=0) returns the whole buffer. Management values are transported through float64, limiting exact representation of large integers and preventing a general typed state API.

## Proposed implementation

First replace truth-value checks with explicit None handling and validate index, value, shape and element count before sending any header. Specify whether set indices refer to source selection or destination selection and implement that contract at both ends. Then introduce a versioned typed payload or reject unsupported values before transfer. Keep legacy hardware transport behind a capability adapter.

## Acceptance criteria

1. None, zero, slices, tuples, boolean masks and integer-array indices follow the documented contract.
2. An invalid local request sends zero protocol messages and the next valid transaction succeeds.
3. Every advertised dtype round-trips exactly where required, including int64 values above 2**53; unsupported values fail clearly.

## Compatibility and review challenge

Fixing if idx alone cannot implement remote partial writes or change the wire format safely. Coordinate Runtime, RuntimeService and ProcessModel handlers.

## Dependencies and delivery

Dependencies: F13 F16. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: R03 R04 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/runtime/runtime.py line 516](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/runtime.py#L516)
- [src/lava/magma/runtime/runtime.py line 573](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/runtime/runtime.py#L573)
