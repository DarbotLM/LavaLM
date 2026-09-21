---
slug: /
title: LavaLM
---
# An open foundation for neurosemantic computing

**LavaLM — Open Source Language Model Framework for Neuro Semantic Computing and Machine Learning.**

LavaLM continues the Lava neuromorphic execution framework under DarbotLM. Its immediate engineering goal is a dependable, documented execution core on which semantic representations and learning experiments can be built.

## Choose a path

| Your goal | Start here |
|---|---|
| Run a CPU process | [Getting started](getting-started.md) |
| Understand the execution pipeline | [Architecture](architecture.md) |
| Build a process or integrate a model | [API guide](api.md) |
| Fix inherited code | [Engineering review](engineering/overview.md) |
| Explore semantic and agent layers | [Roadmap](roadmap.md) |

## What exists today

- Graph declarations through Processes, Vars, and ports.
- Python implementations of spiking and graded neural processes, learning-rule machinery, and composable networks.
- Model selection, compilation, runtime services, and shared-memory message transport for CPU execution.
- Extension points for specialized hardware. Hardware access and optional backends are separate from this repository's CPU baseline.

## What is being designed

Versioned semantic records and codecs, language-model workflows, agent protocol adapters, parallel classifiers, and graph-based applications remain proposals. A 3D view can present a knowledge graph; coordinates alone do not define its meaning. See the [staged roadmap](roadmap.md) for concrete evaluation gates.

LavaLM inherits from **lava-nc**, not **lava.so**. The commercial Lava Desktop and gateway product is a separate project. Read [lineage and compatibility](migration.md) before migrating an environment.
