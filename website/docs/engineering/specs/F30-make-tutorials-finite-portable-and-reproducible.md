# F30 Make tutorials finite portable and reproducible

## Maintenance batch status

Added the Docusaurus wiki, architecture/API guides, all 32 specifications, audit chunks and module index. Notebook modernization remains open.

Status: Partial. Priority: P2. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Tutorial execution has an unlimited notebook timeout, relies on CPython test support, manipulates global working directory and Python path details, and uses a temporary-file pattern that needs cross-platform care. The inventory contains 22 notebooks.

## Proposed implementation

Use isolated working directories and kernels, finite per-cell and per-notebook timeouts, public namespace APIs and os.pathsep. Declare network/dataset/hardware requirements in notebook metadata. Maintain a fast CPU smoke notebook, a full scheduled tutorial lane and a generated API reference tied to the release.

## Acceptance criteria

1. A deliberately hanging cell is stopped with its notebook and cell identified.
2. The CPU smoke notebook runs from an installed wheel outside the checkout on advertised platforms.
3. All 22 notebooks have a recorded execution policy; hardware/network exclusions are visible rather than silent.

## Compatibility and review challenge

Notebook JSON and source cells were inventoried but not executed in this audit. Existing outputs are not fresh validation.

## Dependencies and delivery

Dependencies: F01 F04 F29. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [tests/lava/tutorials/test_tutorials.py line 117](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/tutorials/test_tutorials.py#L117)
- [tests/lava/tutorials/test_tutorials.py line 14](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/tutorials/test_tutorials.py#L14)
- [tests/lava/tutorials/test_tutorials.py line 110](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/tutorials/test_tutorials.py#L110)
