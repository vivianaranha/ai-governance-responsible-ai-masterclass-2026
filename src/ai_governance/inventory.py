REQUIRED=("system_id","name","owner","purpose","users","deployment_status","risk_tier")

def registration_complete(record: dict) -> bool:
    return all(bool(record.get(k)) for k in REQUIRED)

def missing_fields(record: dict) -> list[str]:
    return [k for k in REQUIRED if not record.get(k)]
