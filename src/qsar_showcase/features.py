"""Small SMILES feature view for the public demo.

The private project uses curated RDKit and CDFT descriptors. This module keeps
only a transparent, lightweight descriptor view so the public repository can
show the data flow without releasing the full feature engineering chain.
"""
from __future__ import annotations

from dataclasses import dataclass
import csv
import re
from pathlib import Path


ATOM_RE = re.compile(r"Cl|Br|[BCNOFPSI]|[cnops]")
SUPPORTED_CHARS = set("BCNOFPSIclbrnopsH0123456789=#()-+[]@/\\.")


@dataclass(frozen=True)
class DescriptorView:
    molecule_id: str
    smiles: str
    valid: bool
    warning: str
    smiles_length: int
    heavy_atom_proxy: int
    aromatic_atom_count: int
    hetero_atom_count: int
    halogen_count: int
    ring_marker_count: int
    branch_count: int
    double_bond_count: int
    phenol_like: int
    amine_like: int
    nitro_like: int

    def as_dict(self) -> dict[str, object]:
        return {
            "molecule_id": self.molecule_id,
            "smiles": self.smiles,
            "valid": self.valid,
            "warning": self.warning,
            "smiles_length": self.smiles_length,
            "heavy_atom_proxy": self.heavy_atom_proxy,
            "aromatic_atom_count": self.aromatic_atom_count,
            "hetero_atom_count": self.hetero_atom_count,
            "halogen_count": self.halogen_count,
            "ring_marker_count": self.ring_marker_count,
            "branch_count": self.branch_count,
            "double_bond_count": self.double_bond_count,
            "phenol_like": self.phenol_like,
            "amine_like": self.amine_like,
            "nitro_like": self.nitro_like,
        }


def load_smiles_csv(path: str | Path) -> list[dict[str, str]]:
    """Read a small CSV with molecule_id and smiles columns."""
    rows: list[dict[str, str]] = []
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"molecule_id", "smiles"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        for row in reader:
            rows.append({
                "molecule_id": (row.get("molecule_id") or "").strip(),
                "smiles": (row.get("smiles") or "").strip(),
            })
    return rows


def featurize_smiles(molecule_id: str, smiles: str) -> DescriptorView:
    """Compute a display-only descriptor view from a SMILES string."""
    clean = smiles.strip()
    warning = ""
    invalid_chars = sorted({ch for ch in clean if ch not in SUPPORTED_CHARS})
    tokens = ATOM_RE.findall(clean)
    valid = bool(clean) and bool(tokens) and not invalid_chars
    if not clean:
        warning = "empty SMILES"
    elif invalid_chars:
        warning = f"unsupported characters: {''.join(invalid_chars)}"
    elif not tokens:
        warning = "no supported atom tokens detected"

    aromatic_atom_count = sum(1 for token in tokens if token.islower())
    hetero_atom_count = sum(1 for token in tokens if token.upper() in {"N", "O", "S", "P"})
    halogen_count = sum(1 for token in tokens if token in {"F", "Cl", "Br", "I"})
    ring_marker_count = sum(1 for ch in clean if ch.isdigit())
    branch_count = clean.count("(") + clean.count(")")
    double_bond_count = clean.count("=")

    phenol_like = int("c1ccccc1O" in clean or "Oc1" in clean or "c(O)" in clean)
    amine_like = int("N" in clean or "n" in clean)
    nitro_like = int("[N+](=O)[O-]" in clean or "N(=O)=O" in clean)

    return DescriptorView(
        molecule_id=molecule_id or "unnamed",
        smiles=clean,
        valid=valid,
        warning=warning,
        smiles_length=len(clean),
        heavy_atom_proxy=len(tokens),
        aromatic_atom_count=aromatic_atom_count,
        hetero_atom_count=hetero_atom_count,
        halogen_count=halogen_count,
        ring_marker_count=ring_marker_count,
        branch_count=branch_count,
        double_bond_count=double_bond_count,
        phenol_like=phenol_like,
        amine_like=amine_like,
        nitro_like=nitro_like,
    )

