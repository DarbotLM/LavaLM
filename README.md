# LavaLM

**Open Source Language Model Framework for Neuro Semantic Computing and Machine Learning**

LavaLM is DarbotLM's independent continuation of the open-source Lava neuromorphic framework. The current implementation provides process graphs, CPU process models, a compiler, and a message-passing runtime. Neurosemantic schemas, language-model tooling, agent interfaces, parallel classifiers, and knowledge-graph applications are the development direction; they are not implemented capabilities of this maintenance release.

Start with the [wiki](website/docs/intro.md), [architecture](website/docs/architecture.md), [API guide](website/docs/api.md), and [engineering specifications](website/docs/engineering/overview.md).

## Install from source

Use Python 3.10 and a fresh environment. Linux is the primary CPU validation target; CI also exercises macOS. Python modernization and Windows runtime support require separate validation.

```bash
git clone https://github.com/DarbotLM/LavaLM.git
cd LavaLM
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python examples/cpu_smoke.py
```

The distribution is named `lavalm`; Python imports remain `lava.*` for compatibility. Do not install `lava-nc` and LavaLM into the same environment because they own the same import paths. No published PyPI package is asserted by these instructions.

## Work on the framework

```bash
python -m pip install -r requirements/ci.txt -e .
python -m pytest tests --ignore=tests/lava/tutorials --cov-report=term-missing --cov-fail-under=65
```

The runtime needs worker processes and shared-memory manager sockets. See [testing](website/docs/testing.md) for the distinction between bounded regression tests and live runtime validation.

## Run the Docusaurus wiki

Use Node.js 22 or newer:

```bash
cd website
npm ci
npm start
# Production build (validates links):
npm run build
```

The docs workflow uploads a preview artifact for each pull request and deploys from `main` once GitHub Pages uses the GitHub Actions source. The configured address is `https://darbotlm.github.io/LavaLM/`; configuration alone does not imply a live deployment. See [wiki maintenance](website/README.md).

## Lineage and licensing

This fork derives from [lava-nc/lava](https://github.com/lava-nc/lava), audited at commit `646fa535764c3b0bd1bf24b956aaf64561bf97f6`. Intel's upstream archive notice does not describe a support commitment for this independent fork. LavaLM is separate from the Lava Desktop/gateway product at lava.so.

Original notices and component licenses are retained: core, processes, and utilities use BSD-3-Clause; compiler and runtime use LGPL-2.1-or-later. Read [LICENSE](LICENSE) and the [migration guide](website/docs/migration.md). Changes to the compiler and runtime remain subject to their component licenses.

Report bugs and proposals in [DarbotLM/LavaLM issues](https://github.com/DarbotLM/LavaLM/issues). The [roadmap](website/docs/roadmap.md) separates maintenance work from research milestones.
