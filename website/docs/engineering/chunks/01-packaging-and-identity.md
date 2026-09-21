# 01 Packaging and identity

Keep the useful Lava execution abstractions while establishing an independent LavaLM distribution. The current metadata, README installation commands, and support links still describe upstream lava-nc. Preserve the lava import namespace during the first maintenance release; a distribution rename and an import rename are separate compatibility decisions.

## Implementation specifications

- [F01 Establish the LavaLM distribution identity](../specs/F01-establish-the-lavalm-distribution-identity.md) — P0; S; Source confirmed.
- [F02 Modernize dependencies in controlled stages](../specs/F02-modernize-dependencies-in-controlled-stages.md) — P1; M; Source confirmed.

## Coverage and boundaries

12 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `.gitattributes` — inventory and content classification.
- `.gitignore` — inventory and content classification.
- `.gitmodules` — inventory and content classification.
- `LICENSE` — inventory and content classification; focused review with cited finding.
- `README.md` — inventory and content classification; focused review with cited finding.
- `poetry.lock` — inventory and content classification.
- `pyproject.toml` — inventory and content classification; focused review with cited finding.
- `utils/githook/fix-whitespace.sh` — inventory and content classification.
- `utils/githook/install-hook.sh` — inventory and content classification.
- `utils/githook/run-lint-flake.sh` — inventory and content classification.
- `utils/githook/run-pre-commit.sh` — inventory and content classification.
- `utils/githook/run-pytest.sh` — inventory and content classification.
