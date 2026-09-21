# F26 Make monitor probe limits explicit

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: S then M. Evidence: Source confirmed documented limitation.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The Monitor documentation limits an instance to one probe, while probe construction includes dynamic naming machinery that can look like multi-probe support. Repeated probes should not accidentally create partially supported model state.

## Proposed implementation

First enforce and document the current single-probe contract with an early descriptive error. Treat multi-probe support as a separate feature using a typed probe registry, unique names, per-probe shapes/dtypes and a clear memory budget. Keep visualization consumers independent of simulation execution.

## Acceptance criteria

1. A second unsupported probe fails before changing ports or Vars.
2. Existing one-probe monitoring remains compatible.
3. If multi-probe support is implemented, mixed Var/OutPort probes produce independent correctly shaped data and bounded storage.

## Compatibility and review challenge

This is a documented limitation, not a claimed regression. A 3D viewer should consume exported observations rather than drive the runtime.

## Dependencies and delivery

Dependencies: F23. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/proc/monitor/process.py line 21](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/monitor/process.py#L21)
- [src/lava/proc/monitor/process.py line 86](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/monitor/process.py#L86)
- [src/lava/proc/monitor/models.py line 17](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/monitor/models.py#L17)
