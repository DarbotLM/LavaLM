# F19 Specify learning expression and numeric conformance

## Maintenance batch status

No implementation change in this maintenance batch.

Status: Proposed. Priority: P2. Effort: M. Evidence: Source confirmed design improvement.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

The symbolic parser and the float/bit-approximate appliers form a custom numerical language. Future semantic-learning extensions need stable grammar, diagnostics and overflow rules rather than unconstrained expression expansion.

## Proposed implementation

Document the accepted grammar and numeric rules, cap expression size and nesting for external inputs, and preserve structured parse/evaluation errors. Evaluate the parsed representation with a restricted symbol set. Add differential tests against a simple reference evaluator and boundary vectors for fixed-point shifts, clipping and rounding.

## Acceptance criteria

1. Valid existing rules retain results and invalid syntax gives a location-aware error.
2. Long or deeply nested malformed rules fail within a finite resource budget.
3. Reference comparisons cover signed values, extremes, zero traces, all dependencies and seeded rounding.

## Compatibility and review challenge

The use of asteval alone is not proof of an exploitable path. No exploit was attempted or established; this is a language-contract and reliability improvement.

## Dependencies and delivery

Dependencies: F18. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/magma/core/learning/learning_rule_applier.py line 167](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/learning_rule_applier.py#L167)
- [src/lava/magma/core/learning/symbolic_equation.py line 847](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/symbolic_equation.py#L847)
- [src/lava/magma/core/learning/product_series.py line 366](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/magma/core/learning/product_series.py#L366)
