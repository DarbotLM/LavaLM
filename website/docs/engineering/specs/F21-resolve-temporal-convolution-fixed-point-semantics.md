# F21 Resolve temporal convolution fixed point semantics

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P1. Effort: M. Evidence: Source confirmed contract gap.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The model tagged fixed_pt declares floating weights, output and accumulation buffers. Its 24-bit clamp helper is not called by the inherited execution path. The tag therefore lacks an explicit implemented fixed-point contract.

## Proposed implementation

Define the intended input, weight, accumulator and output widths and whether arithmetic wraps or saturates. Implement that behavior with explicit intermediate dtypes and rounding, or mark the current model unsupported for bit-accurate use until conformance exists. Keep floating-point behavior separate.

## Acceptance criteria

1. A reference integer convolution matches multi-step outputs at overflow and underflow boundaries.
2. Negative values, graded inputs, multi-output kernels and recurrent timing are covered.
3. Selecting fixed_pt cannot silently select floating behavior advertised as bit accurate.

## Compatibility and review challenge

Do not apply clamp_precision blindly: its helper wraps signed values and may differ from the intended hardware arithmetic. The suspected flattened-roll cross-row bug was rejected because the first column is cleared before rolling.

## Dependencies and delivery

Dependencies: F31. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/proc/conv_in_time/models.py line 88](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/conv_in_time/models.py#L88)
- [src/lava/proc/conv_in_time/models.py line 98](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/proc/conv_in_time/models.py#L98)
