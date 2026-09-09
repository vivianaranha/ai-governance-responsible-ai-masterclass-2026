from dataclasses import dataclass

@dataclass
class Control:
    control_id: str
    required: bool
    implemented: bool
    tested: bool
    evidence_present: bool

def control_coverage(controls: list[Control]) -> float:
    required=[c for c in controls if c.required]
    if not required:
        return 1.0
    complete=sum(c.implemented and c.tested and c.evidence_present for c in required)
    return round(complete/len(required),4)

def missing_controls(controls: list[Control]) -> list[str]:
    return [
        c.control_id for c in controls
        if c.required and not (c.implemented and c.tested and c.evidence_present)
    ]
