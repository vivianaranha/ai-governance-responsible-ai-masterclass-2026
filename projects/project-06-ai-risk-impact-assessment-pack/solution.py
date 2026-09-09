"""Project 06: AI Risk & Impact Assessment Pack — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_governance.impact import ImpactArea,rank_impacts
def main():
    impacts=[ImpactArea("employment fairness",5,5,4),ImpactArea("minor UX delay",1,3,1)]
    print([(x.name,x.score) for x in rank_impacts(impacts)])

if __name__=="__main__":
    main()
