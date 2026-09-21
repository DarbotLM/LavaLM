# 04 Compiler and backend selection

The compiler discovers connected processes and model classes, expands subprocesses, groups graph components, invokes subcompilers, and produces builders, channels and an Executable. The public tree contains the Python backend and hooks for optional hardware extensions. Cache identity, graph traversal and configuration mapping need attention before adding new backends.

## Implementation specifications

- [F08 Correct output port configuration lookup](../specs/F08-correct-output-port-configuration-lookup.md) — P1; S; Reproduced with isolated compiler inputs.
- [F09 Bound graph traversal and compiler convergence](../specs/F09-bound-graph-traversal-and-compiler-convergence.md) — P1; M; Helper reproduced and source confirmed.
- [F10 Version and validate compiler caches](../specs/F10-version-and-validate-compiler-caches.md) — P1; M; Source confirmed.
- [F11 Expose backend capabilities and discovery failures](../specs/F11-expose-backend-capabilities-and-discovery-failures.md) — P2; L; Source confirmed design improvement.

## Coverage and boundaries

23 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/magma/compiler/LICENSE` — inventory and content classification.
- `src/lava/magma/compiler/builders/channel_builder.py` — AST and structural risk scan.
- `src/lava/magma/compiler/builders/interfaces.py` — AST and structural risk scan.
- `src/lava/magma/compiler/builders/py_builder.py` — AST and structural risk scan.
- `src/lava/magma/compiler/builders/runtimeservice_builder.py` — AST and structural risk scan.
- `src/lava/magma/compiler/channel_map.py` — AST and structural risk scan.
- `src/lava/magma/compiler/compiler.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/compiler/compiler_graphs.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/compiler/compiler_utils.py` — AST and structural risk scan.
- `src/lava/magma/compiler/exceptions.py` — AST and structural risk scan.
- `src/lava/magma/compiler/executable.py` — AST and structural risk scan.
- `src/lava/magma/compiler/mappable_interface.py` — AST and structural risk scan.
- `src/lava/magma/compiler/mapper.py` — AST and structural risk scan.
- `src/lava/magma/compiler/node.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/address.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/channel_builders_factory.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/channel_map_updater.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/constants.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/exceptions.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/interfaces.py` — AST and structural risk scan.
- `src/lava/magma/compiler/subcompilers/py/pyproc_compiler.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/compiler/utils.py` — AST and structural risk scan.
- `src/lava/magma/compiler/var_model.py` — AST and structural risk scan.
