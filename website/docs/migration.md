# Lineage, compatibility, and licenses

## Names have separate roles

| Name | Meaning |
|---|---|
| LavaLM | This independent DarbotLM project and its research direction. |
| `lavalm` | Distribution name emitted by this repository's package build. Registry ownership and publication are not asserted. |
| `lava.*` | Retained Python import namespace for first-fork compatibility. |
| lava-nc / Lava | The inherited neuromorphic software framework and upstream lineage. |
| lava.so | Separate Desktop/gateway product; its implementation is not part of this fork. |

Use a fresh environment when moving from `lava-nc`. Both distributions own `lava` paths, so installing or uninstalling them together can corrupt the shared namespace. Existing extensions can keep importing `lava.*`; test their supported dependency and backend versions separately.

## Version and support policy

The inherited version `0.11.0.dev0` is retained as a development lineage marker. It is not a new stable release or evidence of package registry ownership. The first maintenance work keeps Python 3.10 and the core numerical dependency baseline. Dependency upgrades, newer Python support, and process start-method changes need explicit conformance and runtime tests.

The original archive notice is preserved in git history. This fork does not imply renewed Intel support or access to proprietary hardware implementations.

## Component licenses

| Component | Existing license |
|---|---|
| `src/lava/magma/core` | BSD-3-Clause |
| `src/lava/magma/compiler` | LGPL-2.1-or-later |
| `src/lava/magma/runtime` | LGPL-2.1-or-later |
| `src/lava/proc`, `src/lava/utils`, tutorials | BSD-3-Clause |

The root [license map](https://github.com/DarbotLM/LavaLM/blob/main/LICENSE) and component license texts are retained. Source headers and upstream attribution are not globally renamed. New layers require an explicit license choice consistent with how they incorporate or link existing components.

## Release prerequisites

The package workflow builds and validates wheel and sdist artifacts without publishing. Before adding publication, establish registry ownership, release versioning, maintainer permissions, a protected environment, and a green runtime/packaging baseline. Do not reuse upstream PyPI targets or actor allowlists.
