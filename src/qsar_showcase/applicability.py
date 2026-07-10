"""Transparent applicability-domain placeholder for the public demo."""
from __future__ import annotations

from dataclasses import dataclass

from .features import DescriptorView


@dataclass(frozen=True)
class ApplicabilityResult:
    label: str
    confidence: float
    flags: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "applicability_label": self.label,
            "applicability_confidence": round(self.confidence, 3),
            "applicability_flags": "; ".join(self.flags) if self.flags else "none",
        }


def assess_applicability(desc: DescriptorView) -> ApplicabilityResult:
    """Return a conservative public-demo AD label.

    The manuscript AD combines model-space diagnostics and structural similarity
    references. Those reference tables are private. This function is intentionally
    simple and should be read as a user-interface demonstration only.
    """
    if not desc.valid:
        return ApplicabilityResult("invalid_input", 0.0, (desc.warning,))

    flags: list[str] = []
    if desc.smiles_length > 80:
        flags.append("long_smiles")
    if desc.heavy_atom_proxy > 60:
        flags.append("large_structure")
    if desc.ring_marker_count > 8:
        flags.append("many_ring_markers")
    if desc.halogen_count >= 4:
        flags.append("halogen_rich")
    if desc.hetero_atom_count >= 8:
        flags.append("hetero_atom_rich")

    if not flags:
        return ApplicabilityResult("inside_demo_domain", 0.86, ())
    if len(flags) <= 2:
        confidence = max(0.45, 0.72 - 0.10 * len(flags))
        return ApplicabilityResult("borderline_demo_domain", confidence, tuple(flags))
    confidence = max(0.25, 0.55 - 0.08 * len(flags))
    return ApplicabilityResult("outside_demo_domain", confidence, tuple(flags))

