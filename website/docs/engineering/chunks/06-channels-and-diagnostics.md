# 06 Channels and diagnostics

PyPyChannel uses shared-memory ring slots, semaphore notifications and local callback threads. CspSelector waits for readiness; a separate optional watchdog diagnoses blocked calls. Correct shutdown and bounded diagnostics matter more than speculative transport replacement.

## Implementation specifications

- [F16 Define channel cancellation and thread ownership](../specs/F16-define-channel-cancellation-and-thread-ownership.md) — P1; M; Source confirmed.
- [F17 Bound watchdog resource usage](../specs/F17-bound-watchdog-resource-usage.md) — P2; M; Source confirmed.

## Coverage and boundaries

3 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/magma/compiler/channels/interfaces.py` — AST and structural risk scan.
- `src/lava/magma/compiler/channels/pypychannel.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/compiler/channels/watchdog.py` — AST and structural risk scan; focused review with cited finding.
