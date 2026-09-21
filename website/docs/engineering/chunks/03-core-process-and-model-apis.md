# 03 Core process and model APIs

AbstractProcess owns Vars and ports; ProcessModels implement behavior selected through decorators and RunConfig. SyncDomain and RunCondition govern execution. Preserve these boundaries. Improve small API contracts first, then make graph ownership and registries explicit for repeated workloads in long-running hosts.

## Implementation specifications

- [F05 Stop adding root log handlers per process](../specs/F05-stop-adding-root-log-handlers-per-process.md) — P1; S; Reproduced.
- [F06 Validate public run and shape contracts early](../specs/F06-validate-public-run-and-shape-contracts-early.md) — P1; S; Reproduced and source confirmed.
- [F07 Make iteration and graph ownership explicit](../specs/F07-make-iteration-and-graph-ownership-explicit.md) — P1; M; Reproduced and source confirmed.
- [F15 Return the context manager object](../specs/F15-return-the-context-manager-object.md) — P2; S; Reproduced for Runtime and source confirmed for Process.

## Coverage and boundaries

30 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/frameworks/loihi2.py` — AST and structural risk scan.
- `src/lava/magma/core/LICENSE` — inventory and content classification.
- `src/lava/magma/core/callback_fx.py` — AST and structural risk scan.
- `src/lava/magma/core/decorator.py` — AST and structural risk scan.
- `src/lava/magma/core/model/interfaces.py` — AST and structural risk scan.
- `src/lava/magma/core/model/model.py` — AST and structural risk scan.
- `src/lava/magma/core/model/py/connection.py` — AST and structural risk scan.
- `src/lava/magma/core/model/py/model.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/model/py/neuron.py` — AST and structural risk scan.
- `src/lava/magma/core/model/py/ports.py` — AST and structural risk scan.
- `src/lava/magma/core/model/py/type.py` — AST and structural risk scan.
- `src/lava/magma/core/model/spike_type.py` — AST and structural risk scan.
- `src/lava/magma/core/model/sub/model.py` — AST and structural risk scan.
- `src/lava/magma/core/process/connection.py` — AST and structural risk scan.
- `src/lava/magma/core/process/interfaces.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/process/message_interface_enum.py` — AST and structural risk scan.
- `src/lava/magma/core/process/neuron.py` — AST and structural risk scan.
- `src/lava/magma/core/process/ports/connection_config.py` — AST and structural risk scan.
- `src/lava/magma/core/process/ports/exceptions.py` — AST and structural risk scan.
- `src/lava/magma/core/process/ports/ports.py` — AST and structural risk scan.
- `src/lava/magma/core/process/ports/reduce_ops.py` — AST and structural risk scan.
- `src/lava/magma/core/process/process.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/process/variable.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/resources.py` — AST and structural risk scan.
- `src/lava/magma/core/run_conditions.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/run_configs.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/sync/domain.py` — AST and structural risk scan.
- `src/lava/magma/core/sync/protocol.py` — AST and structural risk scan.
- `src/lava/magma/core/sync/protocols/async_protocol.py` — AST and structural risk scan.
- `src/lava/magma/core/sync/protocols/loihi_protocol.py` — AST and structural risk scan.
