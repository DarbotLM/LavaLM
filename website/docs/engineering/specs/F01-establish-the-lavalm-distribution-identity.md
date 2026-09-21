# F01 Establish the LavaLM distribution identity

## Maintenance batch status

Distribution metadata and README now identify LavaLM, preserve lava imports and attribution, and define a fresh-environment migration. Package validation is added; registry ownership and publication remain open.

Status: Partial. Priority: P0. Effort: S. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

A renamed GitHub repository still builds a distribution named lava-nc and sends users to upstream support and installation targets. The archive banner describes Intel support, not a LavaLM maintenance policy. The repository has multiple license boundaries.

## Proposed implementation

Update project metadata, supported installation instructions, issue links and maintenance statement. Preserve upstream attribution and component licenses. Keep lava imports for the first compatible fork release; document that lava-nc and the fork must not be installed together if they own the same files. Confirm package-name ownership before publishing. Record version lineage and migration policy.

## Acceptance criteria

1. Build wheel and sdist; inspect METADATA, package paths and included license files.
2. Install each artifact in a clean environment outside the checkout and run a minimal CPU example.
3. README distinguishes current inherited functionality from planned neurosemantic and language-model work.

## Compatibility and review challenge

Do not globally replace lava imports or Intel notices. A namespace migration would break extension imports and existing pickles. Package registry ownership was not verified.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [pyproject.toml line 7](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/pyproject.toml#L7)
- [README.md line 1](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/README.md#L1)
- [LICENSE line 1](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/LICENSE#L1)
