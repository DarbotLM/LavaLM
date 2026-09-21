# 08 Process library and model fidelity

The library already includes dense and sparse synapses, delayed connections, convolution, LIF and adaptive neurons, resonators, sigma-delta models, S4D, continual-learning components, monitoring and simple spike generators. These are computational primitives, not an existing language-model training stack. Changes must preserve timing, overflow and learning behavior.

## Implementation specifications

- [F20 Normalize delayed synapse validation](../specs/F20-normalize-delayed-synapse-validation.md) — P1; S; Reproduced for sparse int32 and source confirmed.
- [F21 Resolve temporal convolution fixed point semantics](../specs/F21-resolve-temporal-convolution-fixed-point-semantics.md) — P1; M; Source confirmed contract gap.
- [F22 Keep S4D expansion matrices sparse](../specs/F22-keep-s4d-expansion-matrices-sparse.md) — P2; S then M; Source confirmed.
- [F23 Create a process model conformance matrix](../specs/F23-create-a-process-model-conformance-matrix.md) — P2; M; Design improvement from source inventory.
- [F26 Make monitor probe limits explicit](../specs/F26-make-monitor-probe-limits-explicit.md) — P2; S then M; Source confirmed documented limitation.

## Coverage and boundaries

46 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/proc/LICENSE` — inventory and content classification.
- `src/lava/proc/atrlif/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/atrlif/process.py` — AST and structural risk scan.
- `src/lava/proc/bit_check/models.py` — AST and structural risk scan.
- `src/lava/proc/bit_check/process.py` — AST and structural risk scan.
- `src/lava/proc/clp/id_broadcast/models.py` — AST and structural risk scan.
- `src/lava/proc/clp/id_broadcast/process.py` — AST and structural risk scan.
- `src/lava/proc/clp/novelty_detector/models.py` — AST and structural risk scan.
- `src/lava/proc/clp/novelty_detector/process.py` — AST and structural risk scan.
- `src/lava/proc/clp/nsm/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/clp/nsm/process.py` — AST and structural risk scan.
- `src/lava/proc/clp/prototype_lif/models.py` — AST and structural risk scan.
- `src/lava/proc/clp/prototype_lif/process.py` — AST and structural risk scan.
- `src/lava/proc/conv/models.py` — AST and structural risk scan.
- `src/lava/proc/conv/process.py` — AST and structural risk scan.
- `src/lava/proc/conv/utils.py` — AST and structural risk scan.
- `src/lava/proc/conv_in_time/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/conv_in_time/process.py` — AST and structural risk scan.
- `src/lava/proc/dense/models.py` — AST and structural risk scan.
- `src/lava/proc/dense/process.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/graded/models.py` — AST and structural risk scan.
- `src/lava/proc/graded/process.py` — AST and structural risk scan.
- `src/lava/proc/learning_rules/r_stdp_learning_rule.py` — AST and structural risk scan.
- `src/lava/proc/learning_rules/stdp_learning_rule.py` — AST and structural risk scan.
- `src/lava/proc/lif/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/lif/process.py` — AST and structural risk scan.
- `src/lava/proc/monitor/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/monitor/process.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/prodneuron/models.py` — AST and structural risk scan.
- `src/lava/proc/prodneuron/process.py` — AST and structural risk scan.
- `src/lava/proc/receiver/models.py` — AST and structural risk scan.
- `src/lava/proc/receiver/process.py` — AST and structural risk scan.
- `src/lava/proc/resfire/models.py` — AST and structural risk scan.
- `src/lava/proc/resfire/process.py` — AST and structural risk scan.
- `src/lava/proc/rf/models.py` — AST and structural risk scan.
- `src/lava/proc/rf/process.py` — AST and structural risk scan.
- `src/lava/proc/rf_iz/models.py` — AST and structural risk scan.
- `src/lava/proc/rf_iz/process.py` — AST and structural risk scan.
- `src/lava/proc/s4d/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/s4d/process.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/sdn/models.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/sdn/process.py` — AST and structural risk scan.
- `src/lava/proc/sparse/models.py` — AST and structural risk scan.
- `src/lava/proc/sparse/process.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/spiker/models.py` — AST and structural risk scan.
- `src/lava/proc/spiker/process.py` — AST and structural risk scan.
