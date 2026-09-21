# F28 Make sparse queries nonmutating

## Maintenance batch status

Explicit-zero queries work on a private copy. Tests cover read-only inputs, downstream exceptions, unsorted/duplicate storage and input preservation. Hosted Linux/macOS CPU suites, including sparse model tests, now pass.

Status: Implemented; CPU CI verified. Priority: P1. Effort: S. Evidence: Reproduced.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

find(explicit_zeros=True) temporarily replaces stored zeros with ones. It fails on read-only input, and an injected downstream failure leaves the original matrix modified.

## Proposed implementation

Read coordinates and values without mutating the caller. Use a copy-and-canonicalize strategy first if needed to preserve the existing ordering and duplicate-coordinate semantics; optimize to CSR index traversal only after those semantics are explicit. Preserve explicit zeros and document supported sparse formats.

## Acceptance criteria

1. Read-only CSR inputs work and original data/indices/indptr never change, including on exceptions.
2. Unsorted indices, duplicates, explicit zeros and empty rows produce the documented coordinates and values.
3. Tests verify callers such as sparse Var access and learning still receive the expected ordering.

## Compatibility and review challenge

A raw CSR traversal may expose duplicates that scipy.find previously coalesced. Nonmutation must not silently change this contract.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: U02 U03 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/utils/sparse.py line 26](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/sparse.py#L26)
