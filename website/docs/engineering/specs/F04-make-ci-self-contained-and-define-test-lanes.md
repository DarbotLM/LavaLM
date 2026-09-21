# F04 Make CI self contained and define test lanes

## Maintenance batch status

Added owned Linux/macOS CPU jobs, explicit principal dependency pins, smoke execution and the 65% coverage gate. Owned critical Ruff checks and Bandit are included; notebook, broader lint/type baselines, and broader platform lanes remain open.

Status: Partial. Priority: P1. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Setup is delegated to an upstream action and the suite mixes different execution requirements. A runtime startup failure creates a large cascade of failures and cleanup errors, making the result hard to interpret.

## Proposed implementation

Use explicit interpreter and dependency setup owned by this repository. Create pure-unit, CPU-runtime, notebook and optional-hardware lanes. Add a startup preflight for multiprocessing/shared memory with a clear diagnostic, finite job timeouts and retained failure logs. Make test and coverage commands explicit; preserve the existing coverage threshold until a measured baseline supports changing it.

## Acceptance criteria

1. A clean clone can run each lane using the same documented command locally and in CI.
2. A machine without the required IPC capability gets a clear integration preflight result; required CI does not silently skip it.
3. Coverage is attributable to the tested commit; required test failures fail the job.

## Compatibility and review challenge

Do not label all existing tests slow or optional to obtain a green build. macOS and Windows support require actual runner evidence. Bootstrap this lane on the current 3.10 baseline before F02 modernization.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [.github/workflows/ci.yml line 24](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/.github/workflows/ci.yml#L24)
- [pyproject.toml line 134](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/pyproject.toml#L134)
- [tests/lava/magma/runtime/test_leakage.py line 9](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/tests/lava/magma/runtime/test_leakage.py#L9)
