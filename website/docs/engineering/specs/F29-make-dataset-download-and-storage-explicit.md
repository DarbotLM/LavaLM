# F29 Make dataset download and storage explicit

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

MNIST downloads use a package-local temporary directory even with a custom destination, begin with an HTTP mirror, have no request timeout or integrity manifest, and store object arrays loaded with pickle enabled.

## Proposed implementation

Use a user-selected or platform cache directory, unique temporary files, HTTPS sources, finite timeouts and verified dataset hashes. Validate IDX headers and payload lengths before reshaping. Store named numeric arrays in NPZ without pickle. Make download permission explicit and retain a deliberate migration path for trusted old caches.

## Acceptance criteria

1. Read-only installed packages can load/download into a writable user cache.
2. Truncation, wrong hash, malformed headers and network timeout leave no valid-looking partial cache.
3. Offline fixture tests exercise conversion without downloading the full dataset; image/label values match reference fixtures.

## Compatibility and review challenge

No current mirror availability was tested. Fetching a URL successfully is not an integrity check.

## Dependencies and delivery

Dependencies: F27. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/utils/dataloader/mnist.py line 21](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/dataloader/mnist.py#L21)
- [src/lava/utils/dataloader/mnist.py line 54](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/dataloader/mnist.py#L54)
- [src/lava/utils/dataloader/mnist.py line 39](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/utils/dataloader/mnist.py#L39)
