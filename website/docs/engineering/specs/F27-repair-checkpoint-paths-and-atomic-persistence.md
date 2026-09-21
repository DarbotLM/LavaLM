# F27 Repair checkpoint paths and atomic persistence

## Maintenance batch status

Checkpoint suffix handling uses the basename; load has an exact-path-first fallback; save validates list members before opening the destination. Atomic writes, portable formats and version metadata remain open.

Status: Partial. Priority: P1. Effort: S then M. Evidence: Reproduced.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

save(model, path_without_suffix) adds .pickle but load(the_same_path) does not. The suffix check searches the whole path, so dots in directories change behavior. A list containing a non-Process value is accepted.

## Proposed implementation

Normalize paths through a shared helper using the basename suffix, validate every list member, and write a temporary sibling followed by atomic replace. Define exact-file precedence so existing suffixless files remain readable. Label pickle loading as trusted-local and retain it for compatibility; design a future versioned data checkpoint separately from executable-object persistence.

## Acceptance criteria

1. Round trips work with and without suffixes, dotted parent directories and explicit existing filenames.
2. Invalid process list elements fail before opening the destination.
3. Interrupted writes preserve the last valid checkpoint; legacy valid pickle files still load through the explicit legacy path.

## Compatibility and review challenge

Post-load type checks cannot make untrusted pickle safe. Do not promise portable or secure exchange merely by adding a schema field.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: U01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/utils/serialization.py line 74](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/serialization.py#L74)
- [src/lava/utils/serialization.py line 116](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/serialization.py#L116)
- [src/lava/utils/serialization.py line 121](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/serialization.py#L121)
