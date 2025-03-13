from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
import numpy as np

class QuantumFourierAnalyzer:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')
        
    def quantum_fft_analysis(self, time_series):
        """Analisi di Fourier quantistica per serie temporali"""
        n = len(time_series)
        qc = QuantumCircuit(n)
        
        # Encoding dati
        for i, val in enumerate(time_series):
            qc.ry(val % (2*np.pi), i)
            
        # Applica QFT
        qc.append(QFT(n), range(n))
        qc.measure_all()
        
        counts = execute(qc, self.backend).result().get_counts()
        return self._analyze_frequencies(counts, n)

    def _analyze_frequencies(self, counts, n_qubits):
        """Estrazione frequenze dominanti"""
        freqs = {}
        for state, count in counts.items():
            freq = int(state, 2)/(2**n_qubits)
            freqs[freq] = freqs.get(freq, 0) + count
        return max(freqs, key=freqs.get)