# Original LavaLM audit evidence

Baseline: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`; reviewed 2026-09-21.

- `coverage.csv`: all 342 tracked paths, baseline hashes and review depth.
- `inventory-summary.json`: structural inventory counts.
- `audit-environment.txt`: dependency freeze used for the original audit.
- `reproductions.json`: 17 original bounded diagnostic observations.
- `reproduce_findings.py`: original diagnostic script; some failure observations should change after fixes. Run with `PYTHONPATH=src python engineering/audit-2026-09-21/reproduce_findings.py` from the repo root. It is evidence tooling, not the CI regression suite.
- `specifications.json`: original source evidence and proposals with maintenance implementation notes added.

CPU baseline: 340 passed, 312 failed, 5 skipped, 4 teardown errors. Worker socket PermissionError caused startup EOFError and cleanup AttributeError failures in the review environment. This is not a green runtime baseline or a count of independent product defects. Full transient baseline logs are not included here.

The wiki is the maintained prose entry point: `website/docs/engineering/overview.md`. Post-change tests are under `tests/lava/test_foundations_regressions.py`.
