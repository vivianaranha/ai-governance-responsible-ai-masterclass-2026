"""Project 02: AI Risk Tiering Workbench — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_governance.risk import RiskAssessment,risk_tier
def main():
    x=RiskAssessment(4,5,4,15)
    print({"inherent":x.inherent,"residual":x.residual,"tier":risk_tier(x.residual)})

if __name__=="__main__":
    main()
