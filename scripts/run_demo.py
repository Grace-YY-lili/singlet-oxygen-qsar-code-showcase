"""Run the public QSAR showcase demo.

This script demonstrates the repository shape only. It does not load manuscript
training data, CDFT tables, train/validation/test splits, or model weights.
"""
from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qsar_showcase.pipeline import run_demo  # noqa: E402


def main() -> int:
    input_csv = ROOT / "examples" / "example_smiles.csv"
    output_dir = ROOT / "outputs"
    records = run_demo(input_csv, output_dir)
    print(f"Wrote {len(records)} demo rows to {output_dir / 'demo_predictions.csv'}")
    print("This is a qualitative showcase output, not a paper reproduction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

