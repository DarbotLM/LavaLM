# F23 Create a process model conformance matrix

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: M. Evidence: Design improvement from source inventory.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Many process families expose float and fixed-point models with different state and overflow semantics. Existing tests are valuable, but the repository does not expose one concise support matrix for model tags, dtypes, timing, learning and backend availability.

## Proposed implementation

Inventory each process/model pair and its supported combinations. Establish golden boundary vectors and differential reference tests for neurons, resonators, sigma-delta, dense/sparse synapses, convolutions and continual-learning allocation. Specify allocator behavior at prototype capacity. Optimize only measured hotspots after conformance is stable.

## Acceptance criteria

1. Every shipped public model has an explicit backend/tag/dtype/timing row.
2. Boundary fixtures cover sign, rounding, saturation or wrap, empty activity and repeated-run state.
3. Any optimization reports output equivalence plus latency and memory on a fixed workload and machine.

## Compatibility and review challenge

TODO comments are investigation prompts, not proof of numerical errors. No neuromorphic hardware fidelity was validated in this audit.

## Dependencies and delivery

Dependencies: F18 F20 F21 F31. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/proc/lif/models.py line 20](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/lif/models.py#L20)
- [src/lava/proc/atrlif/models.py line 195](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/atrlif/models.py#L195)
- [src/lava/proc/clp/nsm/models.py line 117](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/clp/nsm/models.py#L117)
- [src/lava/proc/sdn/models.py line 33](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/sdn/models.py#L33)
