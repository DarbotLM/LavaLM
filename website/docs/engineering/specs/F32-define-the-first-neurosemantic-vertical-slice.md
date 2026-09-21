# F32 Define the first neurosemantic vertical slice

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P3. Effort: L for specification then staged experiments. Evidence: Proposed future architecture.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The repository provides neuromorphic execution primitives, but no reviewed source implements a complete language-model training stack, Agent Client Protocol adapter, semantic schema store, 3D graph product or game-learning engine.

## Proposed implementation

Define a backend-neutral SemanticRecord with stable ID, schema version, typed features, provenance, time and optional task/company/industry/context fields. Encode records into typed tensors/events through a versioned codec. Implement one small contextual classification/retrieval task with a baseline, an existing Lava process implementation and an evaluator. Add a separately versioned agent adapter, graph projection and game adapter only after this slice meets its accuracy, latency and memory gates.

## Acceptance criteria

1. Codec round trips preserve all declared fields, reject unsupported versions and expose any lossy transform.
2. Two classifier branches can run with independent recorded state and a documented deterministic aggregation policy.
3. Graph entities and relationships remain meaningful without 3D coordinates; the viewer is a projection.
4. An agent request supports capability discovery, cancellation, typed errors and explicit permission boundaries through the selected protocol revision.

## Compatibility and review challenge

ACP is a client-agent interoperability protocol, not a neural encoding format. Confirm the intended protocol and revision before implementation. The earlier phrase jev style is unresolved and must not silently become a JEPA specification. No language-model quality or neuromorphic advantage is established.

## Dependencies and delivery

Dependencies: F11 F12 F13 F14 F18 F23 F31. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/core/process/process.py line 37](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/process/process.py#L37)
- [src/lava/magma/core/model/py/model.py line 261](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/model/py/model.py#L261)
- [src/lava/proc/s4d/models.py line 22](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/s4d/models.py#L22)
- [src/lava/networks/network.py line 13](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/networks/network.py#L13)
