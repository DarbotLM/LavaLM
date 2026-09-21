# F02 Modernize dependencies in controlled stages

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The interpreter constraint only permits Python 3.10 while classifiers list 3.8 and 3.9. Legacy dev tooling and a very broad lower bound for NetworkX obscure what is actually supported.

## Proposed implementation

First preserve a reproducible 3.10 baseline and align metadata. Declare runtime, test, documentation and optional backend dependencies separately. Pin the build tool in CI. Add newer interpreter/dependency combinations as explicit candidate jobs, then promote only passing combinations. Upgrade NumPy and NetworkX in separate changes after checking removed APIs and dtype behavior.

## Acceptance criteria

1. A fresh environment reproduces the documented dependency set without relying on globally installed packages.
2. Direct test imports such as psutil are declared in the test dependency group.
3. Each supported interpreter passes artifact installation, numerical tests and multiprocessing integration; unsupported versions fail installation clearly.

## Compatibility and review challenge

Do not widen the Python constraint or replace numerical dependencies solely because imports work. The audit used a compatible selected dependency set, not a full poetry.lock recreation.

## Dependencies and delivery

Dependencies: F04 F12 F31. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [pyproject.toml line 49](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/pyproject.toml#L49)
- [pyproject.toml line 53](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/pyproject.toml#L53)
- [pyproject.toml line 75](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/pyproject.toml#L75)
