# Contributing

Start with a reproducible behavior and the relevant [engineering specification](engineering/overview.md). Preserve the `lava.*` public namespace, component notices, and numerical semantics unless a separately reviewed compatibility change requires otherwise.

## A reviewable change

1. Record the current behavior with a focused regression or measurement.
2. Implement the smallest coherent correction and update its specification status.
3. Run the affected tests and any relevant runtime or numerical lane.
4. Update the wiki in the same pull request, distinguishing measured results from expected benefits.
5. Explain remaining uncertainty: platform access, optional backends, numerical assumptions, and integration limits.

Small changes do not need a duplicate test of every assignment. Tests should protect observable contracts, exception behavior, shape/type boundaries, or meaningful performance properties. A sparse identity regression, for example, checks that construction never invokes a dense identity allocation.

## Working on documentation

In `website/`, run `npm ci`, `npm start`, and `npm run build`. Navigation is defined in `sidebars.js`; Markdown pages live in `docs/`. Each specification records baseline evidence, a proposed contract, acceptance criteria, and a compatibility challenge. The implementation ledger records the narrower work actually delivered.

The 12 audit chunks describe complete file inventory coverage with selected deep review. Do not turn that into a claim that every line or hardware path has been validated. File hashes identify the original audit snapshot.

## Reporting issues

Use [GitHub issues](https://github.com/DarbotLM/LavaLM/issues) and include the commit, Python/dependency versions, operating system, run configuration, minimal graph, expected/actual behavior, and the worker traceback when startup fails. Include seeds and reference values for numerical differences.
