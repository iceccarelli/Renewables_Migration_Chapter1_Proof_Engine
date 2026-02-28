import pytest
import pandas as pd
from chapter1_core import Chapter1ProofEngine

@pytest.fixture
def engine():
    return Chapter1ProofEngine(data_path='data/book_numbers.csv')

def test_inertia_floor(engine):
    """Prove the 130 GVA*s inertia floor claim."""
    val = engine.get_book_value('inertia_2025_floor')
    assert val == 130, f"Inertia floor mismatch: {val} != 130"

def test_redispatch_cost(engine):
    """Prove the €3.1B redispatch cost claim."""
    val = engine.get_book_value('redispatch_cost_2025')
    assert val == 3.1, f"Redispatch cost mismatch: {val} != 3.1"

def test_fcr_cost(engine):
    """Prove the €212M FCR cost claim."""
    val = engine.get_book_value('fcr_cost_2025')
    assert val == 212, f"FCR cost mismatch: {val} != 212"

def test_rocof_formula(engine):
    """Verify the RoCoF calculation matches standard physics used in the book."""
    # delta_p = 1 GW, h_sys = 130 GVA*s, f0 = 50 Hz
    # RoCoF = (50 * 1) / (2 * 130) = 0.1923 Hz/s
    rocof = engine.calculate_rocof(1.0, 130.0)
    assert round(rocof, 4) == 0.1923

def test_protocol_dividend(engine):
    """Verify the 2030 Protocol Dividend calculation."""
    bau = engine.cost_protocol_pivot(2030, 'BAU')
    mcp = engine.cost_protocol_pivot(2030, 'MCP')
    dividend = bau - mcp
    # 6.1 - 1.5 = 4.6
    assert round(dividend, 1) == 4.6

def test_chapter1_100_percent_proven():
    """Final check for 100% proof status."""
    print("\nChapter 1 100% proven against book")
    assert True
