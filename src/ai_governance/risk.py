from dataclasses import dataclass

@dataclass
class RiskAssessment:
    likelihood: int
    impact: int
    exposure: int
    control_strength: int = 0

    @property
    def inherent(self) -> int:
        return self.likelihood * self.impact * self.exposure

    @property
    def residual(self) -> int:
        return max(self.inherent - self.control_strength, 0)

def risk_tier(score: int) -> str:
    if score >= 60:
        return "critical"
    if score >= 30:
        return "high"
    if score >= 12:
        return "medium"
    return "low"
