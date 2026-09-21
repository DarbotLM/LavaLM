# F11 Expose backend capabilities and discovery failures

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: L. Evidence: Source confirmed design improvement.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Optional imports use broad ImportError fallbacks and dummy classes in several modules. Model discovery imports neighboring modules and can suppress exceptions, making an absent backend hard to distinguish from a broken installed backend.

## Proposed implementation

Introduce a backend capability descriptor and explicit registration path while retaining legacy discovery as a compatibility adapter. Report missing optional packages separately from initialization errors. Include backend name, version, supported dtypes, synchronization protocol and process-model tags in selection diagnostics.

## Acceptance criteria

1. CPU-only installation works without hardware extensions.
2. A missing backend gives an actionable capability error; a broken installed backend preserves the original exception.
3. A third-party test backend registers without edits to compiler internals, and legacy models still resolve.

## Compatibility and review challenge

Do not execute arbitrary discovered plugins by default in an agent service. Plugin trust and installation remain host responsibilities.

## Dependencies and delivery

Dependencies: F01 F04. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/compiler/compiler_graphs.py line 28](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler_graphs.py#L28)
- [src/lava/magma/compiler/compiler_graphs.py line 880](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler_graphs.py#L880)
- [src/lava/magma/core/run_configs.py line 34](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/run_configs.py#L34)
