from qiskit import QuantumCircuit

class QuantumTradingEngine:
    def generate_signal(self, data):
        qc = QuantumCircuit(3)
        qc.h(range(3))
        return qc