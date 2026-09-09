"""Project 01: Enterprise AI Inventory & Registration System — compact reference solution."""
import json,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_governance.inventory import registration_complete,missing_fields
def main():
    base=Path(__file__).resolve().parents[2]
    records=json.loads((base/"data"/"ai_inventory.json").read_text())
    print([(r["system_id"],registration_complete(r),missing_fields(r)) for r in records])

if __name__=="__main__":
    main()
