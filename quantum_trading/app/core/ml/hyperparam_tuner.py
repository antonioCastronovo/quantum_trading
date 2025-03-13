from qiskit.algorithms import VQE
from qiskit.circuit.library import RealAmplitudes

class QuantumHyperparamTuner:
    def tune(self, model, X, y):
        """Ottimizzazione iperparametri quantistica"""
        ansatz = RealAmplitudes(X.shape[1])
        vqe = VQE(ansatz, quantum_instance=Aer.get_backend('qasm_simulator'))
        
        def quantum_loss(params):
            model.set_params(params)
            return model.score(X, y)
            
        result = vqe.compute_minimum_eigenvalue(quantum_loss)
        return ansatz.bind_parameters(result.optimal_point)