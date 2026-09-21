# 09 IO and network composition

Network wrappers provide algebraic wiring, while sources, sinks, dataloaders, injectors, extractors and encoders connect external arrays to process graphs. Large identity matrices and weak dataset contracts are practical early improvements. Retain the existing blocking and drop policies and make them observable.

## Implementation specifications

- [F24 Remove dense identity allocation from network composition](../specs/F24-remove-dense-identity-allocation-from-network-composition.md) — P1; S; Source confirmed complexity issue.
- [F25 Validate IO datasets and buffering contracts](../specs/F25-validate-io-datasets-and-buffering-contracts.md) — P1; S then M; Reproduced interval error and source confirmed.

## Coverage and boundaries

12 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/networks/gradedvecnetwork.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/networks/network.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/networks/resfire.py` — AST and structural risk scan.
- `src/lava/proc/io/__init__.py` — AST and structural risk scan.
- `src/lava/proc/io/dataloader.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/io/encoder.py` — AST and structural risk scan.
- `src/lava/proc/io/extractor.py` — AST and structural risk scan.
- `src/lava/proc/io/injector.py` — AST and structural risk scan.
- `src/lava/proc/io/reset.py` — AST and structural risk scan.
- `src/lava/proc/io/sink.py` — AST and structural risk scan.
- `src/lava/proc/io/source.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/proc/io/utils.py` — AST and structural risk scan; focused review with cited finding.
