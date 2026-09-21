# 05 Runtime and actor lifecycle

Runtime controls RuntimeServices, which coordinate ProcessModels over management channels. The CPU infrastructure creates OS processes and shared-memory channels. This is a usable parallel execution foundation, but it needs an explicit multiprocessing context, bounded failure handling and reliable ownership before serving agent requests.

## Implementation specifications

- [F12 Use an explicit multiprocessing context](../specs/F12-use-an-explicit-multiprocessing-context.md) — P1; L; Reproduced.
- [F13 Make runtime startup and cleanup transactional](../specs/F13-make-runtime-startup-and-cleanup-transactional.md) — P1; L; Reproduced cleanup defect and source confirmed lifecycle risks.
- [F14 Validate variable transactions and preserve data types](../specs/F14-validate-variable-transactions-and-preserve-data-types.md) — P1; M then L; Reproduced indexing defect and source confirmed transport limitation.

## Coverage and boundaries

12 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/magma/runtime/LICENSE` — inventory and content classification.
- `src/lava/magma/runtime/message_infrastructure/factory.py` — AST and structural risk scan.
- `src/lava/magma/runtime/message_infrastructure/message_infrastructure_interface.py` — AST and structural risk scan.
- `src/lava/magma/runtime/message_infrastructure/multiprocessing.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/runtime/message_infrastructure/nx.py` — AST and structural risk scan.
- `src/lava/magma/runtime/message_infrastructure/shared_memory_manager.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/runtime/mgmt_token_enums.py` — AST and structural risk scan.
- `src/lava/magma/runtime/runtime.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/runtime/runtime_services/channel_broker/channel_broker.py` — AST and structural risk scan.
- `src/lava/magma/runtime/runtime_services/enums.py` — AST and structural risk scan.
- `src/lava/magma/runtime/runtime_services/interfaces.py` — AST and structural risk scan.
- `src/lava/magma/runtime/runtime_services/runtime_service.py` — AST and structural risk scan.
