"""Optional demo visualization helpers."""
from __future__ import annotations

from pathlib import Path
import warnings


def write_tendency_plot(records: list[dict[str, object]], output_path: str | Path) -> bool:
    """Write a compact bar chart when matplotlib is available."""
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message=".*importlib-metadata.*")
            warnings.filterwarnings("ignore", category=UserWarning, module="setuptools.*")
            import matplotlib.pyplot as plt
    except Exception:
        return False

    names = [str(row["molecule_id"]) for row in records]
    scores = [float(row["relative_tendency_score"]) for row in records]
    colors = ["#4aa69a" if score < 0.40 else "#d9b24c" if score < 0.68 else "#a64040" for score in scores]

    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    ax.bar(names, scores, color=colors, edgecolor="#2f3a3a", linewidth=0.8)
    ax.axhspan(0.0, 0.40, color="#4aa69a", alpha=0.08, label="low")
    ax.axhspan(0.40, 0.68, color="#d9b24c", alpha=0.10, label="medium")
    ax.axhspan(0.68, 1.0, color="#a64040", alpha=0.08, label="high")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Relative tendency score")
    ax.set_title("Public demo tendency bands")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper left", frameon=False, ncol=3)
    fig.tight_layout()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return True
