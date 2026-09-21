# F08 Correct output port configuration lookup

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: S. Evidence: Reproduced with isolated compiler inputs.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The compiler uses the output port ordinal to index that port’s own connection configuration values. Two output ports with one configured connection each raise IndexError on the second port.

## Proposed implementation

Resolve configuration by the relevant port-to-peer relationship. If the initializer can carry only one config, accept one config or identical configs and explicitly reject conflicting fan-out configs until per-edge support is defined. Do not simply replace every index with zero and discard distinct configurations.

## Acceptance criteria

1. Two and three output ports with one config each compile successfully.
2. Reordering ports or connections cannot change which config is selected.
3. Fan-out with differing configs is either faithfully represented or rejected with a precise error.

## Compatibility and review challenge

Connection configuration also affects optional hardware routing. CPU regression tests do not establish hardware correctness.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: K02 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/compiler/subcompilers/py/pyproc_compiler.py line 218](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/subcompilers/py/pyproc_compiler.py#L218)
- [tests/lava/magma/runtime/test_connection_config.py line 62](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/magma/runtime/test_connection_config.py#L62)
