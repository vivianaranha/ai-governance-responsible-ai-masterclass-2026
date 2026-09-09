from dataclasses import dataclass

@dataclass
class ImpactArea:
    name: str
    severity: int
    affected_population: int
    reversibility: int

    @property
    def score(self) -> int:
        return self.severity * self.affected_population * self.reversibility

def rank_impacts(items: list[ImpactArea]) -> list[ImpactArea]:
    return sorted(items,key=lambda x:x.score,reverse=True)
