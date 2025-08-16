# tests/test_returns.py
import numpy as np
import pandas as pd
import pytest
from src.analysis.returns import calculate_daily_returns, calculate_log_returns

def test_calculate_daily_returns():
    prices = pd.Series([100, 101, 100.5, 102, 101.5])
    expected = pd.Series([0.01, -0.00495, 0.01493, -0.00490])
    result = calculate_daily_returns(prices)
    np.testing.assert_almost_equal(result.values, expected.values, decimal=5)

def test_calculate_log_returns():
    prices = pd.Series([100, 101, 100.5, 102, 101.5])
    expected = pd.Series([0.00995, -0.00496, 0.01482, -0.00491])
    result = calculate_log_returns(prices)
    np.testing.assert_almost_equal(result.values, expected.values, decimal=5)