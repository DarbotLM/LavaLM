# F03 Repair release artifact and publishing workflows

## Maintenance batch status

Replaced inherited publishing with owned wheel/sdist build and install checks, using compatible artifact actions. Publication and release governance are deferred; no registry upload is configured.

Status: Partial. Priority: P0. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

CD combines upload-artifact v3 with download-artifact v4, includes unquoted pip version expressions containing shell redirection characters, supplies a literal prerelease expression, and gates publishing on upstream usernames and lava-nc metadata.

## Proposed implementation

Use a compatible supported pair of artifact actions pinned to reviewed commits, unique artifact names and checksums. Quote every requirement or install a requirements file. Use a real expression for the prerelease input. Replace actor-name checks with the LavaLM release environment and owned publishing configuration. Build once, test those exact bytes, then publish those bytes. Update CODEOWNERS and project automation to actual maintainers.

## Acceptance criteria

1. A dispatch builds and downloads the same wheel and sdist; checksum comparisons succeed.
2. A prerelease creates a correctly marked draft and does not run stable publishing.
3. A dry run from an authorized maintainer reaches the owned release environment with the intended package name and minimal permissions.

## Compatibility and review challenge

Publishing credentials and repository environment settings were not inspected. This is a release blocker, not evidence that an unauthorized release occurred.

## Dependencies and delivery

Dependencies: F01. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [.github/workflows/cd.yml line 26](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/.github/workflows/cd.yml#L26)
- [.github/workflows/cd.yml line 102](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/.github/workflows/cd.yml#L102)
- [.github/workflows/cd.yml line 180](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/.github/workflows/cd.yml#L180)
- [.github/CODEOWNERS line 1](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/.github/CODEOWNERS#L1)
