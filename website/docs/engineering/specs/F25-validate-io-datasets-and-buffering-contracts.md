# F25 Validate IO datasets and buffering contracts

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: S then M. Evidence: Reproduced interval error and source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

A zero dataloader interval raises ZeroDivisionError rather than a useful validation error. The public Iterable annotation masks required indexing and length operations. Ring buffers assume a nonempty time dimension.

## Proposed implementation

Define an indexable sized dataset protocol or implement a separate streaming adapter. Validate nonempty datasets, sample/label shapes, positive intervals and buffer lengths before process construction. Preserve offset normalization. Document blocking, drop, FIFO and accumulation policies and expose dropped-sample counters where applicable.

## Acceptance criteria

1. Empty datasets, generators passed to the indexed API, inconsistent samples and zero intervals fail clearly.
2. Source/sink wraparound, padding, offset and label alignment match fixtures.
3. Injector/extractor close obeys the channel cancellation contract and drop counters match intentional overload.

## Compatibility and review challenge

Infinite streams require separate end-of-stream and cancellation semantics; do not silently materialize arbitrary iterables.

## Dependencies and delivery

Dependencies: F06 F16. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

Diagnostic evidence: I01 in `../evidence/reproductions.json`. These diagnostics describe the unmodified baseline; they are not post-fix tests.

## Source evidence

- [src/lava/proc/io/dataloader.py line 89](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/io/dataloader.py#L89)
- [src/lava/proc/io/dataloader.py line 43](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/io/dataloader.py#L43)
- [src/lava/proc/io/source.py line 42](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/io/source.py#L42)
- [src/lava/proc/io/utils.py line 196](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/io/utils.py#L196)
