# F05 Stop adding root log handlers per process

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: S. Evidence: Reproduced.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Constructing three AbstractProcess objects added three handlers to the host root logger. Graph size can amplify duplicate output and retained handler state, while library initialization changes application logging.

## Proposed implementation

Use a library logger hierarchy with a NullHandler default. Make console/file configuration explicit at the application or session boundary. Preserve per-process context as structured fields or LoggerAdapter data rather than per-instance handlers. Apply the same policy to Compiler.

## Acceptance criteria

1. Creating and deleting 100 processes leaves the host root handler count unchanged.
2. A configured warning produces one record containing process ID and name.
3. Two independent graph sessions can use different logging context without duplicate records.

## Compatibility and review challenge

Users relying on automatic console setup need a documented configure_logging helper or a deprecation path.

## Dependencies and delivery

Dependencies: None. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: C02 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/magma/core/process/process.py line 175](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/process.py#L175)
- [src/lava/magma/compiler/compiler.py line 107](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler.py#L107)
