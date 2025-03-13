def test_trading_engine():
    engine = QuantumTradingEngine()
    assert engine.generate_signal([]) is not None