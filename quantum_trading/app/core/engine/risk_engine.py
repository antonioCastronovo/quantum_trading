class RiskAssessmentEngine:
    def calculate_risk(self, positions):
        return sum(p['exposure'] for p in positions) * 0.618