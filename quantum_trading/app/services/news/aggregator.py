from qiskit import QuantumCircuit
from qiskit.algorithms import Grover

class QuantumNewsAggregator:
    def __init__(self, sources):
        self.sources = sources
        self.grover = Grover()
        
    def get_relevant_news(self, keywords):
        """Ricerca quantistica di notizie rilevanti"""
        oracle = self._create_oracle(keywords)
        result = self.grover.amplify(oracle)
        return [self.sources[i] for i, bit in enumerate(result.top_measurement) if bit == '1']