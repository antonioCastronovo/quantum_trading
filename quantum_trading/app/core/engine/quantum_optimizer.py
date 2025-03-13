from qiskit.algorithms import QAOA
from qiskit_optimization.applications import PortfolioOptimization
import numpy as np

class QuantumPortfolioOptimizer:
    def __init__(self, risk_model):
        self.risk_model = risk_model
        self.backend = Aer.get_backend('qasm_simulator')
        
    def optimize(self, returns, cov_matrix, budget):
        """Ottimizzazione portfolio quantistica con QAOA"""
        portfolio = PortfolioOptimization(
            returns, 
            cov_matrix, 
            budget,
            risk_factor=self.risk_model.factor
        )
        qp = portfolio.to_quadratic_program()
        
        qaoa = QAOA(reps=3, quantum_instance=self.backend)
        result = qaoa.compute_minimum_eigenvalue(qp.to_ising()[0])
        
        return self._interpret_solution(result, qp)

    def _interpret_solution(self, result, qp):
        """Interpreta i risultati quantistici"""
        solution = result.eigenstate
        optimal_weights = np.array([solution.probabilities([i]) for i in range(qp.get_num_vars())])
        return optimal_weights / np.sum(optimal_weights)