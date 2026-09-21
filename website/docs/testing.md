# Testing and evidence

## Reproduce the CPU environment

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/ci.txt -e .
python examples/cpu_smoke.py
python -m pytest tests --ignore=tests/lava/tutorials --cov-report=term-missing --cov-fail-under=65
```

The CI file pins principal runtime dependencies to the audit baseline and declares direct test dependencies. It is not a full transitive dependency lock. CPU CI exercises Linux and macOS with a job timeout; the inherited 65% coverage requirement remains enforced. Windows, optional hardware, and newer Python support are not claimed by those lanes.

## Bounded maintenance regressions

```bash
python -m pytest -o addopts='' tests/lava/test_foundations_regressions.py -q
```

These cases check nested/partial iteration, deep and wide flattening, context binding and exception propagation, read-only and failure-safe sparse queries, sparse identity construction, and checkpoint naming/type validation. Runtime context tests mock initialization and shutdown; they do not prove live actor teardown.

## Baseline versus post-change results

The audit revision was `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Its CPU suite, excluding tutorials, reported **340 passed, 312 failed, 5 skipped, and 4 teardown errors** in the review workspace. Captured child tracebacks showed socket creation denied during multiprocessing-manager startup. Failures clustered into startup EOFError and cleanup AttributeError. They are not evidence of 312 independent framework defects or a passing runtime baseline.

Hosted validation of implementation commit `d391cbdbaceb31204c3f31f8333992505c29ab5a` passed on Linux and macOS: **669 passed, 5 skipped, 72.68% coverage** on each platform. Details are recorded in the [implementation ledger](engineering/implementation.md) and the pull request's checks. Never rewrite the historical baseline as a post-fix result.

## Separate validation work

- Tutorials: 22 notebooks inventoried; execution needs a bounded timeout and explicit notebook dependencies. The previous broad unittest lane is replaced by an explicit CPU lane; notebook coverage is not silently claimed.
- Lint/security: owned CI runs Bandit and a critical Ruff rule set (`E9,F63,F7,F822,F823`). This replaces the inherited external setup; it does not claim full legacy style-rule parity. A broader lint/type baseline remains F02/F04 work: an exploratory F821 check found 30 inherited undefined-name reports, largely involving optional backend symbols and type annotations, which need individual review.
- Hardware: CPU simulation is not Loihi hardware conformance.
- Numerical behavior: fixed-point rounding, delays, overflow, learning traces, and reproducibility need separate matrices and reference outputs.

Package CI installs wheel and sdist independently and runs the CPU smoke example from outside the checkout, so local `src` imports cannot conceal packaging omissions. Documentation CI uses `npm ci` and a production build with broken-link failures enabled.
