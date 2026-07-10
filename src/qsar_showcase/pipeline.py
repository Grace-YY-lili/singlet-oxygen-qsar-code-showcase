"""End-to-end public demo pipeline."""
from __future__ import annotations

from pathlib import Path
import csv

from .applicability import assess_applicability
from .features import featurize_smiles, load_smiles_csv
from .model_stub import predict_tendency
from .visualization import write_tendency_plot


def run_demo(input_csv: str | Path, output_dir: str | Path) -> list[dict[str, object]]:
    """Run the qualitative public demo and write CSV/optional PNG outputs."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = load_smiles_csv(input_csv)

    records: list[dict[str, object]] = []
    for row in rows:
        desc = featurize_smiles(row["molecule_id"], row["smiles"])
        ad = assess_applicability(desc)
        pred = predict_tendency(desc, ad)
        records.append({
            **desc.as_dict(),
            **ad.as_dict(),
            **pred.as_dict(),
        })

    csv_path = output_dir / "demo_predictions.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)

    plot_path = output_dir / "demo_tendency_summary.png"
    write_tendency_plot(records, plot_path)
    return records

