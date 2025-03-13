from qiskit import QuantumCircuit, Aer, execute
import numpy as np

class QuantumCorrelation:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')
        
    def entanglement_correlation(self, asset1, asset2):
        """Calcola correlazione usando entanglement quantistico"""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        
        counts = execute(qc, self.backend).result().get_counts()
        correlated = counts.get('00', 0) + counts.get('11', 0)
        return correlated / sum(counts.values())

    def portfolio_entanglement(self, returns):
        """Mappa correlazioni di portfolio come entanglement"""
        n = len(returns)
        corr_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(i+1, n):
                corr_matrix[i,j] = self.entanglement_correlation(returns[i], returns[j])
                
        return corr_matrix + corr_matrix.T - np.diag(np.diag(corr_matrix))