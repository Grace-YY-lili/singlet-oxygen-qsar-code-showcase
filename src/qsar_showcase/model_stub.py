"""Qualitative tendency model stub for the public showcase.

No trained manuscript model is included here. The score below is deterministic
and transparent so reviewers can inspect the demo flow without receiving the
private model weights, target values, or full feature construction.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib

from .applicability import ApplicabilityResult
from .features import DescriptorView


@dataclass(frozen=True)
class PredictionResult:
    tendency_label: str
    relative_tendency_score: float
    reliability: str
    explanation: str

    def as_dict(self) -> dict[str, object]:
        return {
            "tendency_label": self.tendency_label,
            "relative_tendency_score": round(self.relative_tendency_score, 3),
            "reliability": self.reliability,
            "explanation": self.explanation,
        }


def predict_tendency(desc: DescriptorView, ad: ApplicabilityResult) -> PredictionResult:
    """Map public-demo descriptors to a qualitative tendency band."""
    if not desc.valid:
        return PredictionResult("not_evaluated", 0.0, "invalid", desc.warning)

    score = 0.18
    score += 0.035 * min(desc.aromatic_atom_count, 12)
    score += 0.045 * min(desc.hetero_atom_count, 8)
    score += 0.030 * min(desc.halogen_count, 4)
    score += 0.055 * desc.phenol_like
    score += 0.040 * desc.amine_like
    score += 0.035 * desc.nitro_like
    score += 0.010 * min(desc.double_bond_count, 4)

    digest = hashlib.sha256(desc.smiles.encode("utf-8")).hexdigest()
    jitter = (int(digest[:4], 16) % 41 - 20) / 1000
    score = min(0.98, max(0.02, score + jitter))

    if score < 0.40:
        label = "low"
    elif score < 0.68:
        label = "medium"
    else:
        label = "high"

    reliability = "screening_only"
    if ad.label == "borderline_demo_domain":
        reliability = "screening_only_borderline"
    elif ad.label == "outside_demo_domain":
        reliability = "screening_only_outside_domain"

    cues = []
    if desc.phenol_like:
        cues.append("phenol-like tag")
    if desc.amine_like:
        cues.append("amine/heteroaromatic cue")
    if desc.halogen_count:
        cues.append("halogen count")
    if desc.aromatic_atom_count:
        cues.append("aromatic structure")
    explanation = ", ".join(cues) if cues else "small structural descriptor view"

    return PredictionResult(label, score, reliability, explanation)

