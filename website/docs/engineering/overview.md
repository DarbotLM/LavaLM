# Engineering review and specifications

The initial audit covered revision `646fa535764c3b0bd1bf24b956aaf64561bf97f6` on 21 September 2026. It inventoried **342 tracked files**, parsed **271 Python files** including **139 production modules**, and inspected cell sources in **22 notebooks**. Focused source review cited 49 files. This is complete inventory and structural coverage with selected deep review, not exhaustive semantic verification.

The review is grouped into 12 subsystem chapters in the sidebar. Each specification records the observed behavior, proposed change, acceptance criteria, compatibility risk, dependencies, and pinned source evidence. The [implementation ledger](implementation.md) records the smaller maintenance batch now applied.

## Priority and status

P0 means required before a first fork release, not an exploit severity. P1 is near-term correctness/reliability; P2 is bounded improvement or conformance; P3 is future architecture. S/M/L are planning ranges, not delivery promises. “Partial” means only the work described in that specification's maintenance note is implemented. “CPU CI verified” means the hosted CPU suite passed; it does not imply hardware or exhaustive numerical conformance.

| Specification | Priority | Effort | Implementation status |
|---|---|---|---|
| [F01 Establish the LavaLM distribution identity](specs/F01-establish-the-lavalm-distribution-identity.md) | P0 | S | Partial |
| [F02 Modernize dependencies in controlled stages](specs/F02-modernize-dependencies-in-controlled-stages.md) | P1 | M | Proposed |
| [F03 Repair release artifact and publishing workflows](specs/F03-repair-release-artifact-and-publishing-workflows.md) | P0 | M | Partial |
| [F04 Make CI self contained and define test lanes](specs/F04-make-ci-self-contained-and-define-test-lanes.md) | P1 | M | Partial |
| [F05 Stop adding root log handlers per process](specs/F05-stop-adding-root-log-handlers-per-process.md) | P1 | S | Proposed |
| [F06 Validate public run and shape contracts early](specs/F06-validate-public-run-and-shape-contracts-early.md) | P1 | S | Proposed |
| [F07 Make iteration and graph ownership explicit](specs/F07-make-iteration-and-graph-ownership-explicit.md) | P1 | M | Partial |
| [F08 Correct output port configuration lookup](specs/F08-correct-output-port-configuration-lookup.md) | P1 | S | Proposed |
| [F09 Bound graph traversal and compiler convergence](specs/F09-bound-graph-traversal-and-compiler-convergence.md) | P1 | M | Partial |
| [F10 Version and validate compiler caches](specs/F10-version-and-validate-compiler-caches.md) | P1 | M | Proposed |
| [F11 Expose backend capabilities and discovery failures](specs/F11-expose-backend-capabilities-and-discovery-failures.md) | P2 | L | Proposed |
| [F12 Use an explicit multiprocessing context](specs/F12-use-an-explicit-multiprocessing-context.md) | P1 | L | Proposed |
| [F13 Make runtime startup and cleanup transactional](specs/F13-make-runtime-startup-and-cleanup-transactional.md) | P1 | L | Proposed |
| [F14 Validate variable transactions and preserve data types](specs/F14-validate-variable-transactions-and-preserve-data-types.md) | P1 | M then L | Proposed |
| [F15 Return the context manager object](specs/F15-return-the-context-manager-object.md) | P2 | S | Implemented; CPU CI verified |
| [F16 Define channel cancellation and thread ownership](specs/F16-define-channel-cancellation-and-thread-ownership.md) | P1 | M | Proposed |
| [F17 Bound watchdog resource usage](specs/F17-bound-watchdog-resource-usage.md) | P2 | M | Proposed |
| [F18 Validate learning parameters and make seeds reproducible](specs/F18-validate-learning-parameters-and-make-seeds-reproducible.md) | P1 | M | Proposed |
| [F19 Specify learning expression and numeric conformance](specs/F19-specify-learning-expression-and-numeric-conformance.md) | P2 | M | Proposed |
| [F20 Normalize delayed synapse validation](specs/F20-normalize-delayed-synapse-validation.md) | P1 | S | Proposed |
| [F21 Resolve temporal convolution fixed point semantics](specs/F21-resolve-temporal-convolution-fixed-point-semantics.md) | P1 | M | Proposed |
| [F22 Keep S4D expansion matrices sparse](specs/F22-keep-s4d-expansion-matrices-sparse.md) | P2 | S then M | Proposed |
| [F23 Create a process model conformance matrix](specs/F23-create-a-process-model-conformance-matrix.md) | P2 | M | Proposed |
| [F24 Remove dense identity allocation from network composition](specs/F24-remove-dense-identity-allocation-from-network-composition.md) | P1 | S | Partial |
| [F25 Validate IO datasets and buffering contracts](specs/F25-validate-io-datasets-and-buffering-contracts.md) | P1 | S then M | Proposed |
| [F26 Make monitor probe limits explicit](specs/F26-make-monitor-probe-limits-explicit.md) | P2 | S then M | Proposed |
| [F27 Repair checkpoint paths and atomic persistence](specs/F27-repair-checkpoint-paths-and-atomic-persistence.md) | P1 | S then M | Partial |
| [F28 Make sparse queries nonmutating](specs/F28-make-sparse-queries-nonmutating.md) | P1 | S | Implemented; CPU CI verified |
| [F29 Make dataset download and storage explicit](specs/F29-make-dataset-download-and-storage-explicit.md) | P2 | M | Proposed |
| [F30 Make tutorials finite portable and reproducible](specs/F30-make-tutorials-finite-portable-and-reproducible.md) | P2 | M | Partial |
| [F31 Establish regression and performance evidence](specs/F31-establish-regression-and-performance-evidence.md) | P1 | M | Partial |
| [F32 Define the first neurosemantic vertical slice](specs/F32-define-the-first-neurosemantic-vertical-slice.md) | P3 | L for specification then staged experiments | Proposed |

## Evidence and review corrections

The baseline test environment could not create multiprocessing-manager sockets. Its 312 failures and four teardown errors must not be reported as hundreds of independent defects. See [testing](../testing.md).

Seventeen bounded diagnostics captured sixteen issue observations and one rejected hypothesis. The suspected flattened-roll error in ConvInTime was rejected; clearing the first column made the checked operation equivalent to rolling the time axis. Monitor explicitly documents one probe. Local trace RNG classes already use NumPy generators. These details constrain the fixes and prevent unnecessary changes.

Machine-readable evidence and the original reproduction script live in [`engineering/audit-2026-09-21`](https://github.com/DarbotLM/LavaLM/tree/main/engineering/audit-2026-09-21). Diagnostics describe the original revision and are not post-fix regression tests. Some are expected to stop reproducing after a fix.
