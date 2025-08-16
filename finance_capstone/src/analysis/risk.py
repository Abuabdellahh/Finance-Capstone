# src/analysis/risk.py
import numpy as np
import pandas as pd
from scipy import stats

def calculate_rolling_volatility(returns: pd.Series, window: int = 21) -> pd.Series:
    """
    Calculate rolling volatility (annualized).
    
    Args:
        returns: Series of asset returns
        window: Rolling window in days
        
    Returns:
        Series of rolling volatility (annualized)
    """
    return returns.rolling(window=window).std() * np.sqrt(252)

def calculate_var_historical(returns: pd.Series, level: float = 5) -> float:
    """
    Calculate historical Value at Risk (VaR).
    
    Args:
        returns: Series of asset returns
        level: Confidence level (e.g., 5 for 95% confidence)
        
    Returns:
        Value at Risk as a percentage
    """
    return np.percentile(returns, level)

def calculate_cvar(returns: pd.Series, level: float = 5) -> float:
    """
    Calculate Conditional Value at Risk (CVaR).
    
    Args:
        returns: Series of asset returns
        level: Confidence level (e.g., 5 for 95% confidence)
        
    Returns:
        Conditional Value at Risk as a percentage
    """
    var = calculate_var_historical(returns, level)
    return returns[returns <= var].mean()

def adf_test(series: pd.Series) -> dict:
    """
    Augmented Dickey-Fuller test for stationarity.
    
    Args:
        series: Time series data
        
    Returns:
        Dictionary with test results
    """
    from statsmodels.tsa.stattools import adfuller
    result = adfuller(series)
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Critical Values': result[4]
    }