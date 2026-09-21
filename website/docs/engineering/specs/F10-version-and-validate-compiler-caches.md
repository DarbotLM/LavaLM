# F10 Version and validate compiler caches

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The cache is loaded by directory existence and process names without an explicit graph/configuration/version fingerprint. Writing temporarily clears builder parameters and restores them only after successful serialization.

## Proposed implementation

Create a versioned cache manifest containing a canonical graph signature, model identifiers, port shapes and dtypes, compilation options, backend versions and a declared policy for initial state and weights. Treat incompatible caches as misses. Write atomically. Avoid mutating live builders during serialization or restore them in finally. Keep the legacy pickle cache explicitly trusted-local only; a checksum does not make pickle safe.

## Acceptance criteria

1. Changed topology, dtype, shape, model, relevant parameter or compiler version invalidates the cache.
2. Fault injection during serialization leaves live builders and the previous cache intact.
3. Cache hit and miss produce equivalent outputs; corrupt manifests cause a useful miss or error.

## Compatibility and review challenge

A full portable compiler IR is a larger project. Start with cache validation and atomicity without promising cross-version pickle compatibility.

## Dependencies and delivery

Dependencies: F09. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/compiler/compiler.py line 236](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler.py#L236)
- [src/lava/magma/compiler/compiler.py line 297](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/compiler.py#L297)
