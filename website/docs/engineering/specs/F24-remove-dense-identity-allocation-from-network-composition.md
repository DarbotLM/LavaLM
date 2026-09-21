# F24 Remove dense identity allocation from network composition

## Maintenance batch status

AlgebraicVector connections and GradedVec products build CSR identity weights directly. Tests forbid np.eye and verify 10,000-dimensional sparse structure. Broader composition validation remains open.

Status: Partial. Priority: P1. Effort: S. Evidence: Source confirmed complexity issue.

Audited revision: `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Reviewed 21 September 2026.

## Current behavior and value

Identity wiring constructs an n by n dense array before converting it to CSR; vector products create more dense identities. This is quadratic temporary storage for a linear-size identity graph. ProductVec also indexes its two inputs without validating arity.

## Proposed implementation

Use direct sparse identity construction with the existing dtype and shape semantics. Validate vector compatibility and ProductVec arity before wiring any edges. Make composition return values consistent; decide whether NetworkList addition should copy instead of mutating an existing expression.

## Acceptance criteria

1. Small-network wiring and numerical outputs match the old implementation.
2. A large identity connection allocates O(n) sparse data with no dense n by n intermediate.
3. Invalid product inputs leave both graphs unchanged; chained composition follows the documented return contract.

## Compatibility and review challenge

Sparse construction is low risk; composition mutability is a separate API decision. Avoid changing both in the same patch.

## Dependencies and delivery

Dependencies: F28. Split mixed-size work into separate reviewable changes. Complete the targeted regression first, then the affected test lane. Preserve current valid behavior unless the specification explicitly declares a versioned change.

## Source evidence

- [src/lava/networks/network.py line 101](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/networks/network.py#L101)
- [src/lava/networks/gradedvecnetwork.py line 161](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/networks/gradedvecnetwork.py#L161)
- [src/lava/networks/gradedvecnetwork.py line 211](https://github.com/DarbotLM/LavaLM/blob/646fa535764c3b0bd1bf24b956aaf64561bf97f6/src/lava/networks/gradedvecnetwork.py#L211)
