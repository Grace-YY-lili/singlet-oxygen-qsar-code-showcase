# Singlet Oxygen QSAR: Code Showcase

This repository is a lightweight code showcase accompanying a QSAR study of
organic pollutant reactivity toward singlet oxygen (1O2). It contains selected
Python modules that illustrate the workflow style used in the study. It is not
a full implementation and not a reproduction package.

The public release is intentionally small. Its purpose is to show the coding
structure, data-flow boundaries, and interface design without publishing the
private dataset, optimized model artifacts, manuscript figures, or result
regeneration workflow.

## Research Goal

The private project studies how molecular structure and electronic descriptors
can be combined to estimate 1O2 reaction-rate tendency. The full research
workflow evaluates structural descriptors, CDFT electronic descriptors,
conservative fusion logic, applicability-domain checks, and interpretation
analyses. Those private assets are not released here.

## Method Overview

The manuscript workflow is summarized by four ideas:

- Structural context from SMILES-derived molecular descriptors.
- Electronic correction from CDFT descriptors supplied by quantum-chemistry
  calculations.
- Conservative fusion logic for the final prediction route.
- Applicability-domain and interpretation checks to avoid over-reading model
  outputs.

The public demo keeps only the interface shape: SMILES input, lightweight
descriptor extraction, a qualitative tendency band, a demo applicability label,
and optional local demo output. The trained manuscript models, complete feature
tables, full split definitions, final figures, and result-regeneration scripts
are not included.

## Workflow Overview

```text
SMILES examples
      |
      v
Lightweight descriptor view
      |
      v
Demo applicability assessment
      |
      v
Qualitative model interface
      |
      v
Screening-style output table
```

The private research workflow contains additional steps for CDFT descriptor
curation, feature selection, model optimization, validation, and manuscript
figure generation. Those steps are represented here only as clean interfaces or
documentation boundaries.

## What Is Included

- A small qualitative SMILES demo in `scripts/run_demo.py`.
- A compact public package in `src/qsar_showcase/`.
- Five public example SMILES without target values.
- Environment files and `.gitignore` tuned for a public code repository.
- `OPEN_SOURCE_CURATION_REPORT.md`, documenting what was included and excluded.

## Module Map

| Module | Role in this showcase |
| --- | --- |
| `features.py` | Builds a small public descriptor view from SMILES strings. |
| `applicability.py` | Demonstrates the shape of an applicability-domain check. |
| `model_stub.py` | Provides a deterministic qualitative prediction interface. |
| `pipeline.py` | Connects input loading, descriptors, AD labels, and outputs. |
| `visualization.py` | Contains optional local demo plotting code; no result image is committed. |

## Quick Browse

```bash
python scripts/run_demo.py
```

The demo writes:

- `outputs/demo_predictions.csv`
- `outputs/demo_tendency_summary.png` when `matplotlib` is available

Example output columns include:

- `molecule_id`
- `tendency_label`
- `relative_tendency_score`
- `applicability_label`
- `explanation`

These outputs are qualitative showcase outputs. They do not reproduce the paper
model and should not be cited as final quantitative predictions.

## Directory Structure

```text
.
|-- README.md
|-- OPEN_SOURCE_CURATION_REPORT.md
|-- config/
|   `-- showcase_config.json
|-- examples/
|   `-- example_smiles.csv
|-- scripts/
|   `-- run_demo.py
|-- src/
|   `-- qsar_showcase/
|       |-- applicability.py
|       |-- features.py
|       |-- model_stub.py
|       |-- pipeline.py
|       `-- visualization.py
`-- outputs/
```

## Suggested Public Repository Name

The local folder name `QSAR_Project_v3` is an internal working name. For a public
GitHub release, a cleaner repository name is recommended, for example:

- `singlet-oxygen-qsar-code-showcase`
- `1o2-qsar-code-showcase`

Using a dedicated public repository avoids exposing internal version history or
mixing this curated release with other research workspaces.

## Reproducibility Limits

This public repository intentionally excludes:

- Raw and processed training data.
- Train/validation/test split files.
- Complete CDFT descriptor tables.
- Trained model weights and preprocessing objects.
- Manuscript result figures and figure source tables.
- Hyperparameter search logs and internal experiment records.
- Full training, ablation, and paper-result regeneration scripts.
- Private paths, caches, notebooks, logs, and historical failed outputs.

The repository supports workflow-level readability and interface demonstration.
It does not support result-level reproduction of the manuscript metrics,
predictions, or figures.

## Citation

If this repository is used while discussing the study, cite the accompanying
paper after publication. Until then, reference it as a selected code showcase
for the manuscript.

## License

Code in this curated repository is provided under the MIT License unless noted
otherwise. Raw data, trained models, result figures, private experimental
assets, and the complete reproduction workflow are not released here.
