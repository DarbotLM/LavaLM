# F31 Establish regression and performance evidence

## Maintenance batch status

Added focused regressions and explicit CPU/package/docs lanes. Full runtime confirmation and broader numerical/performance gates remain open.

Status: Partial. Priority: P1. Effort: M. Evidence: Observed test results and design improvement.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The audit run completed with 340 passed, 312 failed, 5 skipped and 4 teardown errors. The failures shared IPC startup restrictions and cleanup cascades; they do not demonstrate 312 independent product defects. Runtime success remains unverified here.

## Proposed implementation

Retain the audit diagnostics as failing-before/passing-after regressions for each small fix. Run the full CPU suite on an IPC-capable runner with fixed dependencies. Add fault-injection lifecycle cases and measured baselines for compile time, startup latency, steps per second, peak memory and retained resources. Store workload, hardware, dtype, seed and dependency metadata with every benchmark.

## Acceptance criteria

1. The reference CPU lane is green with all unexpected skips investigated.
2. Every confirmed fix has a narrow regression test that checks public behavior or a meaningful invariant.
3. Performance claims include baseline, modified result, variance and equivalent outputs; no pass/fail gate is based on an unmeasured target.

## Compatibility and review challenge

Do not lower coverage or delete failing tests to establish the baseline. Hardware and cross-platform evidence are separate gates.

## Dependencies and delivery

Dependencies: F04 F13. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [tests/lava/magma/runtime/test_exception_handling.py line 21](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/magma/runtime/test_exception_handling.py#L21)
- [tests/lava/magma/runtime/test_leakage.py line 27](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/magma/runtime/test_leakage.py#L27)
- [tests/lava/proc/dense/test_learning.py line 17](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/proc/dense/test_learning.py#L17)
