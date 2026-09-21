# F16 Define channel cancellation and thread ownership

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M. Evidence: Source confirmed.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Port join methods signal callback threads but do not join them. The queue timeout implementation uses wall-clock time. Send/receive blocking has no consistent cancellation contract for runtime shutdown.

## Proposed implementation

Use monotonic deadlines, explicit OPEN/CLOSING/CLOSED state and bounded callback-thread joins. Wake blocked producers and consumers with a defined cancellation outcome. Preserve slot ownership until all array views and callbacks are released. Validate data before taking a slot and make failed copy operations restore slot accounting.

## Acceptance criteria

1. Full-buffer sender and empty-buffer receiver both unblock on close.
2. Repeated close leaves no live owned callback threads or shared-memory views.
3. FIFO ordering, peek semantics and exact payloads remain correct through wraparound; clock adjustments cannot extend a timeout.

## Compatibility and review challenge

Do not introduce zero-copy receive aliases without a separate ownership contract; the existing receive copy protects slot reuse.

## Dependencies and delivery

Dependencies: F04. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/compiler/channels/pypychannel.py line 156](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/channels/pypychannel.py#L156)
- [src/lava/magma/compiler/channels/pypychannel.py line 146](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/channels/pypychannel.py#L146)
- [src/lava/magma/compiler/channels/pypychannel.py line 293](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/compiler/channels/pypychannel.py#L293)
