# Open-Source Curation Report

Date: 2026-07-10

Target prepared:

- curated public code showcase directory: `QSAR_Project_v3`

Recommended public repository names:

- `singlet-oxygen-qsar-code-showcase`
- `1o2-qsar-code-showcase`

Backups:

- original target backup before first overwrite: `../ML_lili_QSAR_Project_v3_backup_before_open_source_20260710_151447`
- figure-inclusive showcase backup before code-only trim: `../ML_lili_QSAR_Project_v3_backup_before_code_only_20260710_153912`

No GitHub upload, commit, push, or remote repository change was performed.

## Recommended Public File List

- `README.md`
- `LICENSE`
- `.gitignore`
- `requirements.txt`
- `environment.yml`
- `config/showcase_config.json`
- `examples/example_smiles.csv`
- `scripts/run_demo.py`
- `src/qsar_showcase/__init__.py`
- `src/qsar_showcase/features.py`
- `src/qsar_showcase/applicability.py`
- `src/qsar_showcase/model_stub.py`
- `src/qsar_showcase/pipeline.py`
- `src/qsar_showcase/visualization.py`
- `outputs/.gitkeep`
- `OPEN_SOURCE_CURATION_REPORT.md`

## Explicitly Not Public

- result figures, manuscript figures, screenshots, and figure source tables
- raw and processed training data
- train/validation/test split files
- complete CDFT descriptor tables
- complete RDKit/fusion feature matrices
- trained model weights and preprocessing objects
- hyperparameter search logs and internal experiment records
- full training, ablation, benchmark, and paper-result regeneration scripts
- notebooks, internal docs, deployment assets, nested Git metadata
- logs, caches, bytecode, temporary files, and historical failed outputs
- absolute local machine paths and remote credential material

## Actual Created Or Modified Files

Created or retained for public code display:

- `README.md`
- `LICENSE`
- `.gitignore`
- `requirements.txt`
- `environment.yml`
- `config/showcase_config.json`
- `examples/example_smiles.csv`
- `scripts/run_demo.py`
- `src/qsar_showcase/__init__.py`
- `src/qsar_showcase/features.py`
- `src/qsar_showcase/applicability.py`
- `src/qsar_showcase/model_stub.py`
- `src/qsar_showcase/pipeline.py`
- `src/qsar_showcase/visualization.py`
- `outputs/.gitkeep`
- `OPEN_SOURCE_CURATION_REPORT.md`

Removed from the public showcase during code-only trim:

- `results/figures/README.md`
- `results/figures/model_comparison_final_parity.png`
- `results/figures/applicability_domain_stability_overview.png`
- `results/figures/shap_structure_reactivity_summary.png`
- `results/figures/internal_decision_interaction_matrix.png`

## Purpose Of Each Public File

| File | Display purpose |
| --- | --- |
| `README.md` | Public-facing code-showcase overview, scope, quick browse, and reproducibility limits. |
| `LICENSE` | Code license plus explicit note that private research assets are excluded. |
| `.gitignore` | Prevents accidental release of data, model, result, cache, log, and local environment files. |
| `requirements.txt` | Minimal demo dependency note. |
| `environment.yml` | Optional environment shell for browsing the demo. |
| `config/showcase_config.json` | Documents demo-only configuration and release boundaries. |
| `examples/example_smiles.csv` | Small public SMILES examples without measured targets. |
| `scripts/run_demo.py` | One-command qualitative demo entry point. |
| `src/qsar_showcase/features.py` | Transparent lightweight descriptor interface. |
| `src/qsar_showcase/applicability.py` | Demo-only applicability label interface. |
| `src/qsar_showcase/model_stub.py` | Deterministic qualitative model stub; no trained model. |
| `src/qsar_showcase/pipeline.py` | Connects example input, feature view, AD, prediction stub, and outputs. |
| `src/qsar_showcase/visualization.py` | Optional local demo-output chart code; no committed result image. |
| `outputs/.gitkeep` | Keeps the demo output folder visible while generated outputs remain ignored. |
| `OPEN_SOURCE_CURATION_REPORT.md` | Records curation choices, exclusions, and residual checks. |

## GitHub Repository Relationship To Confirm

- Local parent/source remote detected earlier: `https://github.com/Grace-YY-lili/ML_lili.git`
- Confirm whether this code showcase should be uploaded as:
  - a subdirectory `QSAR_Project_v3` inside `Grace-YY-lili/ML_lili`, or
  - a separate dedicated public repository for the paper companion.
- Recommended approach: use a separate dedicated public repository with a
  clean name such as `singlet-oxygen-qsar-code-showcase`.
- Confirm final repository visibility, repository name, and citation text before upload.

No remote action was taken.

## Final Directory Tree

```text
QSAR_Project_v3/
|-- .gitignore
|-- LICENSE
|-- OPEN_SOURCE_CURATION_REPORT.md
|-- README.md
|-- environment.yml
|-- requirements.txt
|-- config/
|   `-- showcase_config.json
|-- examples/
|   `-- example_smiles.csv
|-- outputs/
|   `-- .gitkeep
|-- scripts/
|   `-- run_demo.py
`-- src/
    `-- qsar_showcase/
        |-- __init__.py
        |-- applicability.py
        |-- features.py
        |-- model_stub.py
        |-- pipeline.py
        `-- visualization.py
```

## Sensitive Information And Reproducibility Risk Check

Checks performed:

- No result image or `results/figures` directory remains in the curated target.
- No trained model file, preprocessor, split table, full CDFT table, `.pkl`,
  `.npz`, `.xlsx`, `.log`, `.pyc`, or nested `.git` content is included.
- The public demo uses deterministic qualitative scoring only. It cannot
  reproduce final paper predictions or paper metrics.
- The selected code shows interface shape and engineering style without exposing
  the private data, model weights, complete feature engineering, or full training
  workflow.
- README now frames the release as workflow-level readability and selected code
  modules, not as a complete implementation or result-level reproduction package.

Residual checks before GitHub upload:

- Re-run file tree, file-size, and sensitive-text scans immediately before upload.
- Confirm whether to use an independent repository or the existing `ML_lili`
  repository subdirectory.
