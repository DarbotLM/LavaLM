# SPDX-License-Identifier: BSD-3-Clause
"""One-step CPU simulation; requires permission to create worker processes."""
import numpy as np

from lava.magma.core.run_conditions import RunSteps
from lava.magma.core.run_configs import Loihi1SimCfg
from lava.proc.lif.process import LIF


def main():
    with LIF(shape=(1,), bias_mant=1, vth=100) as neuron:
        neuron.run(condition=RunSteps(num_steps=1),
                   run_cfg=Loihi1SimCfg(select_tag="floating_pt"))
        voltage = neuron.v.get()
        np.testing.assert_allclose(voltage, [1.0])
        print("LavaLM CPU smoke test passed:", voltage)


if __name__ == "__main__":
    main()
