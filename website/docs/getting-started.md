# Getting started

## Supported starting point

Use Python 3.10 in an isolated environment on Linux for the CPU baseline. CI also exercises macOS. The package currently constrains Python to 3.10; newer interpreters require dependency and runtime validation before widening that promise. Optional Loihi packages are not needed for this example.

```bash
git clone https://github.com/DarbotLM/LavaLM.git
cd LavaLM
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python examples/cpu_smoke.py
```

For the pinned engineering validation environment, install `requirements/ci.txt` alongside the package. The inherited Poetry lock is retained as upstream history; these pip instructions do not claim to reproduce that older development environment.

## A one-step process

```python
import numpy as np
from lava.proc.lif.process import LIF
from lava.magma.core.run_conditions import RunSteps
from lava.magma.core.run_configs import Loihi1SimCfg

with LIF(shape=(1,), bias_mant=1, vth=100) as neuron:
    neuron.run(condition=RunSteps(num_steps=1),
               run_cfg=Loihi1SimCfg(select_tag="floating_pt"))
    voltage = neuron.v.get()
    np.testing.assert_allclose(voltage, [1.0])
```

The Process defines state and ports. The run configuration chooses a compatible implementation. `run()` compiles and creates the runtime as necessary. Exiting the context stops the process runtime, including when the body raises. The example in `examples/cpu_smoke.py` is exercised against installed packages in CI.

## Common setup problems

| Symptom | Check |
|---|---|
| Package rejects your Python version | Create a Python 3.10 environment; do not override the constraint to imply support. |
| `lava` imports resolve to unexpected code | Check for a co-installed `lava-nc` distribution; use a fresh environment. |
| Shared-memory startup raises EOFError | Inspect the worker traceback; restricted environments can deny socket creation. |
| Loihi backend import fails | Use the CPU configuration unless you have the separate compatible backend and hardware. |

A passing import or compile test is not evidence that worker startup succeeded. See [testing](testing.md) for the available checks.
