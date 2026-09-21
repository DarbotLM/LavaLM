# 02 CI and release engineering

The workflows depend on lava-nc setup actions, upstream maintainers and package names. Release correctness is a prerequisite for publishing any fork artifact. Replace hidden setup dependencies with explicit, reproducible steps and test the built distribution from outside the checkout.

## Implementation specifications

- [F03 Repair release artifact and publishing workflows](../specs/F03-repair-release-artifact-and-publishing-workflows.md) — P0; M; Source confirmed.
- [F04 Make CI self contained and define test lanes](../specs/F04-make-ci-self-contained-and-define-test-lanes.md) — P1; M; Source confirmed.

## Coverage and boundaries

10 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `.github/CODEOWNERS` — inventory and content classification; focused review with cited finding.
- `.github/ISSUE_TEMPLATE.md` — inventory and content classification.
- `.github/ISSUE_TEMPLATE/bug_report.md` — inventory and content classification.
- `.github/ISSUE_TEMPLATE/config.yml` — inventory and content classification.
- `.github/ISSUE_TEMPLATE/feature_request.md` — inventory and content classification.
- `.github/PULL_REQUEST_TEMPLATE.md` — inventory and content classification.
- `.github/workflows/cd.yml` — inventory and content classification; focused review with cited finding.
- `.github/workflows/ci.yml` — inventory and content classification; focused review with cited finding.
- `.github/workflows/codacy_coverage_reporter.yml` — inventory and content classification.
- `.github/workflows/issues.yml` — inventory and content classification.
