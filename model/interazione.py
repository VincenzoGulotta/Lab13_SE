from dataclasses import dataclass

@dataclass
class Interazione:
    id_gene1: str
    id_gene2: str
    cromosoma_1: int
    cromosoma_2: int
    correlazione: float

    def __str__(self):
        return f'{self.id_gene1} - {self.id_gene2}: {self.cromosoma_1} - {self.cromosoma_2}: {self.correlazione}'

    def __hash__(self):
        return hash(self.id_gene1)
