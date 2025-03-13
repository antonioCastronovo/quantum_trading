from qiskit import QuantumCircuit, Aer, execute
import numpy as np

class QuantumVolatility:
    def __init__(self, window=14):
        self.window = window
        self.backend = Aer.get_backend('qasm_simulator')
        
    def calculate(self, prices):
        """Calcola volatilità quantistica con Quantum Fourier Transform"""
        qc = self._build_volatility_circuit(prices)
        counts = execute(qc, self.backend).result().get_counts()
        return self._compute_volatility(counts)
    
    def _build_volatility_circuit(self, prices):
        """Costruisci circuito per analisi volatilità"""
        n_qubits = min(5, len(prices))
        qc = QuantumCircuit(n_qubits)
        
        # Encoding dati
        for i in range(n_qubits):
            qc.ry(prices[i] % (2*np.pi), i)
            
        # Quantum Fourier Transform
        qc.append(QuantumFourierTransform(n_qubits), range(n_qubits))
        qc.measure_all()
        return qc

    def _compute_volatility(self, counts):
        """Calcola volatilità dai risultati quantistici"""
        total = sum(counts.values())
        return np.sqrt(sum((int(k,2) - total/2**5)**2 * v for k,v in counts.items())/total)