# src/analysis/returns.py
import numpy as np
import pandas as pd

def calculate_daily_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate daily returns from price series.
    
    Args:
        prices: Series of asset prices
        
    Returns:
        Series of daily returns
    """
    return prices.pct_change().dropna()

def calculate_log_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate log returns from price series.
    
    Args:
        prices: Series of asset prices
        
    Returns:
        Series of log returns
    """
    return np.log(prices / prices.shift(1)).dropna()

def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    """
    Calculate cumulative returns from daily returns.
    
    Args:
        returns: Series of daily returns
        
    Returns:
        Series of cumulative returns
    """
    return (1 + returns).cumprod() - 1