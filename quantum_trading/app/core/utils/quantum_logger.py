import logging
from qiskit import QuantumCircuit, Aer, execute

class QuantumLogger:
    def __init__(self, name, log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.backend = Aer.get_backend('qasm_simulator')
        
    def log_entangled(self, message, level):
        """Registra log con entanglement quantistico"""
        qc = self._create_log_circuit(message)
        counts = execute(qc, self.backend).result().get_counts()
        entangled_msg = f"[Q] {message} | {max(counts, key=counts.get)}"
        self.logger.log(level, entangled_msg)
        
    def _create_log_circuit(self, message):
        """Crea circuito quantistico per logging"""
        qc = QuantumCircuit(len(message))
        for i, char in enumerate(message):
            qc.rx(ord(char) % (2*3.1415), i)
        qc.measure_all()
        return qc