import sys
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))

from ai_governance.risk import RiskAssessment,risk_tier
from ai_governance.controls import Control,control_coverage,missing_controls
from ai_governance.evidence import evidence_completeness
from ai_governance.inventory import registration_complete,missing_fields
from ai_governance.impact import ImpactArea,rank_impacts

class GovernanceTests(unittest.TestCase):
    def test_risk_scores(self):
        x=RiskAssessment(4,5,4,10)
        self.assertEqual(x.inherent,80)
        self.assertEqual(x.residual,70)

    def test_tier(self):
        self.assertEqual(risk_tier(70),"critical")
        self.assertEqual(risk_tier(20),"medium")

    def test_control_coverage(self):
        cs=[Control("a",True,True,True,True),Control("b",True,True,False,True)]
        self.assertEqual(control_coverage(cs),.5)

    def test_missing_controls(self):
        cs=[Control("a",True,True,True,True),Control("b",True,False,False,False)]
        self.assertEqual(missing_controls(cs),["b"])

    def test_evidence(self):
        e={"owner":"x","control":"c","test_result":"pass","date":"2026-09-01","artifact":"file"}
        self.assertEqual(evidence_completeness(e),1.0)

    def test_inventory_complete(self):
        r={"system_id":"1","name":"x","owner":"y","purpose":"p","users":"u","deployment_status":"pilot","risk_tier":"high"}
        self.assertTrue(registration_complete(r))
        self.assertEqual(missing_fields(r),[])

    def test_inventory_missing(self):
        r={"system_id":"1"}
        self.assertIn("owner",missing_fields(r))

    def test_impact_rank(self):
        xs=[ImpactArea("minor",1,1,1),ImpactArea("major",4,5,4)]
        self.assertEqual(rank_impacts(xs)[0].name,"major")

if __name__=="__main__":
    unittest.main()
