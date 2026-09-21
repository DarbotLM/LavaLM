# F09 Bound graph traversal and compiler convergence

## Maintenance batch status

Nested-list flattening uses an iterative stack and is tested at width and depth 3,000. Traversal ordering, other recursive graph operations and compilation convergence remain open.

Status: Partial. Priority: P1. Effort: M. Evidence: Helper reproduced and source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The recursive flatten helper raises RecursionError for 2000 siblings. Connected-process discovery also uses recursion and set-based ordering; subcompiler convergence has no iteration limit.

## Proposed implementation

Replace deep recursive traversals with explicit stacks and identity-based visited sets while preserving a documented stable ordering. Avoid repeatedly concatenating accumulated lists. Add a configurable convergence limit with a diagnostic showing the changing subcompiler and channel entries. Retain cycle and hierarchical graph semantics.

## Acceptance criteria

1. Flat and deeply nested inputs above the Python recursion limit produce the expected flattened order.
2. Chain, star, recurrent and hierarchical process graphs compile deterministically across repeated runs.
3. An intentionally oscillating test subcompiler fails within the configured limit and reports useful context.

## Compatibility and review challenge

The audit reproduced the helper failure, not an end-to-end large-network compilation failure. Baseline compile-time and memory benchmarks are required before claiming speedups.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: K01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/compiler/compiler_graphs.py line 76](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler_graphs.py#L76)
- [src/lava/magma/compiler/compiler_graphs.py line 106](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler_graphs.py#L106)
- [src/lava/magma/compiler/compiler.py line 436](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler.py#L436)
