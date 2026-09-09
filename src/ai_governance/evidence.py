REQUIRED_FIELDS=("owner","control","test_result","date","artifact")

def evidence_completeness(evidence: dict) -> float:
    return round(sum(bool(evidence.get(k)) for k in REQUIRED_FIELDS)/len(REQUIRED_FIELDS),4)
