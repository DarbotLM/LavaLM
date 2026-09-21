# Maintenance implementation ledger

This ledger describes the first LavaLM foundation patch relative to audit revision `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Source evidence in the individual specifications remains pinned to that unmodified baseline.

## Delivered scope

| Area | Applied change | Remaining work |
|---|---|---|
| Identity | `lavalm` distribution, owned support links, retained `lava.*` imports and licenses | Registry ownership, release version and namespace policy |
| Iteration | Independent snapshot iterators | Process/Var registry lifetime |
| Compiler | Iterative nested-list flattening | Deterministic traversal, convergence bounds, output-port configuration bug |
| Context managers | Process/Runtime bind self and call existing cleanup | Transactional initialization and bounded shutdown |
| Networks | CSR identities without dense intermediates | Broader composition contracts and performance benchmarks |
| Checkpoints | Consistent suffix fallback and member validation | Atomic writes, versioned portable format |
| Sparse queries | No mutation of caller storage | Live model/learning integration confirmation |
| Automation | Owned CPU/package checks, critical Ruff checks, Bandit, docs build and Pages workflow | Notebook lane, broader lint/type baseline, release governance |
| Documentation | Architecture, APIs, setup, migration, roadmap, all 32 specs and 12 review chunks | Update alongside subsequent implementation |

## Verification

The initial focused run passed **38 tests**, with two live-runtime cases deliberately deselected after a worker socket PermissionError reproduced the known environment restriction. The first test run also exposed an incorrect test assumption about SciPy's coordinate ordering; the regression was corrected to verify coordinate/value tuples while retaining implementation ordering.

`tests/lava/test_foundations_regressions.py` contains 17 maintenance regression cases (including parameterization). Runtime initialization is mocked only for context binding/cleanup-call tests. The sparse allocation cases construct 10,000-dimensional networks, reject `np.eye`, and verify CSR structure; they establish removal of a quadratic intermediate, not a measured end-to-end speedup.

An expanded affected-area run passed **58 tests**, skipped two optional cases, and deselected the same two live-runtime cases. A separate learning/process run passed 81 tests and hit the known socket restriction in 26 live learning tests. This is not a green integration result. Bandit 1.8.6 reported zero findings and zero analysis errors; the selected Ruff critical rules passed. Wheel and sdist builds succeeded, and both retain the applicable component license files.

The Docusaurus production build passed with broken-link and anchor errors enabled. Wheel and sdist each installed into a separate fresh Python 3.10 environment; imports and distribution metadata were verified outside the checkout. Live CPU smoke tests are delegated to hosted CI because of the local socket restriction. Hosted runtime checks are recorded in the pull request. CI is the gate for live CPU execution in an environment that allows worker sockets. Do not equate bounded test success with runtime or hardware conformance.

## Review decisions

- Preserve direct `next(collection)` for compatibility while ordinary iteration becomes independent.
- Keep the historical flatten helper name; expand only lists, preserving tuples as leaves.
- Keep checkpoint string inputs and exact legacy filename precedence; avoid a broad serialization redesign in this patch.
- Preserve SciPy sparse ordering/coalescing semantics through a private copy rather than introducing a new raw CSR traversal contract.
- Keep numerical dependencies and Python 3.10 stable; dependency modernization has its own specification.
- Remove inherited release credentials/targets and do not publish a package as part of maintenance validation.
