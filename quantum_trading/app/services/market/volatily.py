from qiskit.algorithms import EstimationProblem
from qiskit.algorithms import AmplitudeEstimation

class QuantumVolatilityCalculator:
    def calculate(self, price_series):
        """Calcolo volatilità con Quantum Amplitude Estimation"""
        problem = EstimationProblem(
            state_preparation=self._create_state_preparation(price_series),
            objective_qubits=[0]
        )
        ae = AmplitudeEstimation(3)  # 3 qubit di precisione
        result = ae.estimate(problem)
        return result.estimation * 1.618  # Fattore quantistico