# 10 Utilities and persistence

Utilities cover sparse arrays, weight quantization, plotting, dataset downloads, checkpoint serialization and hardware environment setup. Prioritize correctness without changing scientific outputs: nonmutating sparse queries, symmetric checkpoint paths, atomic writes and explicit dataset storage.

## Implementation specifications

- [F27 Repair checkpoint paths and atomic persistence](../specs/F27-repair-checkpoint-paths-and-atomic-persistence.md) — P1; S then M; Reproduced.
- [F28 Make sparse queries nonmutating](../specs/F28-make-sparse-queries-nonmutating.md) — P1; S; Reproduced.
- [F29 Make dataset download and storage explicit](../specs/F29-make-dataset-download-and-storage-explicit.md) — P2; M; Source confirmed.

## Coverage and boundaries

10 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/utils/LICENSE` — inventory and content classification.
- `src/lava/utils/dataloader/mnist.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/utils/loihi.py` — AST and structural risk scan.
- `src/lava/utils/plots.py` — AST and structural risk scan.
- `src/lava/utils/profiler.py` — AST and structural risk scan.
- `src/lava/utils/serialization.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/utils/slurm.py` — AST and structural risk scan.
- `src/lava/utils/sparse.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/utils/system.py` — AST and structural risk scan.
- `src/lava/utils/weightutils.py` — AST and structural risk scan.
