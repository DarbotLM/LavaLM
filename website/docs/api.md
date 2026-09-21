# API guide

This is a curated map of the inherited Python APIs, with links to implementation. LavaLM does not currently expose a REST API, hosted inference endpoint, or ACP server.

## Public building blocks

| API | Import | Purpose |
|---|---|---|
| `AbstractProcess` | `lava.magma.core.process.process` | Declare state and ports; compile, run, pause, wait, stop. |
| `Var` | `lava.magma.core.process.variable` | Shaped state with get/set and aliasing. |
| `InPort`, `OutPort`, `RefPort`, `VarPort` | `lava.magma.core.process.ports.ports` | Message and reference connectivity. |
| `RunSteps`, `RunContinuous` | `lava.magma.core.run_conditions` | Finite or continuous execution conditions. |
| `Loihi1SimCfg`, `Loihi2SimCfg` | `lava.magma.core.run_configs` | CPU model selection for protocol-specific simulation. |
| `PyLoihiProcessModel` | `lava.magma.core.model.py.model` | Python implementation of a Loihi-protocol process. |
| `implements`, `requires`, `tag` | `lava.magma.core.decorator` | Model/process association, resources, and tags. |
| `LavaPyType` | `lava.magma.core.model.py.type` | Declare model-side port/state types. |
| `save`, `load` | `lava.utils.serialization` | Trusted pickle checkpoints of processes and optional executables. |

## Connect a graph

```python
import numpy as np
from lava.proc.lif.process import LIF
from lava.proc.dense.process import Dense

source = LIF(shape=(2,))
weights = Dense(weights=np.ones((3, 2)))
target = LIF(shape=(3,))
source.s_out.connect(weights.s_in)
weights.a_out.connect(target.a_in)
```

The weight matrix maps two input channels to three output channels. Connecting ports declares the graph; it does not start execution. A subsequent `source.run(...)` uses the connected graph and selected models.

## Lifecycle and state access

`process.compile(run_cfg)` creates an executable. `process.run(condition, run_cfg)` can create the runtime and execute. A process context manager returns the process and stops its runtime on exit. A runtime context manager initializes, returns the runtime, and stops on exit.

`RunContinuous` is nonblocking; call pause or stop explicitly and verify the intended protocol supports the operation. Current `RunSteps` input validation and remote Var indexing have known gaps. Do not infer that arbitrary partial writes or full-width integer round trips are guaranteed; see F06 and F14 in the [specification index](engineering/overview.md).

## Checkpoints

```python
from lava.utils.serialization import save, load

save([source, weights, target], "experiment.v1/checkpoint")
processes, executable = load("experiment.v1/checkpoint")
```

The directory must already exist. A basename with no suffix receives `.pickle`; dots in parent directories do not count as an extension. Loading first tries the exact path to preserve legacy extensionless files, then the default suffix. Lists are validated before opening the destination. Checkpoints still use pickle and must come from a trusted source; atomic writes and portable versioned checkpoint formats remain future work.

## Sparse helpers and networks

`lava.utils.sparse.find(matrix, explicit_zeros=True)` uses a private working copy to preserve caller storage, including read-only data and exception paths. The existing SciPy ordering and coalescing behavior is retained. Algebraic vector connections and graded-vector products now allocate CSR identity matrices directly; this removes dense quadratic intermediates without changing the intended wiring.

For exact definitions and related imports, use the [production module index](engineering/module-index.md). Numerical models and learning APIs retain their inherited contracts until separate conformance work establishes changes.
