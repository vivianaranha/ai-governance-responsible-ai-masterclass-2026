"""Project 13: AI Lifecycle & Change Governance — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_governance.controls import Control,control_coverage,missing_controls
def main():
    controls=[Control("GOV-001",True,True,True,True),Control("EVAL-001",True,True,False,False)]
    print({"coverage":control_coverage(controls),"missing":missing_controls(controls)})

if __name__=="__main__":
    main()
