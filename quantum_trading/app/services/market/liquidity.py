from qiskit.algorithms import AmplificationProblem

class QuantumLiquidityAnalyzer:
    def calculate_liquidity(self, order_book):
        """Calcolo liquidità quantistica con Grover"""
        def is_liquid(oracle):
            return order_book['bid'] - order_book['ask'] < 0.618
            
        problem = AmplificationProblem(is_liquid)
        grover = Grover()
        result = grover.amplify(problem)
        return result.top_measurement['liquidity']