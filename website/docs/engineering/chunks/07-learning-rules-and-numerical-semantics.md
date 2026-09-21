# 07 Learning rules and numerical semantics

Learning rules are parsed into symbolic products. Floating-point and bit-approximate appliers evaluate those products; dedicated random generators support trace updates and stochastic rounding. Keep their distinct semantics explicit and validate parameters before execution.

## Implementation specifications

- [F18 Validate learning parameters and make seeds reproducible](../specs/F18-validate-learning-parameters-and-make-seeds-reproducible.md) — P1; M; Reproduced validation gap and source confirmed RNG behavior.
- [F19 Specify learning expression and numeric conformance](../specs/F19-specify-learning-expression-and-numeric-conformance.md) — P2; M; Source confirmed design improvement.

## Coverage and boundaries

8 tracked files belong to this inventory chunk. The file manifest distinguishes structural scanning from focused source review. Test execution does not establish all-path correctness.

- `src/lava/magma/core/learning/constants.py` — AST and structural risk scan.
- `src/lava/magma/core/learning/learning_rule.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/learning/learning_rule_applier.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/learning/product_series.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/learning/random.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/learning/string_symbols.py` — AST and structural risk scan.
- `src/lava/magma/core/learning/symbolic_equation.py` — AST and structural risk scan; focused review with cited finding.
- `src/lava/magma/core/learning/utils.py` — AST and structural risk scan.
