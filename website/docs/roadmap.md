# Roadmap

LavaLM's long-term goal is an open language-model and neurosemantic computing framework. Progress is gated by demonstrable contracts rather than naming or a visualization alone.

| Stage | Deliverable | Exit evidence |
|---|---|---|
| 0 · Foundation | Owned package identity, documentation, reproducible CI, bounded fixes | Built artifacts, passing targeted tests, live CPU validation |
| 1 · Reliable execution | Transactional startup/stop, caller-owned multiprocessing context, typed variable transfers, deterministic compilation | Failure-injection tests, deadlines, platform matrix |
| 2 · Numerical confidence | Dependency modernization, process conformance, sparse scaling, reproducible learning | Reference outputs, seed replay, memory/latency measurements |
| 3 · Semantic substrate | Versioned semantic records, codecs, provenance, schema evolution | Round trips, loss/error bounds, stable entity IDs |
| 4 · Agent and classifier adapters | Session lifecycle, cancellation, parallel orchestration, classifier contracts | Protocol conformance and workload evaluation |
| 5 · Graph and game applications | Semantic graph storage and optional 3D views, domain/task pattern experiments | Task accuracy, latency, resource use, explainable provenance |

## Proposed boundaries

A semantic record should carry a stable identity, schema version, payload type, provenance, and explicit uncertainty where applicable. A codec should declare whether conversion is lossless, which numerical representation it emits, and its measured reconstruction/task error. Model evaluation must compare against a documented baseline, not assume a neuromorphic representation is better.

The [Agent Client Protocol](https://agentclientprotocol.com/get-started/introduction) describes communication between clients and coding agents. An adapter can be evaluated against a pinned protocol version; ACP should not be presented as the semantic encoding format or as interchangeable with MCP. Neither protocol integration exists in the current codebase.

The earlier phrase “JEV-style classifiers” is an unresolved research input. No JEPA equivalence or concrete model architecture is assumed. Define the intended classifier design and benchmark before implementing its orchestration.

Graph identity, edges, provenance, and inference must be independent of 3D coordinates. A viewer is one projection of the graph, not its storage or truth model. Likewise, a company or industry schema needs explicit data provenance and evaluation before claims of optimized task patterns.

See F32 in the [specifications](engineering/overview.md) for the proposed module boundaries and acceptance criteria. Earlier reliability specifications are prerequisites, not automatic proof of language-model capability.
